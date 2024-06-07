import uvicorn
from fastapi import FastAPI
from starlette.responses import JSONResponse
from pydantic import BaseModel
from routers import question_router, survey_router

app = FastAPI()

app.include_router(question_router)
app.include_router(survey_router)