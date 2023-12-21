# Vectorstore retrieval 
import os
import openai
import sys
from dotenv import load_dotenv, find_dotenv
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.chains.query_constructor.base import AttributeInfo
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.retrievers import SVMRetriever, TFIDFRetriever
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load environment variables from a local .env file
_ = load_dotenv(find_dotenv())

# Set up OpenAI API key
openai.api_key = os.environ['OPENAI_API_KEY']

# Install required packages
# !pip install lark

# Create OpenAIEmbeddings instance
embedding = OpenAIEmbeddings()

# Create Chroma vector store
persist_directory = 'docs/chroma/'
vectordb = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding
)

# Print the number of documents in the Chroma vector store
print(vectordb._collection.count())

# Sample texts for similarity search
texts = [
    "The Amanita phalloides has a large and imposing epigeous (aboveground) fruiting body (basidiocarp).",
    "A mushroom with a large fruiting body is the Amanita phalloides. Some varieties are all-white.",
    "A. phalloides, a.k.a Death Cap, is one of the most poisonous of all known mushrooms.",
]

# Create a small Chroma vector store from texts
smalldb = Chroma.from_texts(texts, embedding=embedding)

# Sample question for similarity search
question = "Tell me about all-white mushrooms with large fruiting bodies"

# Perform similarity search
smalldb.similarity_search(question, k=2)

# Perform maximum marginal relevance search
smalldb.max_marginal_relevance_search(question, k=2, fetch_k=3)

# Sample question for similarity search
question = "what did they say about matlab?"

# Perform similarity search with Chroma vector store
docs_ss = vectordb.similarity_search(question, k=3)
docs_ss[0].page_content[:100]
docs_ss[1].page_content[:100]

# Perform maximum marginal relevance search with Chroma vector store
docs_mmr = vectordb.max_marginal_relevance_search(question, k=3)
docs_mmr[0].page_content[:100]
docs_mmr[1].page_content[:100]

# Sample question for specificity with metadata
question = "what did they say about regression in the third lecture?"

# Perform similarity search with metadata filter
docs = vectordb.similarity_search(
    question,
    k=3,
    filter={"source": "docs/cs229_lectures/MachineLearning-Lecture03.pdf"}
)

# Print metadata for the retrieved documents
for d in docs:
    print(d.metadata)

# Sample question for specificity with metadata using self-query retriever
metadata_field_info = [
    AttributeInfo(
        name="source",
        description="The lecture the chunk is from, should be one of `docs/cs229_lectures/MachineLearning-Lecture01.pdf`, `docs/cs229_lectures/MachineLearning-Lecture02.pdf`, or `docs/cs229_lectures/MachineLearning-Lecture03.pdf`",
        type="string",
    ),
    AttributeInfo(
        name="page",
        description="The page from the lecture",
        type="integer",
    ),
]

document_content_description = "Lecture notes"
llm = OpenAI(model='gpt-3.5-turbo-instruct', temperature=0)
retriever = SelfQueryRetriever.from_llm(
    llm,
    vectordb,
    document_content_description,
    metadata_field_info,
    verbose=True
)

# Retrieve relevant documents using self-query retriever
docs = retriever.get_relevant_documents(question)

# Print metadata for the retrieved documents
for d in docs:
    print(d.metadata)

# Sample question for contextual compression retrieval
compression_retriever = ContextualCompressionRetriever(
    base_retriever=vectordb.as_retriever()
)

# Retrieve relevant documents using contextual compression retriever
compressed_docs = compression_retriever.get_relevant_documents(question)


# Sample question for combining various retrieval techniques
compression_retriever = ContextualCompressionRetriever(
    base_retriever=vectordb.as_retriever(search_type="mmr")
)

# Retrieve relevant documents using combined techniques
compressed_docs = compression_retriever.get_relevant_documents(question)


# Sample question for other types of retrieval
# Load PDF document and split
loader = PyPDFLoader("docs/cs229_lectures/MachineLearning-Lecture01.pdf")
pages = loader.load()
all_page_text = [p.page_content for p in pages]
joined_page_text = " ".join(all_page_text)

# Split the text
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=150)
splits = text_splitter.split_text(joined_page_text)

# Create SVM and TFIDF retrievers
svm_retriever = SVMRetriever.from_texts(splits, embedding)
tfidf_retriever = TFIDFRetriever.from_texts(splits)

# Sample question for SVM retriever
question = "What are major topics for this class?"
docs_svm = svm_retriever.get_relevant_documents(question)
docs_svm[0]

# Sample question for TFIDF retriever
question = "what did they say about matlab?"
docs_tfidf = tfidf_retriever.get_relevant_documents(question)
docs_tfidf[0]
