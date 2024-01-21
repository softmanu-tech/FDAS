from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .models import Member

engine = create_engine('sqlite:///attendance.db')
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    encoding = Column(String)  # Store face encoding as a string
    phone_number = Column(String)
    residence = Column(String)
    age = Column(Integer)
    home_fellowship = Column(String)
    department = Column(String)
    attendances = relationship('Attendance', back_populates='member')

class Attendance(Base):
    __tablename__ = 'attendance'

    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('members.id'))
    marked_time = Column(String)  # Store timestamp as a string
    member = relationship('Member', back_populates='attendances')

# Create the database engine and tables
Base.metadata.create_all(engine)
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def get_members_data():
    Session = sessionmaker(bind=engine)
    session = Session()
    members_data = session.query(Member).all()
    session.close()
    return members_data
