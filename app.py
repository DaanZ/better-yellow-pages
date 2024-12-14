import streamlit as st
from handwriting_synthesis.hand import Hand


# Streamlit interface
def main():

    if "generated" not in st.session_state:
        st.session_state.generated = None

    st.title("Handwriting Synthesizer")

    # Text area for user input
    user_text = st.text_area("Enter the text you want to convert into handwriting:", height=150)

    # Number input for line style
    line_style = st.number_input("Select the line style (1 to 9):", min_value=1, max_value=9, value=5)

    # Button to generate handwriting
    if st.button("Generate Handwriting"):
        if user_text.strip():
            # Split user input into lines
            lines = user_text.strip().split("\n")

            # Define parameters
            biases = [0.75 for _ in lines]
            styles = [line_style for _ in lines]
            stroke_colors = ['black' for _ in lines]
            stroke_widths = [1.5 for _ in lines]

            with st.spinner("Generating handwriting..."):
                # Create handwriting SVG
                hand = Hand()
                svg_output = 'usage_demo.svg'
                hand.write(
                    filename=svg_output,
                    lines=lines,
                    biases=biases,
                    styles=styles,
                    stroke_colors=stroke_colors,
                    stroke_widths=stroke_widths
                )
                st.session_state.generated = svg_output
        else:
            st.warning("Please enter some text before generating handwriting.")

    handwritten_image = st.empty()

    if st.session_state.generated:
        handwritten_image.image(st.session_state.generated, caption="Generated Handwriting", width=600)


if __name__ == "__main__":
    main()
