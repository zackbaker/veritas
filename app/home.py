import streamlit

from base import BaseStreamlitPage

class HomePage(BaseStreamlitPage):
    def load_page(self):
        streamlit.title('This Is My Title')

if __name__ == '__main__':
    HomePage().load_page()
