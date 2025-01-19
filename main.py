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

st.set_page_config(layout="centered")

@st.cache_data(show_spinner=False)
def load_data(file_path):
    dataset = pd.read_csv(file_path, sep=':')
    return dataset

@st.cache_data(show_spinner=False)
def split_frame(input_df, rows):
    df = [input_df.loc[i : i + rows - 1, :] for i in range(0, len(input_df), rows)]
    return df

file_path = 'final_output_final_final.txt'
if file_path:
    dataset = load_data(file_path)
    top_menu = st.columns(3)
    # with top_menu[0]:
    #     sort = st.radio("Sort Data", options=["Yes", "No"], horizontal=1, index=1)
    # if sort == "Yes":
    #     with top_menu[1]:
    #         sort_field = st.selectbox("Sort By", options=dataset.columns)
    #     with top_menu[2]:
    #         sort_direction = st.radio(
    #             "Direction", options=["⬆️", "⬇️"], horizontal=True
    #         )
    #     dataset = dataset.sort_values(
    #         by=sort_field, ascending=sort_direction == "⬆️", ignore_index=True
    #     )
    pagination = st.container()

    bottom_menu = st.columns((4, 1, 1))
    with bottom_menu[2]:
        batch_size = st.selectbox("Page Size", options=[25, 50, 100])
    with bottom_menu[1]:
        total_pages = (
            int(len(dataset) / batch_size) if int(len(dataset) / batch_size) > 0 else 1
        )
        current_page = st.number_input(
            "Page", min_value=1, max_value=total_pages, step=1
        )
    with bottom_menu[0]:
        st.markdown(f"Page **{current_page}** of **{total_pages}** ")


    # Add Increase and Decrease buttons
    # col1, col2 = st.columns([1, 1])
    # with col1:
    #     if st.button("Previous Page") and current_page > 1:
    #         current_page -= 1
    # with col2:
    #     if st.button("Next Page") and current_page < total_pages:
    #         current_page += 1

    pages = split_frame(dataset, batch_size)
    pagination.dataframe(data=pages[current_page - 1], use_container_width=True, hide_index=True)




#st.set_page_config(layout="centered")



#df = pd.read_csv('final_output_final_final.txt', sep=':')
#st.dataframe(df, hide_index=True)

# Using the variables we read from secrets.toml


# dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)