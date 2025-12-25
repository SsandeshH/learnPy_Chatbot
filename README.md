## A chatbot that has the knowledge of Python, and is capable to be a tutor.

The workflow is :

Python PDFs 
   =>
Text Extraction (PDF Loader)
   =>
Preprocessing
   =>
Chunking
   =>
Embedding Model
   =>
Vector Database (Chroma / FAISS)
   =>
Retriever
   =>
Gemma:2B (via Ollama)
   =>
Chat Interface (CLI / Flask / Web UI)
