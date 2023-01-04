from gino import Gino
from sqlalchemy import Column, Integer, BigInteger, String, Boolean, Sequence
from sqlalchemy import sql

db = Gino()


class Users(db.Model):
    __tablename__ = 'users'
    id = Column(Integer(), Sequence('user_id_seq'), primary_key=True)
    user_id = Column(BigInteger())
    username = Column(String(32))
    full_name = Column(String(257))
    banned = Column(Boolean(), default=False)
    query: sql.Select
