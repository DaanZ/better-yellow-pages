import os

from PIL import Image
import rootpath


def convert_pages(text_image: str = "images/testing_cleaned.png", output_png: str = "result.jpg"):
    # Step 1: Load the JPG background
    background_path = os.path.join(rootpath.detect(), "demo", "images", "background.jpg")
    background = Image.open(background_path).convert("RGBA")  # Convert to RGBA for transparency handling

    # Step 3: Load the rasterized SVG as an image
    overlay = Image.open(text_image).convert("RGBA")  # Ensure overlay is in RGBA format

    # Step 5: Overlay the images using alpha compositing
    # Create a blank image with the same size as the background
    result = Image.new("RGBA", background.size, (255, 255, 255, 0))

    # Paste the background and overlay on the result image
    result.paste(background, (0, 0))  # Paste the background at the top-left corner
    result.paste(overlay, (70, 45), overlay)  # Use overlay as its own mask

    # Step 6: Convert to RGB (if needed) and save the final image
    final_result = result.convert("RGB")  # Remove alpha channel if saving as JPG
    final_result.save(output_png)
    return output_png