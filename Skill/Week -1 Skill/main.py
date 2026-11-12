
import os
from dotenv import load_dotenv
from google import genai

# Step 1: Load environment variables
load_dotenv()

# Step 2: Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found!")

# Step 3: Initialize Gemini client
client = genai.Client(api_key=api_key)

# Step 4: Send prompt to Gemini
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is Artificial Intelligence? "
)

# Step 5: Display response
print("\nGemini Response:")
print(response.text)
