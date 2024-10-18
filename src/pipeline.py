
import os
from src.preprocess import process_doc
from src.ocr import extract_text_from_boxes
from src.model import load_embedding_model, load_gen_model, gen_embedding, generate_response
from src.milvus_db import connect_milvus, create_collection, insert_embeddings, search_milv_collection

def process_store_docs(directory):
    '''
    Process files in directory, extract, generate embeds, and store into milvus collection
    '''
    connect_milvus()
    collection = create_collection()
    embedding_model = load_embedding_model()

    document_names = []
    embeddings = []

    # Process documents and store embeddings
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath) and (filepath.lower().endswith(".pdf") or filepath.lower().endswith((".png", ".jpg", ".jpeg"))):
            # Extract text
            extracted_text = process_doc(filepath)
            embedding = gen_embedding(embedding_model, extracted_text)
            embeddings.append(embedding)
            document_names.append(filename)
    
    # insert embeddings into milvus
    insert_embeddings(collection, embeddings, document_names)

def query_gen_response(query):
    '''
    Sends a query over to Milvus, then Milvus retrieves similar docs, then generates a response
    '''
    embedding_model = load_embedding_model()
    gen_tokenizer, gen_model = load_gen_model()

    # connect to milvus db
    connect_milvus()
    collection = create_collection()

    # gen embedding for query
    query_embedding = gen_embedding(embedding_model, query)

    # retrieve docs from milvus (default to k=5)
    results = search_milv_collection(collection, query_embedding, top_k=5)

    # combined resulting retrieved docs for context
    retrieved_docs = "\n".join([f"Document: {match.entity.get('document_name')}" for res in results for match in res])

    # gen response using retrieved docs
    response = generate_response(gen_model, gen_tokenizer, query, retrieved_docs)
    return response