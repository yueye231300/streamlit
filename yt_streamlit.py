import streamlit as st
from datetime import time, datetime
import pandas as pd
import numpy as np
import time as times

st.set_page_config(layout="wide")
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


st.subheader('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)


with st.expander('About this app'):
     st.write('This app shows the various ways on how you can layout your Streamlit app.')
     st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])


col1, col2, col3 = st.columns(3)
with col1:
     if user_name != '':
          st.write(f'👋 Hello {user_name}!')
     else:
          st.write('👈  Please enter your **name**!')

with col2:
     if user_emoji != '':
          st.write(f'{user_emoji} is your favorite **emoji**!')
     else:
          st.write('👈 Please choose an **emoji**!')

with col3:
     if user_food != '':
          st.write(f'🍴 **{user_food}** is your favorite **food**!')
     else:
          st.write('👈 Please choose your favorite **food**!')


with st.expander('About this app'):
     st.write('You can now display the progress of your calculations in a Streamlit app with the `st.progress` command.')

my_bar = st.progress(0)
for percent_complete in range(100):
     times.sleep(0.05)
     my_bar.progress(percent_complete + 1)

st.balloons()
