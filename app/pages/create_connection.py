from typing import Dict
import streamlit

from models.base import VeritasMetaDB
from base import BaseStreamlitPage
from models.connections import Connections


class CreateConnection(BaseStreamlitPage):
    # TODO: Errors stay in session after leaving and coming back from page
    # If I bust the cash in __init__ it won't hold the errors at all
    def __init__(self):
        self.db = VeritasMetaDB()

    def load_page(self):
        streamlit.title('Create Connection')

        self.display_errors()

        col1, col2 = streamlit.columns(2)
        with col1:
            connection_name = streamlit.text_input('Connection Name:')
        with col2:
            connection_type = streamlit.selectbox(
                'Connection Type',
                options=['Postgres', 'Snowflake']
            ).lower()

        meta_data = self.load_connection_details(connection_type)

        if streamlit.button('Save Connection'):
            self.check_for_errors(connection_name, meta_data)
            if not streamlit.session_state.errors:
                self.save_connection(connection_name, connection_type, meta_data)

    def display_errors(self):
        if 'errors' not in streamlit.session_state:
            streamlit.session_state.errors = []
        for error in streamlit.session_state.errors:
            streamlit.error(error)

    def check_for_errors(self, connection_name: str, meta_data: Dict[str, str]) -> None:
        streamlit.session_state.clear()
        if 'errors' not in streamlit.session_state:
            streamlit.session_state.errors = []

        session = self.db.get_session()
        if session.query(Connections).where(Connections.name == connection_name).count() > 0:
            self.write_error(
                'Connection already exist, must name connection something else'
            )

        if not connection_name:
            self.write_error('Connection Name cannot be empty')

        for param, value in meta_data.items():
            if not value:
                self.write_error(f'{param.title()} must be filled out')

        if streamlit.session_state.errors:
            streamlit.rerun()

    def save_connection(self, connection_name: str, connection_type: str, meta_data: dict):
        connection = Connections(
            name=connection_name,
            connection_type=connection_type,
            meta_data=meta_data
        )
        self.db.save_obj(connection)
        streamlit.switch_page('pages/connections.py')

    def write_error(self, err_msg: str) -> None:
        streamlit.session_state.errors.append(err_msg)

    def load_connection_details(self, connection_type: str) -> Dict[str, str]:
        col1, col2 = streamlit.columns(2)
        match connection_type:
            case 'postgres':
                with col1:
                    username = streamlit.text_input('Username:')
                    database = streamlit.text_input('Database:')
                with col2:
                    password = streamlit.text_input('Password:', type='password')
                    schema = streamlit.text_input('Schema:', placeholder='all')

                port = streamlit.text_input('Port:', placeholder='5432')
                return {
                    'username': username,
                    'password': password,
                    'database': database,
                    'schema': schema if schema else 'all',
                    'port': port if port else '5432'
                }
            case 'snowflake':
                streamlit.text('Gonna need to set this one up :)')
                return {}
            case other_value:
                return {}

CreateConnection().load_page()
