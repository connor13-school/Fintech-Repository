from chromadb import PersistentClient
from chromadb.utils import embedding_functions

DB_PATH = "./.chroma"
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

client = PersistentClient(path=DB_PATH)
collection = client.get_or_create_collection("my_collection", embedding_function=ef)

query = "What plants might bring the most color to a landscape?" # <---------------- CHANGE THIS

# NOTE: results are NOT a response, they are existing facts pulled from the vector database that match our query
results = collection.query(query_texts=[query], n_results=1)


print('--------------------')
print("Query:", query)
print("Response:", results["documents"][0][0])
