import os
import json
import numpy as np
import faiss

from dotenv import load_dotenv
from google import genai
from google.genai import types


# ============================================================
# 1. Load environment variables
# ============================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")


# ============================================================
# 2. Create Gemini client
# ============================================================

client = genai.Client(api_key=api_key)


# Gemini embedding model
MODEL_NAME = "gemini-embedding-001"


# ============================================================
# 3. Create embedding
# ============================================================

def create_embedding(text):
    """
    Create an embedding for a document chunk.
    """

    result = client.models.embed_content(
        model=MODEL_NAME,
        contents=text,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT"
        )
    )

    return result.embeddings[0].values


# ============================================================
# 4. Create FAISS vector store
# ============================================================

def create_vector_store(chunks):
    """
    Convert document chunks into embeddings
    and save them in FAISS.
    """

    embeddings = []

    print(f"Creating embeddings for {len(chunks)} chunks...")

    for i, chunk in enumerate(chunks, start=1):

        print(f"Embedding {i}/{len(chunks)}")

        embedding = create_embedding(
            chunk["text"]
        )

        embeddings.append(embedding)

    print("\nAll embeddings created.")

    # Convert embeddings to NumPy array
    embeddings_array = np.array(
        embeddings,
        dtype="float32"
    )

    # Get embedding dimension
    dimension = embeddings_array.shape[1]

    print(f"Embedding dimension: {dimension}")

    # Create FAISS index
    index = faiss.IndexFlatL2(dimension)

    # Add embeddings
    index.add(embeddings_array)

    # Create folder
    os.makedirs(
        "faiss_index",
        exist_ok=True
    )

    # Save FAISS index
    faiss.write_index(
        index,
        "faiss_index/index.faiss"
    )

    # Save original chunks and metadata
    with open(
        "faiss_index/chunks.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            chunks,
            f,
            ensure_ascii=False,
            indent=2
        )

    print("\nFAISS index saved successfully.")
    print(f"Vectors stored: {index.ntotal}")


# ============================================================
# 5. Search FAISS
# ============================================================

def search_vector_store(question, top_k=3):
    """
    Search FAISS for chunks relevant to a question.
    """

    # Load FAISS index
    index = faiss.read_index(
        "faiss_index/index.faiss"
    )

    # Load chunks
    with open(
        "faiss_index/chunks.json",
        "r",
        encoding="utf-8"
    ) as f:

        chunks = json.load(f)

    # Create embedding for the question
    result = client.models.embed_content(
        model=MODEL_NAME,
        contents=question,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY"
        )
    )

    query_embedding = np.array(
        [result.embeddings[0].values],
        dtype="float32"
    )

    # Search FAISS
    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for distance, index_number in zip(
        distances[0],
        indices[0]
    ):

        # Ignore invalid index
        if index_number == -1:
            continue

        results.append({
            "text": chunks[index_number]["text"],
            "source": chunks[index_number]["source"],
            "page": chunks[index_number]["page"],
            "distance": float(distance)
        })

    return results