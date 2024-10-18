from src.pipeline import process_store_docs, query_gen_response

def main():
    # process and store documents within directory
    directory = "data/"
    process_store_docs(directory)

    # input user for query
    query = input("Enter your query: ")

    # query database using user's query, generate a response
    response = query_gen_response(query)

    print("Model Response: ")
    print(response)

if __name__ == "__main__":
    main()