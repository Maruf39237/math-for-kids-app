import numpy as np
import pandas as pd
import streamlit as st
import random


st.markdown(
    """
    <style>
        [data-testid="stSidebarNavItems"] span {
            font-size: 24px !important;
            font-weight: bold;
        }

        [data-testid="stSidebar"] {
        width: 300px !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

home = st.Page("home.py", title = "Home")
add = st.Page("addition.py", title = "Addition")
subtract = st.Page("subtraction.py", title = "Subtraction")
multiply = st.Page("multiplication.py", title = "Multiplication")
divide = st.Page("division.py",title = "Division")


pg = st.navigation([home, add, subtract, multiply, divide], position = "sidebar")
pg.run()


