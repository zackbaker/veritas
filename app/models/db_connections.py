from sqlalchemy import JSON, BigInteger, Column, String
from models.base import ORMBase


class Connections(ORMBase):
    '''
    Manages the different connections
    '''
    __tablename__ = 'connections'

    id = Column(BigInteger, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    meta_data = Column(JSON, nullable=False)
