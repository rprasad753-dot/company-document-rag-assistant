import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


# Load .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")


# Create Gemini client
client = genai.Client(api_key=api_key)


# Test text
text = "Employees must follow the company rules and regulations."


# Generate embedding
result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=text,
    config=types.EmbedContentConfig(
        task_type="RETRIEVAL_DOCUMENT"
    )
)


embedding = result.embeddings[0].values

print("Embedding successful!")
print("Embedding dimensions:", len(embedding))
print("First 5 values:", embedding[:5])