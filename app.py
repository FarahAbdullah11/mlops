import streamlit as st
import pandas as pd

st.title("Simple CSV Reader")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("First 3 Rows:")
    # Display the first 3 rows directly in the web app
    st.write(df.head(3))
