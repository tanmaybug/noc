from sqlalchemy import Column, Integer, String, SmallInteger, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class minorityTypeMaster(Base):
    __tablename__ = "noc_minority_type_master"
    __table_args__ = {"schema": "public"}

    minority_type_id_pk = Column(
        Integer,
        Sequence("minority_type_master_minority_type_id_pk_seq"),
        primary_key=True
    )
    minority_type = Column(String, nullable=True)
    active_status = Column(SmallInteger, nullable=True)
