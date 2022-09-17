from email import header
from flask import request
import requests 
import json 
import os 
from dotenv import load_dotenv
load_dotenv()



whatsapp_token = os.environ.get('WHATSAPP_TOKEN')

def welcome_smledate(phone:str,name:str,date:str)-> dict:
    url = 'https://graph.facebook.com/v13.0/108022628653202/messages'
    message = {
            "messaging_product": "whatsapp",
            "to": phone ,
            "type": "template",
            "template": {
                "name": "welcome_smledate",
                "language": {
                    "code": "ar"
                },
                "components": [
            {
                "type": "body",
                "parameters": [
                {
                    "type": "text",
                    "text": str(name)
                },
                {
                    "type": "text",
                    "text": str(date)
                }
                ]
            }
            ]
            }
        }
    headers = {
        'Authorization': 'Bearer '+whatsapp_token,
        'Content-Type': 'application/json'
        }
    r = requests.post(url, headers=headers, json=message)
    return r.json() 




def send_message(phone:str,message:str):
    url = 'https://graph.facebook.com/v13.0/108022628653202/messages'
    m = {
        "messaging_product": "whatsapp",
        "to": phone,
        "type": "text",
        "text": {
            "body": message
        }
    }
    headers = {
        'Authorization': 'Bearer '+whatsapp_token,
        'Content-Type': 'application/json'
        }
    r = requests.post(url, headers=headers, json=m)
    return r.json() 



def reply_message(phone:str,wamid_id:str,message:str):
    url = 'https://graph.facebook.com/v13.0/108022628653202/messages'
    headers = {
        'Authorization': 'Bearer '+whatsapp_token,
        'Content-Type': 'application/json'
        }
    m = {
        "messaging_product": "whatsapp",
        "context": {
            "message_id": wamid_id
        },
        "to": phone,
        "type": "text",
        "text": {
            "body": message
        }
        }
    r = requests.post(url, headers=headers, json=m)
    return r.json() 







