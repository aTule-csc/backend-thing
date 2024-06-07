from pydantic import BaseModel, Field
from typing import List

class SurveyCreate(BaseModel):
    name: str = Field(...,max_length=255,example="Опрос1")
    


    class Config:
        orm_mode = True

class QuestionCreate(BaseModel):
    question: str = Field(...,max_length=1023)
    option1: str = Field(...,max_length=255,example="Опция1")
    option2: str = Field(...,max_length=255,example="Опция2")
    option3: str = Field(...,max_length=255,example="Опция3")
    survey_id : int = Field(...)


    class Config:
        orm_mode = True