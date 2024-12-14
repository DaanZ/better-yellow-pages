from handwriting_synthesis.hand import Hand

lines = [
    "Our Acclaim replacement windows and exclusive new",
    "Ensemble entry doors are engineered to perform in all",
    "climates and in every season. Each window and door is",
    "precision manufactored and custom-measured for",
    "a weathertight fit that helps seal out drafts and the",
    "elements, helping reduce high energy bills and provide",
    "year-round comfort."
]
biases = [.75 for _ in lines]
styles = [5 for _ in lines]
stroke_colors = ['black' for _ in lines]
stroke_widths = [1.5 for _ in lines]

hand = Hand()
hand.write(
    filename='usage_demo.svg',
    lines=lines,
    biases=biases,
    styles=styles,
    stroke_colors=stroke_colors,
    stroke_widths=stroke_widths
)