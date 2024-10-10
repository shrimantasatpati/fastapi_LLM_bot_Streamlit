from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
import os
from dotenv import load_dotenv

load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")
#seeting environment variable for using throughout the execution/project
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
os.environ["HF_API_TOKEN"] = HF_TOKEN
    
print("Import Successfully")

def pinecone_config():
    #configuring pinecone database
    document_store = PineconeDocumentStore(
            # environment="aws-starter",
            index="default",
            namespace="default",
            dimension=768
        )
    return document_store