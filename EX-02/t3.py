from tkinter.tix import INTEGER
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, CHAR, VARCHAR, Integer, String, Text, DateTime, Float, Boolean, PickleType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
db_uri = 'sqlite:///Ex2.sqlite3'
engine = create_engine(db_uri, echo=False)

Base = declarative_base()



class Subjects(Base):
    _tablename_ = 'Subject'
    subject_id = Column(VARCHAR(15), primary_key=True, nullable=False)
    subject_name = Column(VARCHAR(50), nullable=False)
    creadit = Column(Integer(), nullable=False)
    teacher_id = Column(VARCHAR(50), nullable=False)

Sj1 = Subjects(subject_id='060233113',subject_name='ADVANCED COMPUTER PROGRAMMIN', creadit=3, teacher_id='AMK')
Sj2 = Subjects(subject_id='060233201',subject_name='NETWORK ENGINEERING LABORATO', creadit=3, teacher_id='WKN')
Sj3 = Subjects(subject_id='060233112',subject_name='DATA ENGINEERING',             creadit=3,teacher_id='STS')


Session = sessionmaker(bind=engine)
session = Session()
session.add_all([Sj1,Sj2,Sj3])
session.commit()