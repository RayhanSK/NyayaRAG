import json
import glob
import os
import numpy as np
import faiss
from transformers import DPRContextEncoder, DPRContextEncoderTokenizer
import torch

document_folder = "../Documents/"
json_files = glob.glob(os.path.join(document_folder, "*.json"))

texts = []
metadata = []

for file_path in json_files:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for chunk in data.get("chunks", []):
        text = " ".join([
            chunk.get("title", ""),
            chunk.get("content", ""),
            chunk.get("summary", "")
        ]).strip()
        texts.append(text)
        meta = {
            "id": chunk.get("id"),
            "type": chunk.get("type"),
            "topic":chunk.get("topic"),
            "source_file": os.path.basename(file_path)
        }
        for k in ["topic", "section", "confidence"]:
            if k in chunk:
                meta[k] = chunk[k]
        metadata.append(meta)

context_encoder = DPRContextEncoder.from_pretrained("facebook/dpr-ctx_encoder-single-nq-base")
context_tokenizer = DPRContextEncoderTokenizer.from_pretrained("facebook/dpr-ctx_encoder-single-nq-base")

BATCH_SIZE = 16
embeddings = []
for i in range(0, len(texts), BATCH_SIZE):
    batch_texts = texts[i:i+BATCH_SIZE]
    inputs = context_tokenizer(batch_texts, return_tensors="pt", padding=True, truncation=True, max_length=256)
    with torch.no_grad():
        outputs = context_encoder(**inputs)
        batch_embeds = outputs.pooler_output.cpu().numpy()
        embeddings.append(batch_embeds)

embeddings = np.vstack(embeddings) 
dimension = embeddings.shape[1]
faiss_index = faiss.IndexFlatIP(dimension)  

faiss_index.add(np.array(embeddings))

np.save("embeddings.npy", embeddings)
faiss.write_index(faiss_index, "faiss_index.bin")
with open("metadata.json", "w", encoding="utf-8") as f:
    json.dump(metadata, f, ensure_ascii=False, indent=2)

print(f"Processed {len(texts)} chunks from {len(json_files)} files.")
