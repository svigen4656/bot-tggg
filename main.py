import requests
import json

bot=telebot.TeleBot('7283469638:AAEjjWdK8x2Gx5uoIuv4y0b2ucXFeyIjSnA')
API=('65481cf206631d6d7879b371298cd9f4')


@bot.message_handler(commands=['start'])
def start(message):
     bot.send_message(message.chat.id,'привет ,напиши название города')


@bot.message_handler(content_types=['text'])
def get_weater(message):
     city=message.text.strip().lower()
     res=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
     if res.status_code==200:
          data=json.loads(res.text)
          temp=data['main']['temp']
          feels_like = data['main']['feels_like']
          humidity = data['main']['humidity']
          wind_speed = data['wind']['speed']

          bot.reply_to(message, text=f'<b>Погода сейчас:</b>\n'
                                     f'🌡️ Температура: <b>{temp}°C</b>\n'
                                     f'🤔 Ощущается как: <b>{feels_like}°C</b>\n'
                                     f'💧 Влажность: <b>{humidity}%</b>\n'
                                     f'🌬️ Ветер: <b>{wind_speed} м/с</b>',
                       parse_mode='HTML')
     else:
          bot.reply_to(message, 'не правильно написан город')

bot.polling(none_stop=True)
"""f'Температура сейчас: {temp}°C,'
                                f'Ощущается как:{feels_like}°C,'
                                f'Влажность:{humidity}%,'
                                f'Ветер:{wind_speed}м/с,')"""