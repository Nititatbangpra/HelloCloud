


from sqlalchemy import Column,Integer, String ,Text,Boolean,Float, DateTime,PickleType
from sqlalchemy.ext.declarative import declarative_base




Base = declarative_base()

class Member(Base):
    __table__ = 'member'
    id = Column(Integer,primary_key = True , nullable = False)
    name = Column(String(100), nullable = False)
    description = Column(Text, nullable = True)
    join_date  = Column(DateTime, nullable = False)
    vip  = Column(Boolean , nullable = False)
    number = Column(Float , nullable = False)


    def __repr__(self) :
        return '<UserModel model {}>'.format(self.id)


        