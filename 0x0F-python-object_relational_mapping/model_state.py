
#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine, Column, Integer, String, declarative_base

if __name__ == "__main__":
    engine = create_engine('mysql://user:password@localhost:3306/hbtn_0e_6_usa')
    Base.metadata.create_all(engine)
    
   class State(Base):
    __tablename__ = 'states'  # Table name

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


