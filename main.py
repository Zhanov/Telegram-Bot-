import telebot
import requests
import json 

bot = telebot.TeleBot('7446225545:AAEulIZcxS6kc41QqYHHmk7l9dnLKJ_63tM')
API = '5b4874614f4c7bfc878d18ec472ddf3f'

# откликание на стартовое сообщение 
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "Салем ")
# работа с апи сервисом
@bot.message_handler(content_types=['text'])
def get_wheather(messege):
    city = messege.text.strip().lower()
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(response.text)
    bot.reply_to(messege, f'Сейчас погода в {city}: {data["main"]["temp"]}')

bot.polling(non_stop=True)