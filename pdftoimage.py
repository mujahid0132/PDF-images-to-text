import io
import os
import subprocess

package_names = ["PyPDF2", "pytesseract"]
for package in package_names:
    try:
        subprocess.check_call(["pip", "install", package])
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}")

from PyPDF2 import PdfReader
from PIL import Image
import pytesseract
    
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

reader = PdfReader(input("Enter path to manual: "))

for page_index in range(len(reader.pages)):
    page = reader.pages[page_index]
    for image_file_object in page.images:
        image = Image.open(io.BytesIO(image_file_object.data))
        try:
            text = pytesseract.image_to_string(image)
            if(text.strip() != ""):
                with open(f"{output_dir}/{str(page_index)}.txt", "w") as fp:
                    fp.write(text)
        except pytesseract.TesseractNotFoundError as e:
            print(e)
            break
# print("All text files are created in output folder")
