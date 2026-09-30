from pypdf import PdfReader
from pathlib import Path


def test_pdf(pdf_path):
    print("=" * 50)
    print(f"PDF: {pdf_path.name}")

    reader = PdfReader(pdf_path)

    print(f"Pages: {len(reader.pages)}")

    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        print(f"Page {i}: {len(text)} characters")

        if text.strip():
            print(f"Preview: {text[:100].replace(chr(10), ' ')}")
        else:
            print("Preview: NO TEXT FOUND")


documents_folder = Path("documents")

pdf_files = [
    documents_folder / "Company-policies.pdf",
    documents_folder / "Employee Handbook.pdf"
]

for pdf_file in pdf_files:
    if pdf_file.exists():
        test_pdf(pdf_file)
    else:
        print("=" * 50)
        print(f"FILE NOT FOUND: {pdf_file}")