import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base_class import Base
import logging

# Amazon RDS MySQL connection
DATABASE_URL = "mysql+mysqlconnector://admin:masterpassword!23@fastapi-db.c1ogbrnwz4yy.us-east-1.rds.amazonaws.com:3306/fastapi-db"

# create engine
engine = create_engine(DATABASE_URL, pool_recycle=3600, pool_pre_ping=True)

# create sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

# allow logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
