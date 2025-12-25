import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_community.document_loaders import PyMuPDFLoader

load_dotenv()

def text_extraction():
    BASE_DIR = Path(__file__).resolve().parent.parent

    data_env = os.getenv("DATA")
    if not data_env:
        raise EnvironmentError("DATA not set in .env file")

    DATA = BASE_DIR / data_env

    if not DATA.exists():
        raise FileNotFoundError(f"PDF file not found: {DATA}")

    loader = PyMuPDFLoader(str(DATA))
    documents = loader.load()

    # print(f"Total pages loaded: {len(documents)}")
    # print("Sample text:\n", documents[0].page_content[:300])

    return documents

# text_extraction()
