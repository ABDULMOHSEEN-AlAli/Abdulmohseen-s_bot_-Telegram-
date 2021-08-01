# imports
from telegram.ext import *
import Responses as responses
from time import sleep

# Take the TAKEN from a hidden file
hidden_file = open("TAKEN.txt", "r")
TAKEN = hidden_file.readline()

# print a message that tell me if the put is starting
print("Pop! Starting...")


# define a command which have the (/) init
# This command will be in the beginning of the bot it will define it's self
def start_command(update, context):
    update.message.reply_text("Hi, I am Abdulmohseen's son this is the first try to make a bot.\n "
                              "\nIf you ask your self what I am doing type (commands) to get the answer.")


# This function is for ask for help
def help_command(update, context):
    update.message.reply_text("You need help? Do you think that I am a google?!")



# This function is for display the commands that in the bot
def commands_command(update, context):
    update.message.reply_text("Hmm well there are some function that I have in my code")
    sleep(2)
    update.message.reply_text("You can ask me about\n"
                              "what is the time now\n"
                              "also you can ask me for a help by typing \"/help\"\n"
                              "and also you can ask me who is me")


# This is for handle the message from user and try to talk with him
def handle_message(update, context):
    text = str(update.message.text).lower()
    response = responses.sample_responses(text)

    update.message.reply_text(response)


# this is for any error that happen
def error(update, context):
    print(f"Update {update} caused error {context.error}\n")


# main function to turn on the bot
def main():
    # make the updater which have the TAKEN init
    updater = Updater(TAKEN, use_context=True)
    # make a dispatcher in the updater
    dispatcher = updater.dispatcher

    # turn on the commands
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("commands", commands_command))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

    dispatcher.add_error_handler(error)

    # make the bot polling
    updater.start_polling()


# print this if the bot is setup
print("Data is ready")

main()
