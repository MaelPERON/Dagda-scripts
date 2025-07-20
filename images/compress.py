from PIL import Image
import os
import argparse

def resize_to_fit(input_folder, output_folder, max_size, quality=85):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder, exist_ok=True)
    images = os.listdir(input_folder)
    for i, filename in enumerate(images):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_folder, filename)
            with Image.open(img_path) as img:
                img.thumbnail((max_size, max_size))  # Fit within a square of size max_size
                output_path = os.path.join(output_folder, filename)
                img.save(output_path, optimize=True, quality=quality)
                print(f"({i+1}/{len(images)})Resized: {filename} -> {output_path}")

# Example usage:
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize images in a folder to fit within a square of max_size.")
    parser.add_argument("input_folder", help="Path to the input folder containing images")
    parser.add_argument("output_folder", help="Path to the output folder for resized images")
    parser.add_argument("max_size", type=int, help="Maximum size (pixels) for width and height")
    parser.add_argument("--quality", type=int, default=85, help="JPEG quality for output images (default: 85)")

    args = parser.parse_args()

    resize_to_fit(args.input_folder, args.output_folder, args.max_size, args.quality)