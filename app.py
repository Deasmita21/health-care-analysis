
import streamlit as st
import pandas as pd

st.set_page_config(page_title="My Dashboard", layout="wide")

st.title("📊 My Dashboard")

st.write("Hello, Streamlit!")

# Load dataset
df = pd.read_csv("Processed_UAC_Data.csv")

st.subheader("Dataset Preview")
st.dataframe(df)

st.subheader("Basic Statistics")
st.write(df.describe())
