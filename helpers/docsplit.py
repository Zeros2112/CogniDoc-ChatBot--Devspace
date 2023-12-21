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

# Import text splitting modules
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter, TokenTextSplitter, MarkdownHeaderTextSplitter

# Define chunk size and overlap
chunk_size = 26
chunk_overlap = 4

# Create text splitters
r_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
c_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

# Example strings for testing text splitting
text1 = 'abcdefghijklmnopqrstuvwxyz'
text2 = 'abcdefghijklmnopqrstuvwxyzabcdefg'
text3 = "a b c d e f g h i j k l m n o p q r s t u v w x y z"

# Test text splitting with RecursiveCharacterTextSplitter
r_splitter.split_text(text1)
r_splitter.split_text(text2)
r_splitter.split_text(text3)

# Create a CharacterTextSplitter with a custom separator
c_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap, separator=' ')
c_splitter.split_text(text3)

# Create text splitter for token-based splitting
text_splitter = TokenTextSplitter(chunk_size=1, chunk_overlap=0)
text_splitter.split_text(text1)

# Load a PDF document and split it using token-based splitting
from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader("docs/cs229_lectures/MachineLearning-Lecture01.pdf")
pages = loader.load()
text_splitter.split_documents(pages)

# Load documents from a Notion directory and split them using token-based splitting
from langchain.document_loaders import NotionDirectoryLoader
loader = NotionDirectoryLoader("docs/Notion_DB")
notion_db = loader.load()
text_splitter.split_documents(notion_db)

# Define a Markdown document and split it based on header metadata
markdown_document = """# Title\n\n \
## Chapter 1\n\n \
Hi this is Jim\n\n Hi this is Joe\n\n \
### Section \n\n \
Hi this is Lance \n\n 
## Chapter 2\n\n \
Hi this is Molly"""

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
md_header_splits = markdown_splitter.split_text(markdown_document)
