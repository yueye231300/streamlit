import streamlit as st
from datetime import time, datetime
import pandas as pd
import numpy as np

st.header('st.slider')

st.subheader('Slider')
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')


st.subheader('Range slider')
values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)


st.subheader('chart line')
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.subheader('select box')
options = st.selectbox('选择一个你喜欢的颜色', ['green', 'blue', 'red'])
st.write('Your favorite color is ', options)


st.subheader('multiselect')
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue','黄色'],
     ['Yellow', 'Red'])
st.write('You selected:', options)


st.subheader('checkbox')
st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee:
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")