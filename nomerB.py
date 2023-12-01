import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df_mobil =  pd.read_csv("CarPrice_Assignment.csv")

x = df_mobil[['highwaympg','curbweight','horsepower']]
y = df_mobil['price']

#13
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

model_regresi = LinearRegression()
model_regresi.fit(x_train,y_train)

filename = 'model_prediksi_harga_mobil.sav'
pickle.dump(model_regresi,open(filename,'wb'))

model = pickle.load(open('model_prediksi_harga_mobil.sav','rb'))

st.title('prediksi harga mobil')

st.header("dataset")

st.dataframe(df_mobil)

st.write("grafik curbweight")
chart_curbweight = df_mobil['curbweight']
st.line_chart(chart_curbweight)

st.write("grafik horsepower")
chart_horsepower = df_mobil['horsepower']
st.line_chart(chart_horsepower)

highwaympg = st.number_input("highwaympg",10,60)
curbweight = st.number_input("curbweight",1000,5000)
horsepower = st.number_input("horsepower",40,300)

if st.button('prediksi'):
    car_prediction = model.predict([[highwaympg,curbweight,horsepower]])

    harga_mobil_str = np.array(car_prediction)
    harga_mobil_float = float(harga_mobil_str[0])

    harga_mobil_formatted = st.write('jadi harga mobil adalah = $ ',"{:,.3f}".format(harga_mobil_float))
