import streamlit as st
import pandas as pd

st.title("🧪 Example Data")

st.write(
    "Example datasets for learning and testing process capability."
)

data = [
    10.02,
    10.05,
    9.98,
    10.01,
    10.03,
    10.00,
    9.99,
    10.04,
    10.01,
    9.97,
]

df = pd.DataFrame({
    "Measurement": data
})

st.dataframe(
    df,
    use_container_width=True
)

st.write("Number of observations:", len(data))