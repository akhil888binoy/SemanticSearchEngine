from src.database.database import Base
from sqlalchemy import String
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text, ForeignKey , UUID , JSON

class Note(Base):
    __tablename__="notes"
    id = Column(UUID , primary_key=True , nullable=False) 
    title = Column(String , nullable=False)
    content = Column(String , nullable=False)
    embedding = Column(JSON , nullable=False )
    created_at = Column(TIMESTAMP , nullable=False)
