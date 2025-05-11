from pdf2docx import Converter

def convert_pdf_to_docx(pdf_file, docx_file):
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()

if __name__ == "__main__":
    pdf_file = 'example.pdf'  # Replace with your PDF file path
    docx_file = 'output.docx'  # Replace with your desired DOCX file path
    convert_pdf_to_docx(pdf_file, docx_file)
    print(f"Converted {pdf_file} to {docx_file}")
# This script converts a PDF file to a DOCX file using the pdf2docx library.
# It defines a function `convert_pdf_to_docx` that takes the input PDF file and the output DOCX file as arguments.