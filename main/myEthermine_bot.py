import telebot as tb
import main.constansts as const


bot = tb.TeleBot(const.token)


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = tb.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    user_markup.row('Address', 'Hashrate', 'Workers')
    bot.send_message(message.from_user.id, 'Nice to meet you!', reply_markup=user_markup)


@bot.message_handler(commands=['stop'])
def handle_stop(message):
    hide_markup = tb.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, 'Good bye', reply_markup=hide_markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Address':
        bot.send_message(message.from_user.id, 'Enter your Ethereum address')
        if message.text == 0xdad75804e6675c1dfb5c5948cd474595fdd14fdf:
            address = message.text
            bot.send_message(message.from_user.id, 'Well done!')
        else:
            bot.send_message(message.from_user.id, 'The address is wrong. It should look like: 0x742d35Cc6634C0532925a3b844Bc454e4438f44e')


bot.polling(none_stop=True, interval=0)




