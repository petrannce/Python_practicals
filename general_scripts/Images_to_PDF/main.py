from fpdf import FPDF
import os

def create_pdf_with_images(image_folder, output_pdf):
    pdf = FPDF()
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    for image_file in sorted(image_files):
        pdf.add_page()
        image_path = os.path.join(image_folder, image_file)
        pdf.image(image_path, x=0, y=0, w=210, h=297) # A4 size
    pdf.output(output_pdf, 'F')

if __name__ == '__main__':
    image_folder = 'images'  # Replace with your image folder path
    output_pdf = 'images_pdf.pdf'
    create_pdf_with_images(image_folder, output_pdf)