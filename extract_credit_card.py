import pytesseract
from PIL import Image
import re

# Load the image
image_path = "data/credit_card.png"
image = Image.open(image_path)

# Extract text using OCR
extracted_text = pytesseract.image_to_string(image)

# Find a valid credit card number (typically 13 to 19 digits)
card_number_match = re.search(r'\d{13,19}', extracted_text)

if card_number_match:
    card_number = card_number_match.group(0)
    print("Extracted Credit Card Number:", card_number)

    # Save to file
    with open("data/credit-card.txt", "w") as file:
        file.write(card_number)
else:
    print("No valid credit card number found.")
