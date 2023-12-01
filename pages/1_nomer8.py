import streamlit as st
import altair as alt
import pandas as pd
import numpy as npd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

df_rumah = pd.read_csv("housing_price_dataset.csv")
st.image('avatar_mahasiswa.png')
st.markdown("# Plotting Demo")
pilihan = st.sidebar.selectbox("select column",df_rumah.columns)
st.dataframe(df_rumah[pilihan])