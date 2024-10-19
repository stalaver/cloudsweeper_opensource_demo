from pymilvus import Collection, connections, FieldSchema, CollectionSchema, DataType
import numpy as np

# Connecting to Milvus
def connect_milvus():
    connections.connect(host='localhost', port='19530')

def create_collection(collection_name="document_vectors"):
    '''
    Creates a collection through Milvus so that we can store document vectors
    Embedding Dimension based on all-MiniLM-L6-v2
    '''
    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True),
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=384),
        FieldSchema(name="document_name", dtype=DataType.VARCHAR, max_length=255)
    ]
    
    schema = CollectionSchema(fields=fields, description="Document vector collection")
    collection = Collection(name=collection_name, schema=schema)
    collection.create_index(field_name="embedding", index_params={"metric_type": "L2"})
    return collection

def insert_embeddings(collection, embeddings, document_names):
    '''
    Insert doc embeddings into Milvus
    '''
    ids = np.arange(len(embeddings))
    entities = [ids, embeddings, document_names]
    collection.insert(entities)

def load_collection(collection):
    '''
    load collection into memory for search
    '''
    collection.load()

def search_milv_collection(collection, query_embedding, top_k=5):
    '''
    Search Milvus for top k (eg. k=5) most similar docs
    '''
    load_collection(collection)

    search_params = {'metric_type': "L2", "params": {"nprobe": 10}}
    results = collection.search(
        data=[query_embedding],
        anns_field="embedding",
        param=search_params,
        limit=top_k,
        output_fields=["document_name"]
    )
    return results