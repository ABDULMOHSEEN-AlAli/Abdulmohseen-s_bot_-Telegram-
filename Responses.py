# import
from datetime import datetime
from urllib import request
import json

### ---------------------------------------------------
# for joke
# define a url that will take a joke from
url = "http://official-joke-api.appspot.com/random_joke"
# make a request
r = request.urlopen(url)
# read the data init
data = r.read()
json_data = json.loads(data)


# define a class
class Joke:
    # set a setup and punchline
    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline

    # make the format
    def __str__(self) -> str:
        return f" {self.setup}, {self.punchline}"


# pass data inside the class
setup = json_data["setup"]
punchline = json_data["punchline"]
joke = Joke(setup, punchline)

### ----------------------------------------------


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

    help_word = ("help", "heelp")
    for word in help_word:
        if word in user_message:
            return "If you need help you have to write \n(/help)"

        # This is a function that will tell some jokes
        joke_word = ("/joke@ABDULMOHSEEN_bot", "joke", "/joke")
        if user_message in joke_word:
            return str(joke)
    else:
        print("")
