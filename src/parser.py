import pdfplumber

def extract_text_from_pdf(pdf_path):
    """Extract all text content from a PDF resume."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


if __name__ == "__main__":
    # Quick test - run this file directly to check parsing works
    sample_text = extract_text_from_pdf("sample_resume.pdf")
    print(sample_text[:500])  # print first 500 characters to check it worked