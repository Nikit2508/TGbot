import telebot
import random
import os
import requests
from password import generator 


def get_duck_image_url():    
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        return data['data'][0]['attributes']['posterImage']['original']


    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7306983058:AAE8ZChmNm2MTFf8BPM4SULcC0qYdgUvtrc")
images_Eng = os.listdir('images/Eng')
images_Rus = os.listdir('images/Rus')
images_Ecology = os.listdir('images/Ecology')
facts = ['''Большое тихоокеанское мусорное пятно — это скопление мусора антропогенного происхождения в северной части Тихого океана. Оно расположено между 135°—155° западной долготы и 35°—42° северной широты. 4

Мусорное пятно можно условно разделить на две части: западная, расположенная недалеко от Японии, и восточная, которая дрейфует между штатами США Гавайи и Калифорния. Отходы дрейфуют между этими двумя участками, используя тёплые и холодные океанические течения. 2

Точный размер пятна определить сложно, так как мусор постоянно перемещается — учёные и исследователи называют цифры от 700 тысяч до 15 миллионов квадратных километров. 2

Основная часть Большого тихоокеанского мусорного пятна — это не сплошной плот из плавающего мусора, а скорее крошечные кусочки пластика, находящиеся в верхних слоях морской воды. 3''', '''5.5 млн человек умирают каждый год из-за проблем, связанных с водой.

''']
materials = {'пластик':'до 700 лет','пакет':'до 500 лет','банка':'до 100 лет'}

@bot.message_handler(commands=['bot'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока!")

@bot.message_handler(commands=['commands'])
def send_bye(message):
    bot.reply_to(message, "1.bot 2.bye 3.generate 4.mem 5.heh")
    

@bot.message_handler(commands=['generate'])
def send_goodbye(message):
    elements_list = message.text.split()
    if len(elements_list) > 1:
        number = int(elements_list[1])
        if 10 <= number <= 100:
            password = generator(number)
        else:
            password = generator(10)
    else:
        password = generator(10)
    bot.reply_to(message, f"password:{password}")


@bot.message_handler(commands=['util'])
def send_util(message):
    elements_list = message.text.split()
    if len(elements_list) > 1:
        material = elements_list[1]
        if material in materials:
            bot.reply_to(message, materials[material])
        else:
            bot.reply_to(message, 'Данный по этому материалу мы не дописали((')
    else:
        bot.reply_to(message, 'Вы забыли написать материал')



@bot.message_handler(commands=['mem.eng'])
def send_mem(message):
    g = random.choice(images_Eng)
    with open(f'images/{g}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['mem.rus'])
def send_mem(message):
    g = random.choice(images_Rus)
    with open(f'images/{g}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['fact'])
def send_fact(message):
    g = random.randint(0, len(facts)-1)
    with open(f'images/Ecology/{images_Ecology[g]}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)
    bot.reply_to(message, facts[g])


@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)
# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')
    
# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
bot.polling()

