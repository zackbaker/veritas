import pytest
from sqlalchemy import delete

from models.base import VeritasMetaDB
from models.connections import Connections

class TestConnections:
    @classmethod
    def setup_class(self):
        self.db = VeritasMetaDB()

    @classmethod
    def teardown_class(self):
        # TODO: Get this in the base class somehow?
        stmt = delete(Connections).where(Connections.name == 'testing')
        session = self.db.get_session()
        session.execute(stmt)
        session.commit()

    def test_save(self):
        connection = Connections(
            name='testing',
            connection_type='postgres',
            meta_data={'user': 'test', 'password': 'test_test'},
            is_active=True
        )
        self.db.save_obj(connection)
        session = self.db.get_session()
        results = session.query(Connections).filter_by(name='testing').first()
        assert results == connection
