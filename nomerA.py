import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

st.write('hello world')

st.header('st.button')

if st.button('say hello'):
    st.write('why hello there')
else:
    st.write('goodbye')

st.title("this is the app title")
st.markdown("this is the markdown")
st.header("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.write("x=2021")

st.checkbox("yes")
st.button("click")
st.radio("pick your gender",["male","female"])
st.selectbox("pick your gender",["male","female"])
st.selectbox("choose a planet",["planet"],None)
st.select_slider("pick a mark",["bad","good","excellent"])
st.slider("pick a number",0,50)

st.number_input("pick a number",1,10)
st.text_input("email address")
st.date_input("travelling date","today")
st.time_input("school time","now")
st.text_area("Description")
st.file_uploader("upload a phto")
st.color_picker("choose your favorite color")

st.header('st.write')
st.write("hello, *world!* :sunglasses:")
st.write(1234)

df = pd.DataFrame({
    'first': [1,2,3,4],
    'second':[10,20,30,40]
})
st.write(df)

st.write("below is dataframe:",df,"above is dataframe")

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=["a","b","c"]
)

c = alt.Chart(df2).mark_circle().encode(
    x = 'a', y ='b', size='c', color='c', tooltip = ['a','b','c']
)

st.write(c)

df = pd.DataFrame(
    np.random.randn(100,2),
    columns = ['x','y']
)
st.line_chart(df)


with st.container():
   st.write("This is inside the container")

   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")


st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)
    st.image("https://static.streamlit.io/examples/dice.jpg")


