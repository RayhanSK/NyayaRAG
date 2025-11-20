import json
import glob
import os
import numpy as np
import faiss
from transformers import DPRContextEncoder, DPRContextEncoderTokenizer
import torch
import nltk
from nltk.tokenize import sent_tokenize

# Ensure nltk punkt resource is available
nltk.download('punkt_tab')
nltk.download('punkt')

# ----------- Smart Chunk Function -----------
def smart_chunk(content, chunk_base, max_tokens=350, overlap=40):
    sentences = sent_tokenize(content)
    chunks = []
    current = []
    curr_len = 0

    # Crude token counter (can swap w/ HF tokenizer for accuracy)
    def token_count(text):
        return len(text.split())

    for s in sentences:
        if curr_len + token_count(s) > max_tokens:
            chunk_content = " ".join(current)
            new_chunk = chunk_base.copy()
            new_chunk["content"] = chunk_content
            new_chunk["id"] = f'{chunk_base.get("id", "")}-part{len(chunks)}'
            chunks.append(new_chunk)
            # Overlap: keep last X tokens of previous chunk in next
            overlap_tokens = 0
            overlap_sentences = []
            for cs in reversed(current):
                overlap_tokens += token_count(cs)
                overlap_sentences.insert(0, cs)
                if overlap_tokens >= overlap:
                    break
            current = overlap_sentences.copy()
            curr_len = sum(token_count(cs) for cs in current)
        current.append(s)
        curr_len += token_count(s)
    if current:
        chunk_content = " ".join(current)
        new_chunk = chunk_base.copy()
        new_chunk["content"] = chunk_content
        new_chunk["id"] = f'{chunk_base.get("id", "")}-part{len(chunks)}'
        chunks.append(new_chunk)
    return chunks

# ----------- Document Loading and Chunking -----------
document_folder = "../Documents/"
json_files = glob.glob(os.path.join(document_folder, "*.json"))

texts, metadata = [], []

for file_path in json_files:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for i, chunk in enumerate(data.get("chunks", [])):
        base_meta = {
            "type": chunk.get("type", ""),
            "title": chunk.get("title", ""),
            "summary": chunk.get("summary", ""),
            "keywords": chunk.get("keywords", []),
            "confidence": chunk.get("confidence", 1.0),
            "section": chunk.get("section", ""),
            "topic": chunk.get("topic", []),
            "source_file": os.path.basename(file_path),
            "id": chunk.get("id", f"{os.path.basename(file_path)}-chunk{i}")
        }
        smart_chunks = smart_chunk(chunk.get("content", ""), base_meta)
        for sc in smart_chunks:
            text = " ".join([sc.get("title", ""), sc.get("content", ""), sc.get("summary", "")]).strip()
            texts.append(text)
            meta = sc.copy()
            metadata.append(meta)

# ----------- Embedding and Index Creation -----------
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

# ----------- Save Artifacts -----------
np.save("embeddings.npy", embeddings)
faiss.write_index(faiss_index, "faiss_index.bin")
with open("metadata.json", "w", encoding="utf-8") as f:
    json.dump(metadata, f, ensure_ascii=False, indent=2)

print(f"Processed {len(texts)} smart chunks from {len(json_files)} files.")
