import pdfplumber
import json

# PDF file path for Nexus
pdf_path = "/Users/gonzalovillarino/Documents/Swizterland/Personal/Me_peronsal/Harari/Elastic_Python_Codes/Nexus_Convert/Nexus.pdf"
# Output file for JSON data
output_json = "/Users/gonzalovillarino/Documents/Swizterland/Personal/Me_peronsal/Harari/Elastic_Python_Codes/Nexus_Convert/nexus.ndjson"

try:
    # Open the PDF
    with pdfplumber.open(pdf_path) as pdf:
        with open(output_json, "w", encoding="utf-8") as f:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                # Write each page as a separate JSON object
                f.write(json.dumps({"page": i + 1, "content": text.strip() if text else ""}) + "\n")

    print(f"PDF has been successfully converted to {output_json}")

except Exception as e:
    print(f"Error occurred: {e}")
