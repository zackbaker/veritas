import streamlit

from base import BaseStreamlitPage

class HomePage(BaseStreamlitPage):
    def load_page(self):
        streamlit.title('This Is My Title')
        streamlit.subheader('WHY WONT YOU WORK???')

HomePage().load_page()
