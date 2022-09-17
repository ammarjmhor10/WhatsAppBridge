from .Model import Model
import json
from Tele import tele
from WhatsApp import whatsApp
import requests

bot = tele.bot
chat = tele.chat





def FileID(message:dict):
    mess = Model(**message)
    name = mess.entry[0].changes[0].value.contacts[0].profile.name
    phone = mess.entry[0].changes[0].value.messages[0].from_
    wamd_id = mess.entry[0].changes[0].value.messages[0].id
    if mess.entry[0].changes[0].value.messages[0].type == 'text':
        text =  mess.entry[0].changes[0].value.messages[0].text.body
        bot.send_message(chat,text,reply_markup=tele.message_keyboard(str(name),str(phone),str(wamd_id)))
    if mess.entry[0].changes[0].value.messages[0].type == 'image':
        file_id = mess.entry[0].changes[0].value.messages[0]
        id_file = file_id.image.id
        binary_file = send_file_telegram(id_file)
        bot.send_photo(chat,binary_file,reply_markup=tele.message_keyboard(str(name),str(phone),str(wamd_id)))
    if mess.entry[0].changes[0].value.messages[0].type == 'audio':
        file_id = mess.entry[0].changes[0].value.messages[0]
        id_file = file_id.audio.id
        binary_file = send_file_telegram(id_file)
        bot.send_audio(chat,binary_file,reply_markup=tele.message_keyboard(str(name),str(phone),str(wamd_id)))
    if mess.entry[0].changes[0].value.messages[0].type == 'sticker':
        file_id = mess.entry[0].changes[0].value.messages[0]
        id_file = file_id.sticker.id
        binary_file = send_file_telegram(id_file)
        bot.send_sticker(chat,binary_file,reply_markup=tele.message_keyboard(str(name),str(phone),str(wamd_id)))

# file_id = FileID(im)
def send_file_telegram(file_id:str)->None:
    
    url = 'https://graph.facebook.com/v13.0/' + str(file_id)

    headers = {
            'Authorization': 'Bearer '+whatsApp.whatsapp_token
            }

    r = requests.get(url,headers=headers) 
    print(r.status_code)
    r = requests.get(r.json()['url'],headers=headers) 
    print(r.status_code)
    return r.content
    
