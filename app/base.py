import streamlit


class BaseStreamlitPage:
    def __init__(self):
        streamlit.set_page_config(page_title='VeritasDB')

    def load_page(self):
        raise NotImplementedError('Create a load_page function')
