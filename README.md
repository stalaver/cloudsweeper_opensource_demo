## Open Source Demo RAG LLM
To use, install the required frameworks needed as listed in the requirements.txt file. Additionally you will need to install Docker to host the Milvus Container. To run the program, run main.py after set up and you will be asked for a prompt to the model. There are currently only a few documents for testing in the data folder, and the results folder carries the converted images of said documents. The model will scan through data as its directory.

### Models Used
For the embedding model, using a SentenceTransformer "all-MiniLM-L6-v2". For the generative model, using Facebook's OPT "facebook/opt-1.3b".

### Frameworks used:
Currently using Tesseract for the OCR, OpenCV for image processing, pdf2image to convert PDFs into images for processing, Docker to host Milvus Vector Database, and Milvus as the Vector Database.

### Current Issue:
So far, results are good and the first item that is returned from the query has been correct. However, there are instances where multiple items afterwards are returned from the directory that would not be considered correct for the query.