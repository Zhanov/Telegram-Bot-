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
    if response.status_code == 200:
        data = json.loads(response.text)
        temp = data["main"]["temp"]
        bot.reply_to(messege, f'Сейчас погода в {city}: {temp}')
        
        if temp > 8.0:
            image = 'sunny.png'
        else:
            image = 'cloudy.png'

        file = open('images./' + image, 'rb')
        bot.send_photo(messege.chat.id, file)
    else:
        bot.reply_to(messege, "Такого города не существует")


bot.polling(non_stop=True)