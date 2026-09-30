from pdf_processor import load_all_pdfs
from chunker import create_chunks


documents = load_all_pdfs("documents")

chunks = create_chunks(documents)

print("\n" + "=" * 50)
print(f"TOTAL PAGES: {len(documents)}")
print(f"TOTAL CHUNKS: {len(chunks)}")
print("=" * 50)

for i, chunk in enumerate(chunks[:5], start=1):

    print(f"\nCHUNK {i}")
    print(f"Source: {chunk['source']}")
    print(f"Page: {chunk['page']}")
    print(f"Characters: {len(chunk['text'])}")
    print(f"Text: {chunk['text'][:200]}")