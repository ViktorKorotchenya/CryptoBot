from telebot import TeleBot
from pycoingecko import CoinGeckoAPI
from datetime import datetime

api = CoinGeckoAPI()
token = '5486629501:AAGSlyLjFB_LCS_K9psCiM73eJRKC76qJvM'

bot = TeleBot(token=token)
base_currency = 'usd'
current_datetime = datetime.now().date()



@bot.message_handler(commands=['start'])
def crypto_price(message):
    btc = api.get_price(ids='bitcoin', vs_currencies=base_currency)['bitcoin'][base_currency]
    btc_24h = api.get_coin_by_id('bitcoin')['market_data']['price_change_percentage_24h']
    btc_7d = api.get_coin_by_id('bitcoin')['market_data']['price_change_percentage_7d']
    eth = api.get_price(ids='ethereum', vs_currencies=base_currency)['ethereum'][base_currency]
    eth_24h = api.get_coin_by_id('ethereum')['market_data']['price_change_percentage_24h']
    eth_7d = api.get_coin_by_id('ethereum')['market_data']['price_change_percentage_7d']
    gods = api.get_price(ids='gods-unchained', vs_currencies=base_currency)['gods-unchained'][base_currency]
    gods_24h = api.get_coin_by_id('gods-unchained')['market_data']['price_change_percentage_24h']
    gods_7d = api.get_coin_by_id('gods-unchained')['market_data']['price_change_percentage_7d']
    imx = api.get_price(ids='immutable-x', vs_currencies=base_currency)['immutable-x'][base_currency]
    imx_24h = api.get_coin_by_id('immutable-x')['market_data']['price_change_percentage_24h']
    imx_7d = api.get_coin_by_id('immutable-x')['market_data']['price_change_percentage_7d']

    bot.send_message(message.chat.id,
                     f'*Курсы с CoinGecko на текущее время ({current_datetime.day}.{current_datetime.month}.{current_datetime.year})*\n'
                     '\n'
                     f'_Цена токена:_ *BTC = {btc}$*\n      (изменения за 24h = {btc_24h:.2f} %)\n      (изменения за 7d = {btc_7d:.2f} %)\n'
                     '\n'
                     f'_Цена токена:_ *ETH = {eth}$*\n      (изменения за 24h = {eth_24h:.2f} %)\n      (изменения за 7d = {eth_7d:.2f} %)\n'
                     '\n'
                     f'_Цена токена:_ *IMX = {imx}$*\n      (изменения за 24h = {imx_24h:.2f} %)\n      (изменения за 7d = {imx_7d:.2f} %)\n'
                     '\n'
                     f'_Цена токена:_ *GODS = {gods:.3f}$*\n     (изменения за 24h = {gods_24h:.2f} %)\n     (изменения за 7d = {gods_7d:.2f} %)',
                     parse_mode="Markdown")


if __name__ == '__main__':
    bot.polling()
