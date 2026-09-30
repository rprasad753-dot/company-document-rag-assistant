from pypdf import PdfReader
from pathlib import Path


def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF.
    Each page is stored separately with document name and page number.
    """

    pdf_path = Path(pdf_path)
    reader = PdfReader(pdf_path)

    documents = []

    for page_number, page in enumerate(reader.pages, start=1):

        text = page.extract_text() or ""

        # Skip pages with no readable text
        if not text.strip():
            continue

        document = {
            "text": text,
            "source": pdf_path.name,
            "page": page_number
        }

        documents.append(document)

    return documents


def load_all_pdfs(folder_path="documents"):
    """
    Load all PDF files from the documents folder.
    """

    folder = Path(folder_path)

    all_documents = []

    for pdf_file in folder.glob("*.pdf"):

        print(f"Processing: {pdf_file.name}")

        documents = extract_text_from_pdf(pdf_file)

        print(f"  Pages with text: {len(documents)}")

        all_documents.extend(documents)

    return all_documents