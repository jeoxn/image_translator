from PIL import Image
import pytesseract
from googletrans import Translator

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image_path = 'image.png'
image = Image.open(image_path)

extracted_text = pytesseract.image_to_string(image)

translator = Translator()
translated_text = translator.translate(extracted_text, dest='id')

print(translated_text.text)