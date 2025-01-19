import streamlit as st
import numpy as np
import pandas as pd
#import toml
#import mysql.connector as connection



#streamlit moment 3+ hours lost
# Initialize connection.
#conn = st.connection('mysql', type='sql')

# Perform query.
#df = conn.query('SELECT * FROM breach WHERE uri = "https://roblox.com" ORDER BY id DESC LIMIT 10;', ttl=600)

df = pd.read_csv('final_output_final_final.txt', sep=':')
st.dataframe(df)

# Using the variables we read from secrets.toml


# dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)