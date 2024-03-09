import telebot


# Token for the bot
TOKEN = 'YOUR API KEY'

# Create a bot object
bot = telebot.TeleBot(TOKEN)

me = bot.get_me()

print(me.username)
# Handler for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the bot!")

  


# Handler for all other messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


# Start the bot
bot.polling()