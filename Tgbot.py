import requests
phonee = 0
i = 0
params = 0
#k = { 
import telebot

def b0mb3r():
	global phonee, g
	params = {
	    "phone_code": "7",
   	 "phone": phonee,
    	"number_of_cycles": "1"
	}
	print(params)
	request = requests.post("http://127.0.0.1:8080/attack/start", data=params)
	print(request.json())
	g = request.json()
	return g

bot = telebot.TeleBot('1045933830:AAFfArZoVBBdSUheZKWMF8uo5ZuWwdw8vOg')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Я согласен')

@bot.message_handler(commands=['start'])
def start_message(message):
	global i
	i += 1
	print(i)
	bot.send_message(message.chat.id, 'Привет, продолжая пользоваться ботом, ты подтверждаешь, что номер принадлежит тебе и сообщения используются только ради проверки!', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
	global phonee
	if message.text.lower() == "я согласен":
		bot.send_message(message.chat.id, 'Введи номер телефона без +7')
	else:
		phonee = message.text
		print(phonee)
		bot.send_message(message.chat.id, 'Номер +7{0} принят'.format(phonee))
		bot.send_message(message.chat.id, 'Начинаю атаку')
		bot.send_message(619219532, "{0} использует бота и отправляет на номер {1}".format(message.chat.id, phonee))
		b0mb3r()
		if g == phonee:
			bot.send_message(message.chat.id, 'Произошла ошибка')
		bot.send_message(message.chat.id, 'Атака закончена')

    
    	

bot.polling()
