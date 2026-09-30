# Company Document RAG Assistant

A Retrieval-Augmented Generation (RAG) application that allows users to ask questions about company documents and receive context-aware answers using **Google Gemini, FAISS, and Streamlit**.

The project demonstrates an end-to-end RAG workflow including PDF processing, text chunking, embeddings, vector storage, semantic retrieval, and LLM-based question answering.

## Project Overview

Company Document RAG Assistant is designed to retrieve relevant information from company PDF documents before generating an answer.

Instead of relying only on the general knowledge of an LLM, the application searches the uploaded company documents for relevant content and provides that retrieved context to the language model.

## RAG Architecture

```text
Company PDF Documents
        ↓
PDF Text Extraction
        ↓
Text Chunking
        ↓
Embedding Generation
        ↓
FAISS Vector Store
        ↓
User Question
        ↓
Query Embedding
        ↓
Similarity Search
        ↓
Relevant Chunks
        ↓
Gemini LLM
        ↓
Generated Answer
        ↓
Streamlit Interface
```

## Features

- PDF document processing
- Text extraction from company documents
- Text chunking with overlap
- Gemini embedding generation
- FAISS vector similarity search
- Retrieval of relevant document chunks
- LLM-based answer generation
- Source and page information for retrieved chunks
- Streamlit web interface
- Secure API-key management using environment variables

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google Gen AI SDK
- FAISS
- NumPy
- PyPDF
- python-dotenv

## Project Structure

```text
company-rag/
│
├── documents/
│   ├── Company-policies.pdf
│   └── Employee Handbook.pdf
│
├── app.py
├── chunker.py
├── llm.py
├── pdf_processor.py
├── vector_store.py
│
├── test_chunks.py
├── test_embedding.py
├── test_pdf.py
├── test_processor.py
├── test_rag.py
├── test_search.py
├── test_vector_store.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

Generated FAISS/vector-store files and the local virtual environment are excluded from GitHub.

## How the RAG Pipeline Works

### 1. PDF Processing

The application reads the company PDF documents and extracts their text along with document and page information.

### 2. Text Chunking

Extracted text is divided into smaller chunks so that relevant sections can be efficiently retrieved.

Chunk overlap helps preserve context between neighboring sections.

### 3. Embedding Generation

Each text chunk is converted into a numerical embedding using an embedding model.

The embeddings represent the semantic meaning of the text.

### 4. FAISS Vector Store

The document embeddings are stored in a FAISS vector index for efficient similarity search.

### 5. Query Processing

When a user asks a question, the question is also converted into an embedding.

### 6. Similarity Search

FAISS compares the question embedding with the stored document embeddings and retrieves the most relevant chunks.

### 7. LLM Answer Generation

The retrieved document context and the user's question are provided to Google Gemini.

Gemini generates an answer based on the retrieved context.

### 8. Source Information

The application displays retrieved document information such as the source document, page number, and FAISS distance to help users understand where the retrieved context came from.

## Installation

Clone the repository:

```bash
git clone https://github.com/rprasad753-dot/company-document-rag-assistant.git
```

Navigate into the project:

```bash
cd company-document-rag-assistant
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file in the root directory:

```text
GEMINI_API_KEY=your_api_key_here
```

The real `.env` file should never be committed to GitHub.

## Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Then open the local Streamlit URL displayed in the terminal.

## Example Questions

Depending on the contents of the company documents, users can ask questions such as:

- What is the company's leave policy?
- When is a medical certificate required?
- What are the employee responsibilities?
- What actions are prohibited under company policy?

The assistant retrieves relevant document sections before generating its answer.

## What I Learned

This project provided hands-on experience with:

- Retrieval-Augmented Generation (RAG)
- PDF text extraction
- Document chunking
- Embedding generation
- Vector databases and similarity search
- FAISS
- Semantic retrieval
- LLM integration
- Streamlit application development
- Source-aware document question answering
- Secure API-key management

## Security

API keys are stored locally using environment variables.

The following files/directories are excluded from version control:

```text
.env
venv/
__pycache__/
faiss_index/
vectorstore/
```

## Author

**Rahul Prasad**