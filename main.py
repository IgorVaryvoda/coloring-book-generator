import os
from fpdf import FPDF
from PIL import Image

def create_coloring_book(input_folder, output_file):
    # PDF setup
    pdf = FPDF(orientation='P', unit='mm', format='Letter')
    pdf.set_auto_page_break(auto=True, margin=0)

    # Get list of image files
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    for image_file in image_files:
        # Add image page
        pdf.add_page()
        add_image_to_page(pdf, os.path.join(input_folder, image_file))

        # Add blank page
        pdf.add_page()

    # Save the PDF
    pdf.output(output_file)

def add_image_to_page(pdf, image_path):
    # Calculate page dimensions and margins
    page_width = 215.9  # 8.5 inches in mm
    page_height = 279.4  # 11 inches in mm
    left_margin = 9.6  # gutter margin
    right_margin = 9.6
    top_margin = 9.6
    bottom_margin = 9.6

    # Calculate image area
    image_width = page_width - left_margin - right_margin
    image_height = page_height - top_margin - bottom_margin

    # Open and resize image
    with Image.open(image_path) as img:
        img.thumbnail((image_width, image_height))
        temp_path = 'temp_image.png'
        img.save(temp_path)

    # Add image to PDF
    pdf.image(temp_path, x=left_margin, y=top_margin, w=image_width, h=image_height)

    # Remove temporary image file
    os.remove(temp_path)

if __name__ == "__main__":
    input_folder = input("Enter the path to the folder containing images: ")
    output_file = input("Enter the name of the output PDF file: ")
    create_coloring_book(input_folder, output_file)
    print(f"Coloring book PDF has been generated: {output_file}")
