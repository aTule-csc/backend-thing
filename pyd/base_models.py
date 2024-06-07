from pydantic import BaseModel, Field

class SurveyBase(BaseModel):
    id: int = Field(None, gt=0,example=1)
    name: str = Field(...,max_length=255,example="Опрос1")
        
    class Config:
        orm_mode = True

class QuestionBase(BaseModel):
    id: int = Field(None, gt=0,example=1)
    question:str= Field(...,max_length=1023, example="Ваш вопрос")
    option1: str = Field(...,max_length=255,example="Опция1")
    option2: str = Field(...,max_length=255,example="Опция2")
    option3: str = Field(...,max_length=255,example="Опция3")

    class Config:
        orm_mode = True
