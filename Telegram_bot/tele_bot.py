from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

list_job = ["1. Boss's Name", "2. Boss's School", "3. Boss' Telegram Id", "4. Boss's Age"]

def name(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'His name is: Dang Ngoc Quoc Bao')

def school(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'His school is: Da Nang University of Science and Technology School')

def telegram(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'His TeleGramID is: quocbaodang')

def age(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'His age is: 22')

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')
    update.message.reply_text(f'What information do you want look for about my boss?')
    for x in list_job:
        update.message.reply_text(f'{x}')
        

updater = Updater('5065360158:AAEWwdu8TF6v9DUvIGYtNhFg4Mck9JwKU38') # token cua bot


updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.dispatcher.add_handler(CommandHandler('1', name))
updater.dispatcher.add_handler(CommandHandler('2', school))
updater.dispatcher.add_handler(CommandHandler('3', telegram))
updater.dispatcher.add_handler(CommandHandler('4', age))


updater.start_polling()
updater.idle()