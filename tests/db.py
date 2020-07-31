import platform

from sqlalchemy import Column, Date, Float, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = None
if platform.python_implementation() == "PyPy":
    engine = create_engine("sqlite:///tmp.db")
else:
    engine = create_engine("sqlite://")

Base = declarative_base()


class Pyexcel(Base):
    __tablename__ = "pyexcel"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    weight = Column(Float)
    birth = Column(Date)


class Signature(Base):
    __tablename__ = "signature"
    X = Column(Integer, primary_key=True)
    Y = Column(Integer)
    Z = Column(Integer)


class Signature2(Base):
    __tablename__ = "signature2"
    A = Column(Integer, primary_key=True)
    B = Column(Integer)
    C = Column(Integer)


Session = sessionmaker(bind=engine)
