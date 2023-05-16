"""
This example shows how to create a database with sqlalchemy
"""

import os
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
import sqlalchemy

Base = declarative_base()
STRING_LENGTH = 250


class Person(Base):  # type: ignore
    __tablename__ = "person"
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(STRING_LENGTH), nullable=False)


class Address(Base):  # type: ignore
    __tablename__ = "address"
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(STRING_LENGTH))
    street_number = Column(String(STRING_LENGTH))
    post_code = Column(String(STRING_LENGTH), nullable=False)
    person_id = Column(Integer, ForeignKey("person.id"))
    person = relationship(Person)


# Create an engine that stores data in the local directory"s
# sqlalchemy_example.db file.
# filename = "/tmp/sqlalchemy_example.db"
# engine = create_engine("sqlite:///{}".format(filename))

# for the next line to work you need the "pymysql" module installed

myDB = URL(
    username=None,
    password=None,
    port=None,
    drivername="mysql+pymysql",
    host="localhost",
    database="test",
    query={"read_default_file": os.path.expanduser("~/.my.cnf")},  # type: ignore
)
engine = create_engine(url=myDB)
# engine = create_engine("mysql+pymysql://localhost/test?charset=utf8")

# lets drop all tables in the database, whatever they are:
meta = sqlalchemy.MetaData()
meta.reflect(bind=engine)
meta.drop_all(bind=engine)

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
