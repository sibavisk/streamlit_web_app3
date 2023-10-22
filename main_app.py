import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

st.title('サプーアプリ')
st.caption('これはサプーアプリの動画用テストアプリです')

image = Image.open('/Users/shibatakouki/Desktop/レタッチ/retouch2023-31edw.jpg')
st.image(image,width=200)

