import os
import sqlalchemy
import dotenv

from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


class ORMBase(DeclarativeBase):
    pass


class VeritasMetaDB:
    def __init__(self):
        dotenv.load_dotenv()
        user = os.getenv('VERITAS_DB_USERNAME')
        password = os.getenv('VERITAS_DB_PASSWORD')
        db_url = os.getenv('VERITAS_DB_URL')
        database = os.getenv('VERITAS_DB_DATABASE')
        self.db_url = f'postgresql+psycopg2://{user}:{password}@{db_url}:5432/{database}'
        self.engine = sqlalchemy.create_engine(self.db_url)
        self.session = sessionmaker(self.engine)()

    def __del__(self):
        self.session.close()

    def get_url(self) -> str:
        return self.db_url

    def get_session(self) -> Session:
        return self.session

    def save_obj(self, obj: ORMBase):
        try:
            self.session.add(obj)
            self.session.commit()
        except Exception:
            self.session.rollback()

