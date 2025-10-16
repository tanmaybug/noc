from sqlalchemy import Column, Integer, String, SmallInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class demographicMaster(Base):
    __tablename__ = "noc_demographic_master"

    demographic_id_pk = Column(Integer, primary_key=True, index=True)
    demographic_description = Column(String(255), nullable=True)
    active_status = Column(SmallInteger, nullable=True)
  
