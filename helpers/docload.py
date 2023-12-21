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

# Import necessary libraries for PDF loading
from langchain.document_loaders import PyPDFLoader

# Load a PDF document from Andrew Ng's CS229 course
loader = PyPDFLoader("docs/cs229_lectures/MachineLearning-Lecture01.pdf")
pages = loader.load()

# Print the number of pages in the PDF
len(pages)

# Access the content and metadata of the first page
page = pages[0]
print(page.page_content[0:500])
page.metadata

# Import necessary libraries for YouTube loading
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader

# Install required packages
# ! pip install yt_dlp
# ! pip install pydub

# Define YouTube URL and save directory
url="https://www.youtube.com/watch?v=jGwO_UgTS7I"
save_dir="docs/youtube/"

# Create a generic loader for YouTube content
loader = GenericLoader(
    YoutubeAudioLoader([url], save_dir),
    OpenAIWhisperParser()
)

# Load documents from YouTube
docs = loader.load()

# Print the content of the first document
docs[0].page_content[0:500]

# Import library for loading content from web URLs
from langchain.document_loaders import WebBaseLoader

# Create a loader for a specific URL
loader = WebBaseLoader("https://github.com/basecamp/handbook/blob/master/37signals-is-you.md")

# Load documents from the URL
docs = loader.load()

# Print the content of the first document
print(docs[0].page_content[:500])

# Import Notion directory loader
from langchain.document_loaders import NotionDirectoryLoader

# Create a loader for a Notion directory
loader = NotionDirectoryLoader("docs/Notion_DB")

# Load documents from the Notion directory
docs = loader.load()

# Print the content and metadata of the first document
print(docs[0].page_content[0:200])
docs[0].metadata
