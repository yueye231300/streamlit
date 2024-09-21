#import relevant libraries (visualization, dashboard, data manipulation)
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from datetime import datetime
# build dashboard

add_siderbar = st.sidebar.selectbox('Aggregate or Individual Video', ('Aggregate Metrics', 'Individual Video Analysis'))

# total picture
if add_siderbar == 'Aggregate Metrics':
    st.write("Ken Jee YouTube Aggregated Data")
if add_siderbar == 'Individual Video Analysis':
    st.write('Ind')
