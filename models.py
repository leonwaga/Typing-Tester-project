from sqlalchemy import Column, Float, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(Integer, nullable=False)
    

    typing_tests = relationship('TypingTest', back_populates='user')
    scores = relationship('Score', back_populates='user')

class TypingTest(Base):
    __tablename__ = 'typing_tests'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    duration_seconds = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='typing_tests')
    scores = relationship('Score', back_populates='typing_test')


class Score(Base):
    __tablename__ = 'scores'

    id = Column(Integer, primary_key=True)
    typing_speed = Column(Float)
    typing_test_id = Column(Integer, ForeignKey('typing_tests.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    typing_test = relationship('TypingTest', back_populates='scores')
    user = relationship('User', back_populates='scores')


engine = create_engine('sqlite:///typing_test.db')
session = sessionmaker(bind=engine)
session = session()
Base.metadata.create_all(engine)