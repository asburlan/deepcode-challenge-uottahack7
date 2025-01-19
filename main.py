import streamlit as st
import numpy as np

# Initialize connection.
conn = st.connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * FROM breach WHERE uri = "https://roblox.com" ORDER BY id DESC LIMIT 10;', ttl=600)



dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)