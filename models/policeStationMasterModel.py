from sqlalchemy import Column, Integer, String, SmallInteger, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class policeStationMaster(Base):
    __tablename__ = "noc_police_station_master"
    __table_args__ = {"schema": "public"}

    police_station_id_pk = Column(
        Integer,
        Sequence("police_station_master_police_station_id_pk_seq"),
        primary_key=True
    )
    police_station_name = Column(String(255), nullable=True)
    active_status = Column(SmallInteger, nullable=True)
