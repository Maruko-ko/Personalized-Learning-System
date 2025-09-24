import pytesseract
from PIL import Image

image_path = "../../data/processed/page_8.png"

text = pytesseract.image_to_string(Image.open(image_path), lang="eng")
print("OCR Result:\n", text)