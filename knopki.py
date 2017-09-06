import telepot, time, subprocess
from telepot.namedtuple import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)


#вот тут мы формируем кнопочки
    bot.sendMessage(chat_id, "Выполнено",
                            reply_markup=ReplyKeyboardMarkup(
                               keyboard = [

        [KeyboardButton(text="Нет минут"), KeyboardButton(text="Одна минута")],
        [KeyboardButton(text="Звук на ПК"), KeyboardButton(text="Звук на ТВ")],
        [KeyboardButton(text="Кнопка 1"), KeyboardButton(text="Кнопка 2"), KeyboardButton(text="Кнопка 3")],
        [KeyboardButton(text="Выключить ПК")]
                                                                        
                                          ]
                            ))


    if (content_type == 'text'):
        command = msg['text']
        print ('Got command: %s' % command)

        if  'Нет минут' in command:
            p = subprocess.Popen(cmd0, shell=True) 
            bot.sendMessage(chat_id, "Комп не уйдёт в спящий режим")

        if  'Одна минута' in command:
            p = subprocess.Popen(cmd1, shell=True)
            bot.sendMessage(chat_id, "Комп уйдёт в спящий режим через одну минуту простоя")

          
        if  '/off' in command:
            #p = subprocess.Popen(shut, shell=True)
            bot.sendMessage(chat_id, "Выключаю комп")

        if  'Звук на ПК' in command:
            p = subprocess.Popen(soundpc, shell=True)
            bot.sendMessage(chat_id, "Звук на столе")

        if  'Звук на ТВ' in command:
             p = subprocess.Popen(soundtv, shell=True)
             bot.sendMessage(chat_id, "Звук на телике")


bot = telepot.Bot('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
cmd0 = 'Powercfg -setactive 46a2d4bc-148e-4bb2-af30-38579c57e732'
cmd1 = 'Powercfg -setactive 2e977135-68b3-45e4-a9d4-2085b6389840'
shut = 'shutdown -s'
soundpc = 'C:\SSD_v3.exe\SSD.exe 7777hidden'
soundtv = 'C:\SSD_v3.exe\SSD.exe 7771hidden'

bot.message_loop(handle)

while 1:
    time.sleep(20)