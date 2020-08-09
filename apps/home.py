import streamlit as st
import pandas as pd
import numpy as np
from data.create_data import create_table

def app():
    st.title('Home')

    st.write("This is a sample home page in the mutliapp.")
    st.write("See `apps/home.py` to know how to use it.")

    st.markdown("### Sample Data")
    df = create_table()
    st.write(df)

    st.write('Navigate to `Data Stats` page to visualize the data')


