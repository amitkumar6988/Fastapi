from sqlalchemy import create_engine
from sqlalchemy.orm import  DeclarativeBase,Mapped,mapped_column,Session
#database connection url
DATABASE_URL='postgresql://postgres:postgresql@localhost/fastapi'
#create database engine
engine=create_engine(DATABASE_URL)
#base class for orm models
class Base(DeclarativeBase):
    pass

#orm model
class HealthRecord(Base):
    __tablename__='health_records'
    id:Mapped[int]=mapped_column(primary_key=True)
    person_name:Mapped[str]=mapped_column(nullable=False)
    temperature:Mapped[float]=mapped_column(nullable=False)

#create the table
Base.metadata.create_all(engine)

#create one record

with Session(engine)as session:
    record=HealthRecord(
        person_name='amit',
        temperature=98.6
    )
    session.add(record)
    session.commit()
    session.refresh(record)

    print(record.id)



from fastapi import FastAPI

from pydantic import BaseModel

class HealthRecordSchema(BaseModel):
    person_name:str
    temperature:float



app=FastAPI()
#creating an api

@app.post('/health_records/')
async def create_health_record(record:HealthRecordSchema):
    with Session(engine)as session:
        record=HealthRecord(
            person_name=record.person_name,
            temperature=record.temperature

        )
        session.add(record)
        session.commit()
        session.refresh(record)
        return{'id':record.id,'person_name':record.person_name}

    