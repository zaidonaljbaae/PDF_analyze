
import fitz  # PyMuPDF
import PIL.Image  # pillow
import io
import re
from pdfminer.high_level import extract_text

# Extract all text from the PDF
pdf_path = "test.pdf"
text = extract_text(pdf_path)
print("Extracted Text:")
print(text)

# Find specific text pattern in the extracted text
mytext = re.compile(r"[a-zA-Z]+,{1}\s{1}")
matches = mytext.findall(text)
print("\nFound Matches:")
print(matches)

# Extract images from the PDF
pdf = fitz.open(pdf_path)
counter = 1
for i in range(len(pdf)):
    page = pdf[i]
    images = page.get_images(full=True)  # Get all images on the page
    for image in images:
        base_img = pdf.extract_image(image[0])
        image_data = base_img["image"]
        img = PIL.Image.open(io.BytesIO(image_data))
        extension = base_img["ext"]
        img_path = f"image{counter}.{extension}"
        img.save(open(img_path, "wb"))
        print(f"Saved image {counter} as {img_path}")
        counter += 1

