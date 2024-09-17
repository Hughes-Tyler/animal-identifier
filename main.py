import streamlit as st
from PIL import Image

# Set the header of the app
st.title("Machine Learning Animal Identifier")

# Load the image
image = Image.open('leopard.jpg')

# Display the image
st.image(image, use_column_width=True)

# Center the button using columns for layout
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button('Identify Animal'):
        # Display "Snowy Owl" in bold and larger font size
        st.markdown("<h2 style='text-align: center; font-weight: bold;'>Not Snowy Owl (Bubo Scandiacus)</h2>", unsafe_allow_html=True)
