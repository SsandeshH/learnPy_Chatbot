from text_extractor import text_extraction
from preprocessing import clean_text
from chunk_text import chunk_documents
from embeddings import get_embedding_model


docs = text_extraction()
for each_doc in docs:
    each_doc.page_content = clean_text(each_doc.page_content)
    each_doc.page_content = each_doc.page_content.replace("\t", "    ")

chunks = chunk_documents(docs, 650, 100)

embeddings = get_embedding_model()

# test_vector = embeddings.embed_query("What is a Python list?")
# print(len(test_vector))





