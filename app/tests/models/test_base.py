import pytest

from models.base import VeritasMetaDB


class TestVeritasMetaDB:
    @classmethod
    def setup_class(self):
        self.veritas_db = VeritasMetaDB()

    def test__init__(self):
        assert self.veritas_db.engine is not None
        assert self.veritas_db.db_url is not None

    def test_get_url(self):
        assert self.veritas_db.get_url() is not None
        assert isinstance(self.veritas_db.get_url(), str)
