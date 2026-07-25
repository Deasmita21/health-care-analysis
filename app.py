
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ------------------------------------
# Page Configuration
# ------------------------------------
st.set_page_config(
    page_title="Healthcare Capacity Dashboard",
    page_icon="🏥",
    layout="wide"
)

# ------------------------------------
# Load Dataset
# ------------------------------------
df = pd.read_csv("Processed_UAC_Data.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# ------------------------------------
# Sidebar
# ------------------------------------
st.sidebar.title("Dashboard Menu")

option = st.sidebar.radio(
    "Select Section",
    [
        "Dashboard",
        "Data Preview",
        "Statistics"
    ]
)

# ------------------------------------
# Dashboard
# ------------------------------------
if option == "Dashboard":

    st.title("Healthcare Capacity Monitoring Dashboard")
    st.markdown("---")

    # ================= KPIs =================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total System Load",
            int(df["Total_System_Load"].iloc[-1])
        )

    with col2:
        st.metric(
            "Current Backlog",
            int(df["Backlog"].iloc[-1])
        )

    with col3:
        st.metric(
            "Net Daily Intake",
            int(df["Net_Daily_Intake"].iloc[-1])
        )

    st.markdown("---")

    # ================= Graph 1 =================

    st.subheader("Total System Load")

    fig = px.line(
        df,
        x="Date",
        y="Total_System_Load",
        title="Total System Load Over Time"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ================= Graph 2 =================

    st.subheader("CBP vs HHS Care")

    fig = px.line(
        df,
        x="Date",
        y=[
            "Children in CBP custody",
            "Children in HHS Care"
        ],
        title="CBP vs HHS Care"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ================= Graph 3 =================

    st.subheader("Net Daily Intake")

    fig = px.bar(
        df,
        x="Date",
        y="Net_Daily_Intake",
        title="Net Daily Intake"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ================= Graph 4 =================

    st.subheader("Backlog Trend")

    fig = px.line(
        df,
        x="Date",
        y="Backlog",
        title="Backlog Over Time"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ================= Graph 5 =================

    if "Rolling_7_Day" in df.columns:

        st.subheader("7-Day Rolling Average")

        fig = px.line(
            df,
            x="Date",
            y="Rolling_7_Day"
        )

        st.plotly_chart(fig, use_container_width=True)

    # ================= Heatmap =================

    st.subheader("Correlation Heatmap")

    fig, ax = plt.subplots(figsize=(8,6))

    sns.heatmap(
        df.select_dtypes(include="number").corr(),
        annot=True,
        cmap="Purples",
        ax=ax
    )

    st.pyplot(fig)

# ------------------------------------
# Data Preview
# ------------------------------------
elif option == "Data Preview":

    st.title("Dataset Preview")

    st.dataframe(
        df,
        use_container_width=True
    )

# ------------------------------------
# Statistics
# ------------------------------------
elif option == "Statistics":

    st.title("Dataset Statistics")

    st.write(df.describe())

    st.markdown("### Missing Values")

    st.write(df.isnull().sum())

    st.markdown("### Data Types")

    st.write(df.dtypes)

# ------------------------------------
# Download
# ------------------------------------

csv = df.to_csv(index=False)

st.download_button(
    label="Download Processed Dataset",
    data=csv,
    file_name="Processed_UAC_Data.csv",
    mime="text/csv"
)
