#!/usr/bin/env python
# coding: utf-8

# Import necessary libraries
import os
import openai
import sys
from dotenv import load_dotenv, find_dotenv

# Load environment variables from a local .env file
_ = load_dotenv(find_dotenv())

# Set up OpenAI API key
openai.api_key = os.environ['OPENAI_API_KEY']

# Import document loaders, text splitters, embeddings, and vector stores
from langchain.document_loaders import PyPDFLoader, NotionDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# Load PDF documents using PyPDFLoader
loaders = [
    PyPDFLoader("docs/cs229_lectures/MachineLearning-Lecture01.pdf"),
    PyPDFLoader("docs/cs229_lectures/MachineLearning-Lecture01.pdf"),
    PyPDFLoader("docs/cs229_lectures/MachineLearning-Lecture02.pdf"),
    PyPDFLoader("docs/cs229_lectures/MachineLearning-Lecture03.pdf")
]
docs = []
for loader in loaders:
    docs.extend(loader.load())

# Split the documents using RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=150
)
splits = text_splitter.split_documents(docs)

# Create OpenAIEmbeddings instance
embedding = OpenAIEmbeddings()

# Example sentences for embedding testing
sentence1 = "i like dogs"
sentence2 = "i like canines"
sentence3 = "the weather is ugly outside"

# Embed the example sentences
embedding1 = embedding.embed_query(sentence1)
embedding2 = embedding.embed_query(sentence2)
embedding3 = embedding.embed_query(sentence3)

# Test similarity between embeddings
import numpy as np
np.dot(embedding1, embedding2)
np.dot(embedding1, embedding3)
np.dot(embedding2, embedding3)

# Create a Chroma vector store from documents
persist_directory = 'docs/chroma/'
vectordb = Chroma.from_documents(
    documents=splits,
    embedding=embedding,
    persist_directory=persist_directory
)

# Perform similarity search with a question
question = "is there an email I can ask for help"
docs = vectordb.similarity_search(question, k=3)

# Print the content of the retrieved documents
for doc in docs:
    print(doc.page_content)

# Save the Chroma vector store for later use
vectordb.persist()
