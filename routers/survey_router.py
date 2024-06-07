from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
from database import get_db
import pyd

router = APIRouter(
    prefix="/survey",
    tags=["survey"],
)

@router.get('/survey', response_model=List[pyd.SurveyBase])

async def get_surveys(db:Session=Depends(get_db)):
    sur_db = db.query(models.Survey).all()
    return sur_db

@router.post('/add_survey', response_model=pyd.SurveyCreate)

async def add_survey(survey_input:pyd.SurveyCreate, db:Session=Depends(get_db)):
    sur_db=db.query(models.Survey).filter(models.Survey.name == survey_input.name).first()
    if sur_db:
        raise HTTPException(400,detail='This survey already exists')
    sur_db = models.Survey()
    sur_db.name = survey_input.name
    db.add(sur_db)
    db.commit()
    return sur_db

@router.put('/change_survey/{survey_id}', response_model=pyd.SurveyCreate)

async def change_survey(survey_input: pyd.SurveyCreate, survey_id = int,db:Session=Depends(get_db)):
    sur_db=db.query(models.Survey).filter(models.Survey.id == survey_id).first()
    if not sur_db:
        raise HTTPException(404,detail='This survey is not found')
    sur_db.name = survey_input.name
    db.commit()
    return sur_db

@router.delete('/survey/delete/{survey_id}')

async def delete_survey(survey_id = int, db:Session=Depends(get_db)):
    sur_db=db.query(models.Survey).filter(models.Survey.id == survey_id).first()
    if not sur_db:
        raise HTTPException(404,detail='This survey is not found')
    db.delete(sur_db)
    db.commit()
    return 'success'