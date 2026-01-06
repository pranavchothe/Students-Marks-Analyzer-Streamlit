'''Q2. Build a streamlit app that analyzes student marks and shows basic insights.
Columns:
Name
Subject
Marks

####Tasks

Upload a csV file
Display the dataset
Show:
Average marks
Highest marks
Lowest marks
Filter data by subject
Display a bar chart of student marks'''



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Students Marks Analyzer")

st.title("Students Marks Analyzer")
st.write("Uploade a CSV file containing student marks data with columns: Name, Subject, Marks")

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv","xls","xlsx"])

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    st.subheader("Dataset")
    st.dataframe(df)

    required_columns = {"Name", "Subject", "Marks"}
    if not required_columns.issubset(df.columns):
        st.error(f"File Must Contain: Name, Subject, Marks")
    else:

        df["Marks"]= pd.to_numeric(df["Marks"], errors='coerce')
        df = df.dropna()

        avg_marks = df["Marks"].mean()  
        max_marks = df["Marks"].max()
        min_marks = df["Marks"].min()

        st.subheader("Insights")
        st.write(f"Average Marks: {avg_marks}")
        st.write(f"Highest Marks: {max_marks}")
        st.write(f"Lowest Marks: {min_marks}")

        st.subheader("Filter Data by Subject")
        subjects = df["Subject"].unique()
        selected_subject = st.selectbox("Select Subject", subjects) 
        filtered_df = df[df["Subject"] == selected_subject]
        st.dataframe(filtered_df)

        st.subheader("Bar chart of Student Marks")

        fig, ax = plt.subplots()
        ax.bar(filtered_df["Name"], filtered_df["Marks"], color='skyblue')
        ax.set_xlabel("Student Name")
        ax.set_ylabel("Marks")
        ax.set_title(f"Marks of Students in {selected_subject}")
        plt.xticks(rotation=45)
        st.pyplot(fig)

else:
    st.info("Please upload a CSV file to analyze student marks.")