AI in Finance – Loan Processing & Compliance Assistance
Overview
This project integrates AI-driven financial solutions to improve risk assessment, automate KYC/AML verification, and provide an AI chatbot for financial education and compliance assistance. It includes:
OCR Module: Extracts text from scanned documents (e.g., ID cards) for KYC processing.
Risk Assessment Model: Uses machine learning (Random Forest) to predict loan defaults.
AI Compliance Chatbot: Educates users on loan eligibility and answers compliance-related queries.

Features
✔ Automated OCR Processing – Extracts details like Name, DOB, and Address from scanned documents.
 ✔ AI-Based Risk Assessment – Predicts loan default probability using financial and behavioral data.
 ✔ Compliance Chatbot – Answers queries on KYC, AML, loan eligibility, and regulations.
 ✔ Secure & Scalable – Built using Phidata, OpenAI, Tesseract OCR, and Scikit-learn.

Installation
1. Set Up Environment
pip install -r requirements.txt

2. Install Tesseract OCR (For KYC Processing)
🔗 Tesseract Installation Guide
3. Set Up API Keys (For AI Agent)
Create a .env file and store your OpenAI API Key:
OPENAI_API_KEY=your-api-key-here

Future Improvements
Enhance OCR Accuracy: Use deep learning-based text recognition.
Advanced Risk Modeling: Implement deep learning models for better default prediction.
Voice & Multi-Language AI Chatbot: Enable speech recognition and support for regional languages.
API Deployment: Convert modules into microservices for integration with financial platforms.