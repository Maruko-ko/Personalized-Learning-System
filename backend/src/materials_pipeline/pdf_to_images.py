from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    pages = convert_from_path(pdf_path, dpi=300)

    image_paths = [] 
    for i, page in enumerate(pages):
        image_path = os.path.join(output_dir, f"page_{i+1}.png")
        page.save(image_path, "PNG")
        image_paths.append(image_path) 

    return image_paths
