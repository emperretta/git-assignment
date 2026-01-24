from dotenv import load_dotenv
from google import genai
import os
import re
load_dotenv()
client = genai.Clien(api_key=os.environ.get("GEMINI_API_KEY"))