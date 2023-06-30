import streamlit as st
import pandas
from send_email import send_email

st.header("Contact me")
df = pandas.read_csv("topics.csv")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email adress")
    selected_option = st.selectbox("Choose your topic", df["topic"])
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New Email from {user_email}

From: {user_email}
Topic: {selected_option}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully")