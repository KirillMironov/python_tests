import telebot as tb
import main.constansts as const
import requests

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
def start_handler(message):
    chat_id = message.from_user.id
    msg = bot.send_message(chat_id, 'Enter your Ethereum address')
    bot.register_next_step_handler(msg, ask_eth_address)


def ask_eth_address(message):
    chat_id = message.from_user.id
    address = message.text
    request = requests.get("https://balidator.io/api/ethereum/" + address).json()
    eth_validation = request['valid_address']

    if not eth_validation:
        msg = bot.send_message(chat_id, '''The address is wrong :(
It should look like: 0x742d35Cc6634C0532925a3b844Bc454e4438f44e''')
        bot.register_next_step_handler(msg, ask_eth_address)
    else:
        bot.send_message(chat_id, 'Well done!')


bot.polling(none_stop=True, interval=0)
