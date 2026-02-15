import os
from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):
   
    reader = PdfReader(pdf_path)
    text = ""
    
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text.strip(), len(reader.pages)


def load_pdfs_from_directory(directory_path="data"):
    """
    Loads all PDF files from a directory.
    Returns a list of structured document dictionaries.
    """
    documents = []

    for filename in os.listdir(directory_path):
        if filename.lower().endswith(".pdf"):
            full_path = os.path.join(directory_path, filename)
            
            text, num_pages = extract_text_from_pdf(full_path)

            document = {
                "paper_id": os.path.splitext(filename)[0],
                "text": text,
                "metadata": {
                    "num_pages": num_pages,
                    "source_path": full_path
                }
            }

            documents.append(document)

    return documents
