import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the NASA API key
NASA_API_KEY = os.getenv('NASA_API_KEY')
# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
