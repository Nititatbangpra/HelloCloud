from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, CHAR, VARCHAR, Integer, String, Text, DateTime, Float, Boolean, PickleType

Base = declarative_base()
db_uri = 'sqlite:///work3.sqlite3'
engine = create_engine(db_uri, echo=False)

# class Students(Base):
#     _tablename_ = 'Students' 
#     student_id = Column(String(13),primary_key = True,nullable = True) 
#     f_name = Column(String(30),nullable = False) 
#     l_name = Column(String(30),nullable=False) 
#     e_mail = Column(String(50), nullable=False) 

#     def __repr__(self):
#         return '<User(student_id = {}, f_name = {}, l_name = {}, e_mail ={})>'.format(self.student_id, self.f_name, self.l_name, self.e_mail)
        

class Registration(Base):
    _tablename_ = 'Registration' 
    id = Column(Integer(), primary_key = True)
    student_id = Column(String(13)) 
    subject_id = Column(String(15),nullable = False) 
    year = Column(String(4),nullable=False) 
    semester = Column(String(1),nullable=False)  
    grade = Column(String(2))

def __repr__(self):
        return '<User(student_id = {}, subject_id = {}, year = {}, semester ={}, grade={})>'.format(self.student_id, self.subject_id, self.year , self.semester, self.grade)

# student_id = Column(String(15),primary_key = True) 
    #subject_name = Column(String(50),nullable = False) 
    #credit = Column(Integer(),nullable=False) 
    #teacher_id = Column(String(3),nullable=False) 

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

# user1 = Students(
#     student_id ='6406022620070',
#     f_name='Rawiporn',
#     l_name='Suamsiri',
#     e_mail ='6406022620070@kmutnb.ac.th'
# )

# user2 = Students(
#     student_id ='6406022620088',
#     f_name='Puntita',
#     l_name='Chaungchawna',
#     e_mail ='6406022620088@kmutnb.ac.th'
# )

# user3 = Students(
#     student_id ='6406022620061',
#     f_name='Mathawee',
#     l_name='Robkhob',
#     e_mail ='6406022620061@kmutnb.ac.th'
# )

regis1 = Registration(
    student_id ='6406022620070',
    subject_id='ADVANCED COMPUTER PROGRAMMIN',
    year='2565',
    semester ='1',
    grade = 'A'
)

regis11 = Registration(
    student_id ='6406022620070',
    subject_id='NETWORK ENGINEERING LABORATO',
    year='2565',
    semester ='1',
    grade = 'A'
)

regis2 = Registration(
    student_id ='6406022620088',
    subject_id='ADVANCED COMPUTER PROGRAMMIN',
    year='2565',
    semester ='1',
    grade = 'A'
)

regis22 = Registration(
    student_id ='6406022620088',
    subject_id='NETWORK ENGINEERING LABORATO',
    year='2565',
    semester ='1',
    grade = 'A'
)

regis3 = Registration(
    student_id ='6406022620061',
    subject_id='ADVANCED COMPUTER PROGRAMMIN',
    year='2565',
    semester ='1',
    grade = 'A'
)

regis33 = Registration(
    student_id ='6406022620061',
    subject_id='NETWORK ENGINEERING LABORATO',
    year='2565',
    semester ='1',
    grade = 'A'
)

session.add_all([regis1, regis11, regis2, regis22, regis3, regis33])
session.commit()