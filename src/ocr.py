import pytesseract

def extract_text_from_boxes(image):
    '''
    OCR finds bounding boxes from image and extracts text using tesseract
    '''

    # Extract text within bounding boxes
    ocr_data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

    texts = []
    boxes = []

    for i in range(len(ocr_data['text'])):
        # Filter out low confidence extracted texts
        if int(ocr_data['conf'][i] > 60):
            texts.append(ocr_data['text'][i])
            (x, y, w, h) = (ocr_data['left'][i], ocr_data['top'][i], ocr_data['width'][i], ocr_data['height'][i])
            boxes.append((x, y, x + w, y + h)) # (x_min, y_min, x_max, y_max)
    
    return texts, boxes