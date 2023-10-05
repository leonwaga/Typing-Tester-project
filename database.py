from sqlalchemy import create_engine
from models import User, TypingTest, Score, sessionmaker

engine = create_engine("sqlite:///typingtester.db")
session = sessionmaker(bind=engine)
session = session()