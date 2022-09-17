from telebot import TeleBot,custom_filters,types
from WhatsApp import whatsApp
from dotenv import load_dotenv
import os 
load_dotenv()
TOKEN = os.environ.get('TELE_TOKEN_WHATSAPP_BRIDGE')
bot = TeleBot(TOKEN)


SUDO_ID = "259127202"
chat ='-789422554'


def message_keyboard(name:str,phone:str,wamd_id:str):
    return types.InlineKeyboardMarkup(
        keyboard=[
            [
                types.InlineKeyboardButton(name,callback_data='k')
            ],
            [ 
                types.InlineKeyboardButton(phone,callback_data='e')
            ],
            [ 
                types.InlineKeyboardButton(str(wamd_id),callback_data=str('reply:')+str(232))
            ]
        ]
    )

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'this is a private WhatsApp bridge bot ')


@bot.message_handler(commands=['help'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)



@bot.message_handler(is_reply=True)
def start_filter(message):
    try:
        phone = str(message.json['reply_to_message']['reply_markup']['inline_keyboard'][1][0]['text'])
        whatsApp.send_message(phone,message.text)
    except:
        print('no')
        phone,message_id = str(message.json['reply_to_message']['text']).split(':')[1:]
        print(whatsApp.reply_message(phone,message_id,message.text))
        # bot.delete_message(message.chat.id,message.json['reply_to_message']['message_id'])




@bot.callback_query_handler(func=lambda c:str(c.data).split(':')[0] =='reply')
def reply_message(call):
    print(call)
    wamd_id = call.message.json['reply_markup']['inline_keyboard'][2][0]['text']
    m = types.ForceReply()
    phone= call.message.json['reply_markup']['inline_keyboard'][1][0]['text']
    print(wamd_id)
    reply_message = bot.send_message(call.message.chat.id,'Reply To this message:' + str(phone)+ ":"+str(wamd_id),reply_markup=m)

