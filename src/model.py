from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer

def load_embedding_model():
    '''
    Load pre-trained SentenceTransformer for generating text embeddings. Just picked a random one that was lightweight
    '''
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model

def gen_embedding(model, text):
    '''
    Generate embedding for given text
    '''
    embedding = model.encode(text, convert_to_tensor=False)
    return embedding


def load_gen_model():

    '''
    Loading a pre-trained llm. Because my computer isn't that strong I'm using facebook/opt-1.3b
    '''    
    tokenizer = AutoTokenizer.from_pretrained("facebook/opt-1.3b")
    model = AutoModelForCausalLM.from_pretrained("facebook/opt-1.3b")
    return tokenizer, model

def generate_response(model, tokenizer, query, retrieved_docs):
    '''
    After preprocessing docs, generate a response based on user query
    '''

    # Comebine query with data (documents in our case) 
    input_txt = f"Query: {query}\n\nDocuments:\n{retrieved_docs}"

    # Tokenize
    inputs = tokenizer(input_txt, return_tensors="pt")

    # Generate response
    outputs = model.generate(inputs['input_ids'], max_new_tokens=50)

    # Decode response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response