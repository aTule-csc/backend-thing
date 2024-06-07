from sqlalchemy import Numeric, Table, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Survey(Base):
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question = Column(String(1023))
    option1 = Column(String(255))
    option2 = Column(String(255))
    option3 = Column(String(255))
    survey_id = Column(Integer, ForeignKey("surveys.id"))
    surveys = relationship("Survey", backref="questions")