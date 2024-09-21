
import streamlit as st


add_siderbar = st.sidebar.selectbox('Aggregate or Individual Video', ('Aggregate Metrics', 'Individual Video Analysis'))

# total picture
if add_siderbar == 'Aggregate Metrics':
    st.write("Ken Jee YouTube Aggregated Data")
if add_siderbar == 'Individual Video Analysis':
    st.write('Ind')
