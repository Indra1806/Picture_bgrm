import os
from rembg import remove
from PIL import Image

def remove_background(input_path: str, output_path: str):
    try:
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)
        print(f"Background successfully removed. Image saved to: {output_path}")
    except FileNotFoundError:
        print(f"Error: The file at {input_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = "input_image.png"
    output_file = "output_image.png"
    remove_background(input_file, output_file)
