from models import User, TypingTest, Score, session
import time


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
    user_id = User.id
    
    sample_text = "Kenya, in East Africa, is famous for its stunning landscapes, wildlife, and diverse cultures. It's well known for places like Maasai Mara, offering a blend of natural beauty and vibrant heritage."
    print("Karibu to the Jiamini Typing Tester!")
    print("Your sample text is:")
    print(sample_text)
    input("Press enter to begin...")

    start_time = time.time()
    user_input = get_user_input()
    end_time = time.time()

    elapsed_time = end_time - start_time
  
    words_per_minute = calculate_typing_speed(user_input, elapsed_time)

    print(f"Congrats!! Your typing speed is: {words_per_minute:.2f} words per minute")

    typing_test = create_typing_test(user_id, int(elapsed_time))
    save_score(typing_test, user_id, words_per_minute)

if __name__ == '__main__':
    test()