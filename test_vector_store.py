from pdf_processor import load_all_pdfs
from chunker import create_chunks
from vector_store import create_vector_store


print("Loading PDFs...")

documents = load_all_pdfs("documents")

print("\nCreating chunks...")

chunks = create_chunks(documents)

print(f"\nTotal chunks: {len(chunks)}")

print("\nCreating vector store...")

create_vector_store(chunks)

print("\nDONE!")