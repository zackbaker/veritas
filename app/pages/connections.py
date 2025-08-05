from typing import List
import streamlit

from models.base import VeritasMetaDB
from base import BaseStreamlitPage
from models.connections import Connections

class ViewConnections(BaseStreamlitPage):
    def __init__(self):
        self.db = VeritasMetaDB()

    def load_page(self):
        streamlit.title('Connections')

        # TODO: Add search symbol in placeholder?
        search = streamlit.text_input('', placeholder='Search for Connection Name')

        if streamlit.button('Create Connection', use_container_width=True):
            streamlit.switch_page('pages/create_connection.py')
        
        connections = self.get_connections(search)
        self.display_connections(connections)

    def get_connections(self, search: str) -> List[Connections]:
        if search:
            return self.db.get_session().query(Connections).where(Connections.name.ilike(f'%{search}%')).all()
        return self.db.get_session().query(Connections).all()

    def display_connections(self, connections: List[Connections]) -> None:
        for connection in connections:
            # TODO: Put connection icons next to name i.e. postgres logo
            with streamlit.expander(str(connection.name), expanded=True):
                cols = streamlit.columns(3)
                i = 1
                for element, value in connection.meta_data.items():
                    if element == 'password':
                        value = '********'
                    cols[i - 1].write(f'{element.title()}: {value}')

                    if i < 3:
                        i += 1
                    else:
                        i = 1

                _, _, col3 = streamlit.columns(3)
                if col3.button('View Connection', key=str(connection.id)):
                    pass
                


ViewConnections().load_page()
