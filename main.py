
from telegram.ext import Updater, MessageHandler, Filters


#this function reply to user 
def reply(update,text):
	update.message.reply_text(text)
	

def handle_text_message(update, context):
    text = update.message.text
    #user message is stored in text
    
    if "hi" in text:
    	reply(update,"hello")
    	
    #add more conditions as u need 


updater = Updater(token='7248395522:AAHSV_o2pjdK4M9D1tCT6XXnqLsgw1hLpEw', use_context=True)


dp = updater.dispatcher


text_handler = MessageHandler(Filters.text & ~Filters.command, handle_text_message)


dp.add_handler(text_handler)


updater.start_polling()


updater.idle()
