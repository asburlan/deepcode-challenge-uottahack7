import streamlit as st
import pandas as pd

st.set_page_config(layout="centered")

@st.cache_data(show_spinner=False)
def load_data(file_path):
    dataset = pd.read_csv(file_path, sep=':')
    return dataset

@st.cache_data(show_spinner=False)
def split_frame(input_df, rows, page):
    start = (page - 1) * rows
    end = start + rows
    return input_df.iloc[start:end]

file_path = 'final_output_with_priv.txt'
if file_path:
    dataset = load_data(file_path)
    top_menu = st.columns(3)
    with top_menu[0]:
        filter = st.checkbox("exclude non routable ip ranges", value=True)
    if filter:
        dataset = dataset[dataset['is_private'] != True]
    with top_menu[1]:
        search = st.text_input("Search", placeholder="eg. roblox")
        if search:
            dataset = dataset[dataset['uri'].str.contains(search, case=False, na=False)]
    
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

    paginated_data = split_frame(dataset, batch_size, current_page)
    pagination.dataframe(data=paginated_data, use_container_width=True, hide_index=True)