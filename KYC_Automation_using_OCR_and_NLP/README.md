OCR Module for KYC/AML Verification
Overview
This OCR module extracts text from scanned images and PDFs to automate the KYC (Know Your Customer) and AML (Anti-Money Laundering) verification process. It uses Tesseract OCR for text recognition and OpenCV for image preprocessing to enhance accuracy.

Features
✔ Extracts text from images (JPG, PNG, etc.)
 ✔ Converts PDFs into images and extracts text from each page
 ✔ Uses grayscale conversion and optional thresholding for better OCR accuracy
 ✔ Can be integrated into KYC/AML workflows for automated compliance

Installation
1. Install Dependencies
pip install -r requirements.txt

2. Install Tesseract OCR
Download and install Tesseract OCR:
 🔗 Tesseract OCR for Windows
 🔗 Linux/macOS: Install via package manager (sudo apt install tesseract-ocr or brew install tesseract)

Usage
Extract Text from an Image
from ocr_module import extract_text_from_image

text = extract_text_from_image("data/sample_id.jpg")
print(text)

Extract Text from a PDF
from ocr_module import extract_text_from_pdf

text = extract_text_from_pdf("data/sample_document.pdf")
print(text)

Future Improvements
Enhance Preprocessing: Adaptive thresholding and noise removal
Improve Text Accuracy: Fine-tune Tesseract OCR for better results
Add NLP Processing: Extract structured details like Name, DOB, and Address
Deploy as API: Convert the module into a microservice for real-time OCR processing
