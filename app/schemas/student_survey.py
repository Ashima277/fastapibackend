from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date
from app.models.student_survey import (
    LikedMostEnum,
    InterestSourceEnum,
    RecommendationLikelihoodEnum,
)


class StudentSurveyBase(BaseModel):
    first_name: str
    last_name: str
    street_address: str
    city: str
    state: str
    zip: str
    telephone: str
    email: EmailStr
    date_of_survey: Optional[date]
    liked_most: List[LikedMostEnum]
    interest_source: InterestSourceEnum
    recommendation_likelihood: RecommendationLikelihoodEnum
    comment: str


class StudentSurveyCreate(StudentSurveyBase):
    pass


class StudentSurveyRead(StudentSurveyBase):
    id: int

    class Config:
        orm_mode = True
