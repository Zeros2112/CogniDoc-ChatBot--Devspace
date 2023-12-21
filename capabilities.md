# ChatWithYourData_Bot Capabilities

ChatWithYourData_Bot is a conversational chatbot designed to interact with loaded documents, answer user queries, and provide information from the stored data. Below are the key capabilities of the chatbot:

## 1. Document Loading and Splitting

The chatbot can load PDF documents using the PyPDFLoader and split them into manageable chunks for efficient processing. This ensures that large documents are processed effectively.

## 2. Vector Database Storage

Documents are stored in a vector database using the Chroma vector store. The OpenAI embeddings are utilized to create vectors for each document, enabling similarity search based on user queries.

## 3. Retrieval Augmented Generation (RAG)

The chatbot employs a Retrieval Augmented Generation (RAG) approach. It retrieves relevant documents from the database based on user queries and generates responses using the OpenAI language model (LLM).

## 4. Conversational Interface

Users can interact with the chatbot through a user-friendly web interface powered by Flask, Panel, and Bokeh. The conversational history is displayed, allowing users to have dynamic and iterative conversations with the chatbot.

## 5. Document Load and Query

- Users can load PDF documents into the database using the "Load DB" button.
- The last database query, generated question, and source documents are displayed in the "Database" tab.
  
## 6. Chat History

- Users can view the chat history, including user inputs and chatbot responses, in the "Chat History" tab.
- The chat history can be cleared using the "Clear History" button.

## 7. Conversation with Data

- Users can enter text in the input box in the "Conversation" tab to interact with the chatbot.
- The chatbot responds to user queries, retrieves relevant information from the loaded documents, and displays the conversation history.

## 8. Customization

- The OpenAI model version can be customized by changing the model name in the `app.py` file.
- Users can load different PDF files into the database for varied interactions.

## 9. Contribution

- The project is open to contributions. Developers can follow the standard GitHub fork and pull request workflow to contribute.

## 10. License

- The project is licensed under the MIT License.

Explore the capabilities of ChatWithYourData_Bot by running the Flask app and interacting with the provided functionalities.

**Note:** Ensure that you have the necessary prerequisites and have set up the OpenAI API key before running the application.
