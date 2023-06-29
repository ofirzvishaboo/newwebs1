import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("Ofir zvish")
content = """
    im 23 y/o from israel and grew up in givatayim
    """
st.info(content)

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data.csv", sep=",")
with col1:
    for index, row in df[:4].iterrows():
        st.header(f'{row["first name"]} {row["last name"]}')
        st.write(row["role"])
        st.image("images/" + row["image"])
with col2:
    for index, row in df[4:8].iterrows():
        st.header(f'{row["first name"]} {row["last name"]}')
        st.write(row["role"])
        st.image("images/" + row["image"])
with col3:
    for index, row in df[8:].iterrows():
        st.header(f'{row["first name"]} {row["last name"]}')
        st.write(row["role"])
        st.image("images/" + row["image"])
