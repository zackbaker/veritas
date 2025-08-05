from sqlalchemy import JSON, BigInteger, Boolean, Column, String
from models.base import ORMBase


class Connections(ORMBase):
    '''
    Manages the different connections
    '''
    __tablename__ = 'connections'

    id = Column(BigInteger, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    connection_type = Column(String, nullable=False)
    meta_data = Column(JSON, nullable=False)
    is_active = Column(Boolean, default=True)
