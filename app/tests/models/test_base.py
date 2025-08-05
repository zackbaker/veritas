import pytest
from sqlalchemy import text
from sqlalchemy.orm import Session

from models.base import VeritasMetaDB


class TestVeritasMetaDB:
    @classmethod
    def setup_class(self):
        self.veritas_db = VeritasMetaDB()

    def test__init__(self):
        assert self.veritas_db.engine is not None
        assert self.veritas_db.db_url is not None
        
        connection = self.veritas_db.engine.connect()
        result = connection.execute(text('SELECT 1'))
        for row in result:
            assert row[0] == 1

        connection.close()

    def test_get_url(self):
        assert self.veritas_db.get_url() is not None
        assert isinstance(self.veritas_db.get_url(), str)

    def test_get_session(self):
        assert isinstance(self.veritas_db.get_session(), Session)

    def test_save_obj(self):
        # This wil be tested as part of the ORM classes
        assert True
