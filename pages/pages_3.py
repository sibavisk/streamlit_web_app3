import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/data.csv')
st.dataframe(df)