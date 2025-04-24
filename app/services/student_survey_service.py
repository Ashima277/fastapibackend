from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.student_survey import StudentSurvey
from app.schemas.student_survey import StudentSurveyCreate


def get_all_surveys(db: Session):
    return db.query(StudentSurvey).all()


def get_survey_by_id(db: Session, survey_id: int):
    return db.query(StudentSurvey).filter(StudentSurvey.id == survey_id).first()


def create_survey(db: Session, survey_data: StudentSurveyCreate):
    survey = StudentSurvey(**survey_data.dict())
    db.add(survey)
    db.commit()
    db.refresh(survey)
    return survey


def update_survey(db: Session, survey_id: int, updated_data: StudentSurveyCreate):
    survey = db.query(StudentSurvey).filter(StudentSurvey.id == survey_id).first()
    if not survey:
        raise HTTPException(status_code=404, detail=f"Survey not found with ID: {survey_id}")

    for field, value in updated_data.dict().items():
        setattr(survey, field, value)

    db.commit()
    db.refresh(survey)
    return survey


def delete_survey(db: Session, survey_id: int):
    survey = db.query(StudentSurvey).filter(StudentSurvey.id == survey_id).first()
    if not survey:
        raise HTTPException(status_code=404, detail=f"Survey not found with ID: {survey_id}")

    db.delete(survey)
    db.commit()
