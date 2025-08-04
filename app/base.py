import streamlit


class BaseStreamlitPage:
    def __init__(self):
        streamlit.set_page_config(page_title='VeritasDB')
