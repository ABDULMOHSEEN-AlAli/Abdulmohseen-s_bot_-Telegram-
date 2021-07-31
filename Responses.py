# import
from datetime import datetime


# define a function that take input from user and return some strings
def sample_responses(input_text):
    user_message = str(input_text).lower()

    hello_word = ("hello", "hi", "?!", "?")
    for word in hello_word:
        if word in user_message:
            return "Hi? did you call me??"

    who_word = ("who are you", "who is you", "who")
    for word in who_word:
        if word in user_message:
            return "Really! you don't know who is me?\n I am your uncle"

    time_words = ("time", "time?")
    for word in time_words:
        if word in user_message:
            now = datetime.now()
            data_time = now.strftime("%d/%m/%y, %H:%M:%S")
            return str(data_time)

    else:
        return "Hah? English please"
