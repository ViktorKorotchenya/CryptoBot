from telebot import TeleBot
from pycoingecko import CoinGeckoAPI

api = CoinGeckoAPI()
token = '5486629501:AAGSlyLjFB_LCS_K9psCiM73eJRKC76qJvM'


bot = TeleBot(token=token)
base_currency = 'usd'


@bot.message_handler(content_types=['text'])
def crypto_price(message):
    crypto_id = message.text
    price = api.get_price(ids=crypto_id, vs_currencies=base_currency)
    if price:
        price = price[crypto_id][base_currency]
    else:
        bot.send_message(message.chat.id, 'Токен не найден')
        return 

    bot.send_message(message.chat.id, f'Цена токена: {crypto_id} = {price}$')


if __name__ == '__main__':
    bot.polling()
