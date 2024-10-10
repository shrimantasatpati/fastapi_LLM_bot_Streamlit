from haystack import Pipeline #creating haystack pipeline
from haystack.components.writers import DocumentWriter
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
from haystack.components.converters import PyPDFToDocument
from pathlib import Path # type: ignore
import os
from dotenv import load_dotenv
from QASystem.utils import pinecone_config

#Pipeline -> the collection of the component
#Documentwriter -> Writing into database
#DocumentSplitter -> Splitting into chunks
#embedder -> creating embeddings for senetences
#pineconedocumentstore -> it is used for stoting into pinecone vector database
#pathlib -> Library for getting relative system path

def ingest(document_store):
        #configuring pinecone database
        '''document_store = PineconeDocumentStore(
            environment="gcp-starter",
            index="default",
            namespace="default",
            dimension=768
        )
        '''
        # In Haystack, we get pipeline
        # In Langchain, we have chain
        indexing = Pipeline()

        #adding the components in pipeline
        indexing.add_component("converter", PyPDFToDocument())
        indexing.add_component("splitter", DocumentSplitter(split_by="sentence", split_length=2))
        indexing.add_component("embedder", SentenceTransformersDocumentEmbedder())
        indexing.add_component("writer", DocumentWriter(document_store))

        #coneecting all the components of pipeline
        indexing.connect("converter", "splitter")
        indexing.connect("splitter", "embedder")
        indexing.connect("embedder", "writer")

        #stroing the data as a embedding in the database
        indexing.run({"converter": {"sources": [Path("D:\\fastapi_LLM_bot\\data\\Retrieval-Augmented-Generation-for-NLP.pdf")]}})

if __name__ == "__main__":
    #if running this module individually
    # ingest()
	#loading the environment variable
    '''load_dotenv()
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
    
    print("Import Successfully")'''
    document_store=pinecone_config()
    # The pinecone configuration is the document store
    
    ingest(document_store)