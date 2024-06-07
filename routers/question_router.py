from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
from database import get_db
import pyd

router = APIRouter(
    prefix="/question",
    tags=["question"],
)

@router.get('/question', response_model=List[pyd.QuestionBase])

async def get_question(db:Session=Depends(get_db)):
    que_db = db.query(models.Question).all()
    return que_db

@router.post('/add_question', response_model=pyd.QuestionBase)

async def add_question(que_input: pyd.QuestionCreate, db:Session=Depends(get_db)):
    que_db = models.Question()
    que_db.question = que_input.question
    que_db.option1 = que_input.option1
    que_db.option2 = que_input.option2
    que_db.option3 = que_input.option3
    db.add(que_db)
    db.commit()
    return que_db

@router.put('/change_question/{question_id}', response_model=pyd.QuestionCreate)

async def change_question(que_input: pyd.QuestionCreate, que_id = int,db:Session=Depends(get_db)):
    que_db = db.query(models.Question).filter(models.Question.id == que_id).first()
    if not que_db:
        raise HTTPException(404,detail='This question is not found')
    que_db.question = que_input.question
    que_db.option1 = que_input.option1
    que_db.option2 = que_input.option2
    que_db.option3 = que_input.option3
    que_db.survey_id = que_input.survey_id
    db.commit()
    return que_db

@router.delete('/question/delete/{question_id}')

async def delete_question(question_id =int, db:Session=Depends(get_db)):
    que_db = db.query(models.Question).filter(models.Question.id == question_id).first()
    if not que_db:
        raise HTTPException(404,detail='This question is not found')
    db.delete(que_db)
    db.commit()
    return 'success'
