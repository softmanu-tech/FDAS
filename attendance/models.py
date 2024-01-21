



from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database_setup import Base

class Member(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    phone_number = Column(String(20), nullable=False)
    residence = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    attendances = relationship('Attendance', back_populates='member')

class Attendance(Base):
    __tablename__ = 'attendance'
    id = Column(Integer, primary_key=True)
    marked_time = Column(DateTime, default=datetime.now)
    face_id = Column(String(100), ForeignKey('members.id'))
    member = relationship('Member', back_populates='attendances')
