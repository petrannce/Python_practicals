from PyPDF2 import PdfReader, PdfWriter
import getpass

def protect_pdf(input_pdf, output_pdf):
    # Create a PdfReader object
    reader = PdfReader(input_pdf)

    # Create a PdfWriter object
    writer = PdfWriter()

    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Get the password from the user
    password = getpass.getpass("Enter the password to protect the PDF: ")

    # Encrypt the PDF with the password
    writer.encrypt(password)

    # Write the protected PDF to a new file
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)
    print(f"Protected PDF saved as {output_pdf}")
    
if __name__ == "__main__":
    input_pdf = "example.pdf"  # Replace with your input PDF file
    output_pdf = "protected_example.pdf"  # Replace with your desired output PDF file
    protect_pdf(input_pdf, output_pdf)
# This script protects a PDF file with a password using PyPDF2.