# CogniDoc Chatbot @Devspace
# ChatWithYourData Bot

## Overview
ChatWithYourData_Bot is a conversational chatbot that leverages a retrieval-augmented generation (RAG) approach. It uses a combination of document loading, splitting, storage, retrieval, and a conversational interface powered by OpenAI models. The goal is to enable users to have interactive conversations with their data, retrieving relevant information from loaded documents.

## Setup

### Prerequisites
- Python 3.x
- pip (Python package installer)
- An OpenAI API key

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/ChatWithYourData_Bot.git
   cd ChatWithYourData_Bot
   
2. Install the required Python packages
   ```
   pip install -r requirements.txt
   ```
   
3. Set up your OpenAI API key by creating a '.env' file in the project root directory with the following content:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage 
### Run the Flask App
1. Run the Flask app to serve the Panel app:
   ```
   python app.py
   ```

2. Open your web browser and go to http://localhost:5000/ to interact with the chatbot.

## Dashboard Features 

* Conversation Tab: Enter text in the input box to interact with the chatbot. The conversation history is displayed with user and chatbot responses.

* Database Tab: Load a PDF file into the database using the "Load DB" button. The last database query, generated question, and source documents are displayed.

* Chat History Tab: View the chat history, including user inputs and chatbot responses.

* Configure Tab: Load a PDF file, clear chat history, or clear the chatbot panel.

## How It Works
1. Document Loading: PDF documents are loaded into the system using the PyPDFLoader.

2. Splitting: Documents are split into chunks for efficient processing.

3. Storage: Documents are stored in a vector database (Chroma) with OpenAI embeddings.

4. Retrieval: The system retrieves relevant documents based on user queries.

5. Conversational Interface: Users interact with the chatbot through a web interface powered by Flask, Panel, and Bokeh.

## Customization 
* OpenAI Model: Change the OpenAI model version in the 'app.py' file if needed.
* Database Load: Upload different PDF files by using the "Load DB" button in the "Configure" tab.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Note: Please replace `"your_api_key_here"` in the `.env` file with your actual OpenAI API key. Additionally, customize the GitHub repository URL and other details based on your project.
