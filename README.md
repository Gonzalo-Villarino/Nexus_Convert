# Nexus Convert

This repository contains the code and resources for converting PDF documents into Newline-delimited JSON (NDJSON) format. The conversion process uses Python and the `pdfplumber` library to extract text from a PDF document. The resulting JSON can then be imported into Elasticsearch or similar platforms for indexing and search.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Gonzalo-Villarino/Nexus_Convert.git
    ```

2. Navigate to the project folder:
    ```bash
    cd Nexus_Convert
    ```

3. Install the required Python libraries:
    ```bash
    pip install pdfplumber
    ```

## Usage

1. Place the PDF file you want to convert into the project folder.

2. Run the Python script to convert the PDF to NDJSON:
    ```bash
    python convert_Nexus_pdf_to_ndjson.py
    ```

3. The script will generate a `nexus.ndjson` file that you can use for import into Elasticsearch or any other service that supports NDJSON format.

## Example
Here is a sample of the output JSON format:
```json
{
    "page": 1,
    "content": "Extracted text from page 1 of the PDF document."
}
