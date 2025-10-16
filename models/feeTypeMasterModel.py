from sqlalchemy import Column, Integer, SmallInteger, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class feeTypeMaster(Base):
    __tablename__ = "noc_fee_type_master"
    __table_args__ = {"schema": "public"}

    fee_type_id_pk = Column(
        Integer,
        Sequence("fee_type_master_fee_type_id_pk_seq"),
        primary_key=True
    )
    fee_type = Column(Integer, nullable=True)  # You may want this to be String instead of Integer?
    active_status = Column(SmallInteger, nullable=True)