import streamlit as st

st.header('streamlit_button')
if st.button('say hello'):
     st.write('why hello there')
else:
    st.write('Goodbye')