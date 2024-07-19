import os
from fpdf import FPDF
from PIL import Image

def create_coloring_book():
    input_folder = '/home/igor/Desktop/coloring book/upscaled'
    output_file = '/home/igor/Desktop/coloring book/upscaled/result.pdf'
    # PDF setup
    pdf = FPDF(orientation='P', unit='mm', format='Letter')
    pdf.set_auto_page_break(auto=True, margin=0)

    # Get list of image files
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    print(image_files)
    for image_file in image_files:
        print(f"Processing image: {image_file}")  # Debug statement
        # Add image page
        pdf.add_page()
        add_image_to_page(pdf, os.path.join(input_folder, image_file))

        # Add blank page
        pdf.add_page()

    # Save the PDF
    pdf.output(output_file)
    print(f"PDF saved as: {output_file}")  # Debug statement

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

    # Open image and get dimensions
    with Image.open(image_path) as img:
        img_width, img_height = img.size
        aspect_ratio = img_width / img_height

        if image_width / image_height > aspect_ratio:
            # Image is wider relative to its height
            new_height = image_height
            new_width = aspect_ratio * new_height
        else:
            # Image is taller relative to its width
            new_width = image_width
            new_height = new_width / aspect_ratio

        # Calculate position to center the image
        x_pos = (page_width - new_width) / 2
        y_pos = (page_height - new_height) / 2

        print(f"Adding image to PDF: {image_path}")  # Debug statement
        # Add image to PDF
        pdf.image(image_path, x=x_pos, y=y_pos, w=new_width, h=new_height)

if __name__ == "__main__":
    create_coloring_book()
    print(f"Coloring book PDF has been generated")
