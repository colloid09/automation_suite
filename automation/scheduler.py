
import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(file_path):
    reader = PdfReader(file_path)
    base = os.path.splitext(file_path)[0]
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        out_path = f"{base}_page_{i+1}.pdf"
        with open(out_path, 'wb') as f:
            writer.write(f)
