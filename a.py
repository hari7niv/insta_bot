import sqlite3
import streamlit as st

con = sqlite3.connect('sql.db')

cursor = con.cursor()
data = cursor.execute("select * from scam")

st.header("id_:\password")
for row in data:
    st.text(row)

