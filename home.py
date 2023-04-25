import streamlit as st
import os
from PIL import Image
from matplotlib import image


st.header(":blue[Flipkart Laptop Price Prediction Data App :desktop_computer]")
#Using subheader
st.write('By: :red[Harshal Mahajan]')

#Adding Image
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_of_interest = os.path.join(FILE_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "images")
IMAGE_PATH1 = os.path.join(IMAGE_PATH, "pic.jpg")

img = image.imread(IMAGE_PATH1)
st.image(img)