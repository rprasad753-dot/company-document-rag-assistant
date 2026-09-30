from vector_store import search_vector_store


question = "What are the company rules and regulations?"


results = search_vector_store(
    question,
    top_k=3
)


print("\n" + "=" * 60)
print("SEARCH RESULTS")
print("=" * 60)


for i, result in enumerate(results, start=1):

    print(f"\nRESULT {i}")

    print(f"Source: {result['source']}")
    print(f"Page: {result['page']}")
    print(f"Distance: {result['distance']:.4f}")

    print("\nText:")
    print(result["text"][:500])