import cairosvg


# Convert SVG to PNG
def convert_svg_to_png(input_svg_path, output_png_path, width=None, height=None):
    """
    Convert an SVG file to a transparent PNG.

    Args:
        input_svg_path (str): Path to the input SVG file.
        output_png_path (str): Path to the output PNG file.
        width (int): Optional width for resizing the image.
        height (int): Optional height for resizing the image.
    """
    with open(input_svg_path, 'rb') as svg_file:
        svg_data = svg_file.read()
        cairosvg.svg2png(
            bytestring=svg_data,
            write_to=output_png_path,
            output_width=width,
            output_height=height,
        )
    print(f"PNG saved at {output_png_path}")


if __name__ == "__main__":
    # Example usage
    input_svg = "overlay.svg"  # Path to your SVG
    output_png = "example.png"  # Path to save the PNG
    convert_svg_to_png(input_svg, output_png, width=800, height=600)
