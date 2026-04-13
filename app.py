import streamlit as st
import pandas as pd
import numpy as np

st.title("Simple Data Analytics App")

name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 0, 100, 25)

if name:
    st.write(f"Hello {name}, you are {age} years old!")

data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=['Column A', 'Column B']
)

st.write(data)
st.line_chart(data)
st.bar_chart(data)

if st.button("Celebrate"):
    st.balloons()
