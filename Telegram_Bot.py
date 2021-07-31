# imports
from telegram.ext import *
import Responses as responses
hidden_file= open("TAKEN.txt", "r")
TAKEN = hidden_file.readline()
print("Pop! Starting...")

# define a command


def start_command(update, context):
    update.message.reply_text("Type something")


def help_command(update, context):
    update.message.reply_text("You need help? what are you talking about?? am I google?")


def handel_message(update, context):
    text = str(update.message.text).lower()
    response = responses.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(TAKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text, handel_message))

    dispatcher.add_error_handler(error)

    updater.start_polling()


main()
