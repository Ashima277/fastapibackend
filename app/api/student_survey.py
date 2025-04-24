from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.student_survey import (
    StudentSurveyRead,
    StudentSurveyCreate,
)
from app.services.student_survey_service import (
    get_all_surveys,
    get_survey_by_id,
    create_survey,
    update_survey,
    delete_survey,
)
from app.db.session import get_db

router = APIRouter(
    prefix="/api/surveys",
    tags=["Student Surveys"]
)


@router.get("/", response_model=List[StudentSurveyRead])
def read_surveys(db: Session = Depends(get_db)):
    return get_all_surveys(db)


@router.get("/{survey_id}", response_model=StudentSurveyRead)
def read_survey(survey_id: int, db: Session = Depends(get_db)):
    survey = get_survey_by_id(db, survey_id)
    if survey is None:
        raise HTTPException(status_code=404, detail="Survey not found")
    return survey


@router.post("/", response_model=StudentSurveyRead, status_code=201)
def create_new_survey(survey: StudentSurveyCreate, db: Session = Depends(get_db)):
    return create_survey(db, survey)


@router.put("/{survey_id}", response_model=StudentSurveyRead)
def update_existing_survey(survey_id: int, updated: StudentSurveyCreate, db: Session = Depends(get_db)):
    return update_survey(db, survey_id, updated)


@router.delete("/{survey_id}", status_code=204)
def delete_existing_survey(survey_id: int, db: Session = Depends(get_db)):
    delete_survey(db, survey_id)
    return
