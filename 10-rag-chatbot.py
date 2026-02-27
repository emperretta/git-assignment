import os
import streamlit as st
from dotenv import load_dotenv
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.google_genai import GoogleGenAI

load_dotenv()

Settings.llm = GoogleGenAI(model="gemini-2.5-flash")
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")


def validate_config():
    """Check that required API key is present before app starts."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        st.error("GEMINI_API_KEY not found. Please check your .env file.")
        st.stop()


def validate_data_directory():
    """Check that data directory exists and contains files."""
    if not os.path.exists("data"):
        st.error("Data directory not found. Please create a 'data' folder and add your documents.")
        st.stop()
    if not os.listdir("data"):
        st.error("Data directory is empty. Please add documents to the 'data' folder.")
        st.stop()


@st.cache_resource  # Prevents re-indexing on every Streamlit rerun
def build_query_engine():
    """Load documents, build vector index, and return query engine."""
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    return index.as_query_engine()


def main():
    validate_config()          # Fail fast if API key is missing
    validate_data_directory()  # Fail fast if data folder is missing or empty
    st.title("Babson Handbook Chatbot")

    try:
        query_engine = build_query_engine()
    except Exception as e:
        st.error(f"Failed to load documents: {e}")
        st.stop()

    user_input = st.chat_input("Ask a question about the Babson student handbook...")

    if user_input:
        with st.spinner("Thinking..."):
            try:
                response = query_engine.query(user_input)
            except Exception as e:
                st.error(f"Failed to get a response: {e}")
                st.stop()
        st.write("**Answer:**")
        st.write(str(response))


if __name__ == "__main__":
    main()