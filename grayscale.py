import streamlit as st
from PIL import Image

uploaded_image1 = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    # start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # Create a pillow image
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

    # Render the grayscale image on the webpage
    st.image(gray_img)

if uploaded_image1:
    img1 = Image.open(uploaded_image1)
    gray_img1 = img1.convert("L")
    st.image(gray_img1)
