from xml.etree import ElementTree as ET
import cairosvg


def clean_svg_background(svg_path):
    """Remove background elements from an SVG to ensure transparency."""
    tree = ET.parse(svg_path)
    root = tree.getroot()

    # Iterate through all elements to find the <rect> tag with a white fill
    for rect in root.findall(".//{http://www.w3.org/2000/svg}rect"):
        root.remove(rect)

    # Save the cleaned SVG
    clean_svg_path = svg_path.replace(".svg", "_cleaned.svg")
    tree.write(clean_svg_path)

    # Step 2: Convert the SVG to a rasterized format (PNG)
    png_path = clean_svg_path.replace(".svg", ".png")
    cairosvg.svg2png(url=clean_svg_path, write_to=png_path)

    return png_path


if __name__ == "__main__":
    # Example usage
    input_svg = "images/testing.svg"  # Your SVG path
    clean_svg = clean_svg_background(input_svg)
