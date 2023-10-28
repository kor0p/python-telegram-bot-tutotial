from telebot import TeleBot

bot = TeleBot('<TOKEN>')


@bot.message_handler()
def main(msg):
    bot.send_message(msg.chat.id, msg.text)


bot.infinity_polling()
