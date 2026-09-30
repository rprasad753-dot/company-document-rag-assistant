from pdf_processor import load_all_pdfs


documents = load_all_pdfs("documents")

print("\n" + "=" * 50)
print(f"TOTAL PAGES LOADED: {len(documents)}")
print("=" * 50)

for doc in documents[:5]:
    print(f"\nSource: {doc['source']}")
    print(f"Page: {doc['page']}")
    print(f"Characters: {len(doc['text'])}")
    print(f"Preview: {doc['text'][:150].replace(chr(10), ' ')}")