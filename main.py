from telebot import TeleBot

bot = TeleBot('<TOKEN>', threaded=False)


@bot.message_handler()
def main(msg):
    bot.send_message(msg.chat.id, msg.text)
