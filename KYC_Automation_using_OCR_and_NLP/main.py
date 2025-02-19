from src.ocr_module import extract_text_from_image, extract_text_from_pdf
from src.nlp_module import extract_fields
from src.aml_check import check_aml

def run_kyc_verification(document_path, is_pdf=False):
    print("Processing document...")

    text = extract_text_from_pdf(document_path) if is_pdf else extract_text_from_image(document_path)

    extracted_data = extract_fields(text)
    
    aml_result = check_aml(extracted_data["name"])

    return {
        "extracted_data": extracted_data,
        "aml_check": aml_result
    }

if __name__ == "__main__":
    result = run_kyc_verification("data/sample_id.jpg")
    print("KYC Verification Result:", result)
