# here is the source: https://docs.llamaindex.ai/en/latest/examples/customization/prompts/chat_prompts/#1-explicitly-define-chatmessage-and-messagerole-objects

import os
from dotenv import load_dotenv
import streamlit as st
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.readers.file import FlatReader
from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core import ChatPromptTemplate

# Load environment variables
load_dotenv()

# API key
openai_api_key = os.getenv('OPENAI_API_KEY')

# Set up the OpenAI LLM with the API key
llm = OpenAI(model="gpt-4o", api_key=openai_api_key)

# using FlatReader for reading text files
file_extractor = {".txt": FlatReader()}

# load documents from this directory
reader = SimpleDirectoryReader("./data", file_extractor=file_extractor)
documents = reader.load_data()

# vector Store Index
vector_index = VectorStoreIndex.from_documents(documents)

# streamlit app 
st.set_page_config(page_title="Anna's demo Chatbot", layout="wide")
st.title("Anna's Beginner Chatbot 🌷")
st.write("Swiftie Questions only! My knowledge is limited to the lyrics of the Reputation album. :3")

# conversation history
if 'responses' not in st.session_state:
    st.session_state['responses'] = []
if 'questions' not in st.session_state:
    st.session_state['questions'] = []

# display conversation history
for response in st.session_state['responses']:
    with st.chat_message("user"):
        st.write(response['user'])
    with st.chat_message("assistant"):
        st.write(response['assistant'])

# user 
user_input = st.chat_input("Ask something!")

if user_input:
    query_str = str(user_input)

    # text QA Prompt Template
    chat_text_qa_msgs = [
        ChatMessage(
            role=MessageRole.SYSTEM,
            content="You are a helpful assistant that answers questions based on the given text data. But you can also answer questions after looking them up online."
        ),
        ChatMessage(
            role=MessageRole.USER,
            content=query_str  
        ),
    ]
    text_qa_template = ChatPromptTemplate(chat_text_qa_msgs)

    # set up the query engine 
    query_engine = vector_index.as_query_engine(
        text_qa_template=text_qa_template,
        llm=llm
    )

    # execute the query and extract the response text
    response = query_engine.query(query_str)
    response_text = response.response  

    # display the response in the chat
    st.session_state['responses'].append({"user": query_str, "assistant": response_text})
    st.rerun()
