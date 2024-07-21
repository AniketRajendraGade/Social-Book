import vertexai
import torch
# PROJECT_ID = "gcp-markytics-ai"  # @param {type:"string"}
# vertexai.init(project=PROJECT_ID, location="asia-south1")


# Utils
import time
from typing import List

# Langchain
import langchain
from pydantic import BaseModel

from langchain_community.document_loaders import TextLoader

# Vertex AI
from langchain.chat_models import ChatVertexAI
from langchain.embeddings import VertexAIEmbeddings
from langchain.llms import VertexAI
from langchain.schema import HumanMessage, SystemMessage
import vertexai
from langchain.document_loaders import WebBaseLoader
from langchain.vectorstores import Chroma

# # LLM model
llm = VertexAI(
    model_name="gemini-pro",
    #     max_output_tokens=512,
    temperature=0.1,
    top_p=0.8,
    top_k=40,
    verbose=True,
)

chat = ChatVertexAI()

# Embedding
EMBEDDING_QPM = 15
EMBEDDING_NUM_BATCH = 2
embeddings = VertexAIEmbeddings(
    requests_per_minute=EMBEDDING_QPM,
    num_instances_per_batch=EMBEDDING_NUM_BATCH,
)

# loader = WebBaseLoader("https://rgkarmch.org/mazi-ladki-bahin-yojana/")
# documents = loader.load()

loader = TextLoader(r"C:\Users\Administrator\Downloads\English_data90.txt")
documents = loader.load()

# split the documents into chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=0)
docs = text_splitter.split_documents(documents)
print(f"# of documents = {len(docs)}")

# select embedding engine - we use Vertex PaLM Embeddings API
embeddings

# Store docs in local vectorstore as index
# it may take a while since API is rate limited


db = Chroma.from_documents(docs, embeddings)

db = Chroma.from_documents(docs, embeddings, persist_directory="./chroma_db3")