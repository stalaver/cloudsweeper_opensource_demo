# pre process using OpenCV
from pdf2image import convert_from_path
import pytesseract
import cv2

def process_doc(file_path):
    '''
    Process PDF or image and use Tesseract OCR to extract text
    '''

    extracted_txt = ""

    if file_path.lower().endswith(".pdf"):
        # convert PDF pages to images
        images = convert_from_path(file_path)
        for image in images:
            text = pytesseract.image_to_string(image)
            extracted_txt += text + "\n"
    
    else:
        # read and extract text directly from image
        image = cv2.imread(file_path)
        text = pytesseract.image_to_string(image)
        extracted_txt += text + "\n"
    
    return extracted_txt