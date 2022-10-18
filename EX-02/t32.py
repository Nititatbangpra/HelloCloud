from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType,VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
db_uri = 'sqlite:///Ex3.sqlite3'
engine = create_engine(db_uri, echo=False)

class Subjects(Base):
    _tablename_ = 'Subject'
    subject_id = Column(String(15), primary_key=True, nullable=False)
    subject_name = Column(String(50), nullable=False)
    creadit = Column(Integer(), nullable=False)
    teacher_id = Column(String(50), nullable=False)

    def __repr__(self):
        return '<user(suubject_id ={},subject_name={},creadit={},teacher_id={}) >'.format(self.subject_id,self.subject_name,self.creadit,self.teacher_id)
        



Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user = Subjects(
    subject_id='060233113',subject_name='ADVANCED COMPUTER PROGRAMMIN', creadit=3, teacher_id='AMK'
)
session.add_all([user])
session.commit()
print(user)