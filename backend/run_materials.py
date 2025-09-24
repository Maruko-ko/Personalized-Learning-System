import os
from src.materials_pipeline.pdf_to_images import pdf_to_images

BASE_DIR = os.path.dirname(__file__)

PDF_PATH = os.path.join(BASE_DIR, "data", "raw", "A1_Workbook.pdf")
IMG_DIR = os.path.join(BASE_DIR, "data", "processed")

def main():
    os.makedirs(IMG_DIR, exist_ok=True)

    images = pdf_to_images(PDF_PATH, IMG_DIR)
    print("Images saved:", images)

if __name__ == "__main__":
    main()
