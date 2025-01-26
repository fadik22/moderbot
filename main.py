import telebot 
from config import token
import requests

from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
        bot.send_types(message.chat.id, str(pokemon.show_types()))
        bot.send_weight_height(message.chat.id, str(pokemon.show_weight_height()))
        bot.send_level(message.chat.id, str(pokemon.show_level()))
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")


@bot.message_handler(commands=['types'])
def types(message):
    bot.reply_to(message, "Пока в разработке...")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "Напиши /go для создания покемона")

@bot.message_handler(commands=['level'])
def level(message):
    bot.reply_to(message, "[+] Вы улучшили своего покемона")


bot.infinity_polling(none_stop=True)
