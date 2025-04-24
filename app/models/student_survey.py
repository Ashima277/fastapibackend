from sqlalchemy import Column, String, Integer, Date, Enum, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import ENUM
from typing import List
import enum

from app.db.base_class import Base

class LikedMostEnum(str, enum.Enum):
    STUDENTS = "STUDENTS"
    LOCATION = "LOCATION"
    CAMPUS = "CAMPUS"
    ATMOSPHERE = "ATMOSPHERE"
    DORMS = "DORMS"
    SPORTS = "SPORTS"

class InterestSourceEnum(str, enum.Enum):
    FRIENDS = "FRIENDS"
    TELEVISION = "TELEVISION"
    INTERNET = "INTERNET"
    OTHER = "OTHER"

class RecommendationLikelihoodEnum(str, enum.Enum):
    VERY_LIKELY = "VERY_LIKELY"
    LIKELY = "LIKELY"
    UNLIKELY = "UNLIKELY"

class StudentSurvey(Base):
    __tablename__ = "student_surveys"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    street_address = Column(String(100), nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    zip = Column(String(10), nullable=False)
    telephone = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)
    date_of_survey = Column(Date, nullable=True)
    liked_most = Column(JSON, nullable=False)
    interest_source = Column(ENUM(InterestSourceEnum), nullable=False)
    recommendation_likelihood = Column(ENUM(RecommendationLikelihoodEnum), nullable=False)
    comment = Column(String(500), nullable=False)
