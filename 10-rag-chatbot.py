import os
import streamlit as st
from dotenv import load_dotenv
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.llms.google_genai import GoogleGenAI

load_dotenv()

Settings.llm = GoogleGenAI(model="gemini-2.5-flash")
Settings.embed_model = GoogleGenAIEmbedding(model_name="models/gemini-embedding-004")

@st.cache_resource
def build_query_engine():
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    return index.as_query_engine()


def main():
    st.title("Babson Handbook Chatbot")

    query_engine = build_query_engine()

    user_input = st.chat_input("Ask a question about the Babson student handbook...")

    if user_input:
        with st.spinner("Thinking..."):
            response = query_engine.query(user_input)
        st.write("**Answer:**")
        st.write(str(response))
