import pytesseract
from PIL import Image
import os

img_dir = "../../data/processed"
output_dir = "../../data/text"
output_file = os.path.join(output_dir, "ocr_result.txt")

def ocr_images(img_dir, output_file):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    full_text = ""
    for file in sorted(os.listdir(img_dir)):
        if file.endswith(".png"):
            img_path = os.path.join(img_dir, file)
            text = pytesseract.image_to_string(Image.open(img_path), lang="eng")
            full_text += f"\n--- {file} ---\n{text}\n"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(full_text)

    return output_file

if __name__ == "__main__":
    result_file = ocr_images(img_dir, output_file)
    print(f"Save at: {result_file}")
