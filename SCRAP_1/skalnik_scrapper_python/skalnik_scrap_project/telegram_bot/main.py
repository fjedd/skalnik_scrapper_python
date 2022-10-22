import constants as keys
from telegram.ext import *
import responses as R

print('Bot started')

def starter(update, context):
    update.message.reply_text('Hello')
 
def send_items(update, context):
    response = R.response_items()
    update.message.reply_text(response)
       
def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler('start', starter))
    dp.add_handler(CommandHandler('go', send_items))
    
    updater.start_polling()
    updater.idle()
    
main()