
# pip install chromadb
# pip install sentence-transformers

from pathlib import Path
import ast
from chromadb import PersistentClient
from chromadb.utils import embedding_functions

DB_PATH = Path("./.chroma")
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

client = PersistentClient(path=str(DB_PATH))
collection = client.get_or_create_collection("my_collection", embedding_function=ef)

with open("facts.txt", "r", encoding="utf-8") as f:
    facts = ast.literal_eval(f.read())

ids = [f"fact-{i}" for i in range(len(facts))]
collection.upsert(documents=facts, ids=ids)

print(f"Loaded {len(facts)} facts into {DB_PATH}")
