import json
import glob
import os
import numpy as np
import faiss
import torch
from transformers import DPRQuestionEncoder, DPRQuestionEncoderTokenizer
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../KG')))
from all_law_KG import build_law_kg, get_all_law_triplets
triplets = get_all_law_triplets()
KG = build_law_kg(triplets)

question_encoder = DPRQuestionEncoder.from_pretrained("facebook/dpr-question_encoder-single-nq-base")
question_tokenizer = DPRQuestionEncoderTokenizer.from_pretrained("facebook/dpr-question_encoder-single-nq-base")

llm_model = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

with open("../Chunking/metadata.json") as f:
    metadata = json.load(f)
embeddings = np.load("../Chunking/embeddings.npy")
faiss_index = faiss.read_index("../Chunking/faiss_index.bin")

document_folder = "../Documents/"
json_files = glob.glob(os.path.join(document_folder, "*.json"))
texts = []
for file_path in json_files:
    with open(file_path, "r", encoding="utf-8") as q:
        data = json.load(q)
        texts.extend([
            " ".join([
                chunk.get("title", ""),
                chunk.get("content", ""),
                chunk.get("summary", "")
            ]).strip()
            for chunk in data.get("chunks", [])
        ])

def retrieve_chunks(query, faiss_index, question_encoder, question_tokenizer, metadata, texts, k=3, threshold=18):
    inputs = question_tokenizer([query], return_tensors="pt", padding=True, truncation=True, max_length=256)
    with torch.no_grad():
        outputs = question_encoder(**inputs)
        query_vec = outputs.pooler_output.cpu().numpy()
    D, I = faiss_index.search(query_vec, k)
    if all(d < threshold for d in D[0]):
        return None
    results = []
    for idx in I[0]:
        idx = int(idx)
        results.append({
            "id": metadata[idx]["id"],
            "type": metadata[idx]["type"],
            "content": texts[idx]
        })
    return results

def enhance_with_kg(query, retrieved_chunks, KG, top_n=3):
    enhanced_facts = []
    for chunk in retrieved_chunks or []:
        chunk_id = chunk.get("id")
        if chunk_id in KG:
            for target in KG.successors(chunk_id):
                relation = KG[chunk_id][target]["relation"]
                enhanced_facts.append((chunk_id, relation, target))
                if relation == "has_faq":
                    for t in KG.successors(target):
                        r = KG[target][t]["relation"]
                        if r.startswith("has_"):
                            enhanced_facts.append((target, r, t))
    keyword = query.lower()
    result = [fact for fact in enhanced_facts if keyword in str(fact).lower()]
    return result[:top_n] if result else enhanced_facts[:top_n]

def format_answer_with_llm(query, retrieved_chunks, llm_model):
    if not retrieved_chunks:
        return "I do not know the answer to that question."
    context = "\n\n".join([f"{r['type'].title()} [{r['id']}]: {r['content']}" for r in retrieved_chunks])
    prompt = (
        "You are a legal assistant. ONLY use the information in the context below to answer the user's question. "
        "If the context does not help, reply exactly: 'I do not know the answer to that question.'\n\n"
        f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    )
    response = llm_model.invoke(prompt)
    return response.content

def rewrite_query_with_llm(query_history, llm_model, history_turns=3):
    context = "\n".join(query_history[-history_turns:])
    prompt = (
        "Given the conversation below, rewrite the latest legal query to be precise and information-rich for retrieval.\n"
        f"Conversation so far:\n{context}\nRewritten Query:"
    )
    response = llm_model.invoke(prompt)
    return response.content.strip()

def expand_query_with_llm(query, llm_model):
    prompts = [
        f"Rephrase for document retrieval: {query}",
        f"Expand with synonyms or related legal terms: {query}",
        f"Write the query as a legal expert would: {query}"
    ]
    expanded_queries = [llm_model.invoke(p).content.strip() for p in prompts]
    return expanded_queries

query_history = []

while True:
    user_query = input("Your legal question: ")
    if user_query.lower() in {"exit", "quit"}:
        break

    query_history.append(user_query)

    enhanced_query = rewrite_query_with_llm(query_history, llm_model)

    expanded_queries = expand_query_with_llm(enhanced_query, llm_model)
    all_queries = [enhanced_query] + expanded_queries

    all_retrieved = []
    for q in all_queries:
        retrieved = retrieve_chunks(q, faiss_index, question_encoder, question_tokenizer, metadata, texts, k=3)
        if retrieved:
            all_retrieved.extend(retrieved)
    seen = set()
    distinct_retrieved = []
    for r in all_retrieved:
        if r["id"] not in seen:
            distinct_retrieved.append(r)
            seen.add(r["id"])

    enhanced_facts = enhance_with_kg(enhanced_query, distinct_retrieved, KG, top_n=3)

    final_answer = format_answer_with_llm(user_query, distinct_retrieved, llm_model)
    print("\nAnswer:\n" + final_answer)
    print("\n[Query Log] Original:", user_query)
    print("[Query Log] Enhanced:", enhanced_query)
    print("[Query Log] Expanded:", expanded_queries)
