from vector_store import search_vector_store
from llm import generate_answer


# ============================================================
# User question
# ============================================================

question = "What are the company rules and regulations?"


# ============================================================
# Step 1: Retrieve relevant chunks
# ============================================================

print("Searching company documents...")

retrieved_chunks = search_vector_store(
    question,
    top_k=3
)


print(f"Retrieved {len(retrieved_chunks)} chunks.")


# ============================================================
# Step 2: Generate answer using Gemini
# ============================================================

print("\nGenerating answer...")

result = generate_answer(
    question,
    retrieved_chunks
)


# ============================================================
# Step 3: Display answer
# ============================================================

print("\n" + "=" * 60)
print("RAG ANSWER")
print("=" * 60)

print("\nQuestion:")
print(question)

print("\nAnswer:")
print(result["answer"])


# ============================================================
# Step 4: Display sources
# ============================================================

print("\n" + "=" * 60)
print("SOURCES")
print("=" * 60)

for source in result["sources"]:

    print(
        f"- {source['source']} "
        f"(Page {source['page']})"
    )