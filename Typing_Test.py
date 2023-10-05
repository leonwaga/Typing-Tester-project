# Import necessary libraries and modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, TypingTest, Score, session
import time
import hashlib
# Create an engine and a session
engine = create_engine("sqlite:///typing_test.db")
session = sessionmaker(bind=engine)
session = session()

def get_or_create_user():
    username = input("Enter your username: ")
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
# Query the database to see if a user with the same username exists, if not create a new user and add it to the database
    user = session.query(User).filter_by(username=username).first()

    if user is None:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user = User(username=username, email=email, password=hashed_password)
        session.add(user)
        session.commit()

    return user

def create_typing_test(user_id, duration_seconds):
    typing_test = TypingTest(user_id=user_id, duration_seconds=duration_seconds)
    session.add(typing_test)
    session.commit()
    return typing_test

def save_score(typing_test, user_id, words_per_minute):
    score = Score(typing_test_id=typing_test.id, user_id=user_id, typing_speed=words_per_minute)
    session.add(score)
    session.commit()

def get_user_input():
    return input("Start typing!: ")
                                  
def calculate_typing_speed(input_text, elapsed_time):
    words = input_text.split()
    word_count = len(words)
    words_per_minute = (word_count / elapsed_time) * 60
    return words_per_minute

def test():
    user = get_or_create_user()
    
    sample_text = "The quick brown fox jumps over the lazy dog. This sentence contains all the letters of the alphabet. It's a beautiful day outside, and the birds are singing. The sun is shining, and the sky is clear. Typing accurately and quickly is a valuable skill. Practice makes perfect!"
    print("Karibu to the Jiamini Typing Tester!")
    print("Below, you can see the text you'll be typing. Good luck!")
    print(sample_text)
    input("Press enter to begin...")

    start_time = time.time()
    user_input = get_user_input()
    end_time = time.time()

    elapsed_time = end_time - start_time
  
    words_per_minute = calculate_typing_speed(user_input, elapsed_time)

    print(f"Congrats!! Your typing speed is: {words_per_minute:.2f} words per minute")

    typing_test = create_typing_test(user.id, int(elapsed_time))
    save_score(typing_test,user.id, words_per_minute)

if __name__ == '__main__':
    test()