import sys
import os
import cv2
import numpy as np
from PIL import Image

def prep_photo(input_path, output_path="source-prepped.png"):
    if not os.path.exists(input_path):
        print(f"Error: Input photo '{input_path}' not found.")
        sys.exit(1)

    print(f"Loading image from '{input_path}'...")
    input_image = Image.open(input_path).convert("RGBA")

    # Step 1: Remove background using rembg with fallback
    try:
        from rembg import remove
        print("Removing background using rembg...")
        bg_removed = remove(input_image)
    except Exception as e:
        print(f"Notice: rembg failed or model unavailable ({e}). Using threshold background isolation fallback.")
        # Fallback background isolation: thresholding light borders
        img_np = np.array(input_image)
        gray = cv2.cvtColor(img_np, cv2.COLOR_RGBA2GRAY)
        # Create alpha mask from otsu thresholding or non-white area
        _, alpha = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
        img_np[:, :, 3] = alpha
        bg_removed = Image.fromarray(img_np)

    # Step 2: Composite onto pure white background
    white_bg = Image.new("RGBA", bg_removed.size, (255, 255, 255, 255))
    composited = Image.alpha_composite(white_bg, bg_removed).convert("L")
    img_gray = np.array(composited)

    # Step 3: Boost local contrast with OpenCV CLAHE
    print("Applying CLAHE local contrast enhancement...")
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(img_gray)

    # Save output
    cv2.imwrite(output_path, enhanced)
    print(f"Successfully saved prepped image to '{output_path}'")

if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "Ruturaj_Passport_photo.png"
    if not os.path.exists(src):
        # Fallback search for common names
        for alt in ["source-photo.jpg", "source-photo.png", "Ruturaj_Passport_photo.png"]:
            if os.path.exists(alt):
                src = alt
                break

    prep_photo(src)
