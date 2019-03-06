from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

updater = Updater(token='641604340:AAGkF513VeMNQTGrb9rZSfLKTlDPSV5-xl8',
        use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
            text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def echo(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
            text=update.message.text)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.message.chat_id,
            text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

def unknown(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
            text="yo wat u tok about man i dun und")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(caps_handler)

updater.start_polling()
