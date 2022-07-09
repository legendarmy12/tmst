import re, os, random, asyncio, html,configparser,pyrogram, subprocess, requests, time, traceback, logging, telethon, csv, json, sys
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from asyncio.exceptions import TimeoutError
from pyrogram.errors import SessionPasswordNeeded, FloodWait, PhoneNumberInvalid, ApiIdInvalid, PhoneCodeInvalid, PhoneCodeExpired, UserNotParticipant
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from telethon.client.chats import ChatMethods
from csv import reader
from telethon.sync import TelegramClient
from telethon import functions, types, TelegramClient, connection, sync, utils, errors
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError, PhoneCodeInvalidError, PhoneNumberBannedError, PhoneNumberInvalidError, UserBannedInChannelError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError,  UserBannedInChannelError, UserAlreadyParticipantError,  UserPrivacyRestrictedError, ChatAdminRequiredError
from telethon.sessions import StringSession
from pyrogram import Client,filters
from pyromod import listen
from sql import add_user, query_msg
from support import users_info
from datetime import datetime, timedelta,date
import csv
#add_user= query_msg= users_info=0
if not os.path.exists('./sessions'):
    os.mkdir('./sessions')
if not os.path.exists(f"Users/1669178360/phone.csv"):
   os.mkdir('./Users')
   os.mkdir(f'./Users/1669178360')
   open(f"Users/1669178360/phone.csv","w")
if not os.path.exists('data.csv'):
    open("data.csv","w")
APP_ID = 7099462
API_HASH = "a34660c224f9ab893e35ca6da9175cc5"
BOT_TOKEN = "Enter you bot token"
UPDATES_CHANNEL = "Infinity_botz"
OWNER= [5032100535,1953656325]
PREMIUM= ["Infinity_botz"]
app = pyrogram.Client("app", api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

with open("data.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",", lineterminator="\n")
    next(rows, None)
    ishan=[]
    for row in rows:
        d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
        r = datetime.strptime("2021-12-01", '%Y-%m-%d') - datetime.strptime("2024-11-03", '%Y-%m-%d')
        if d<=r:
            PREMIUM.append(int(row[1]))

# ------------------------------- Subscribe --------------------------------- #
async def Subscribe(lel, message):
   update_channel = UPDATES_CHANNEL
   if update_channel:
      try:
         user = await app.get_chat_member(update_channel, message.chat.id)
         if user.status == "kicked":
            await app.send_message(chat_id=message.chat.id,text="Sorry Sir, You are Banned. Contact My [Support Group](https://t.me/TSF_CH4TTING).", parse_mode="markdown", disable_web_page_preview=True)
            return 1
      except UserNotParticipant:
         await app.send_message(chat_id=message.chat.id, text="**Please Join My Updates Channel To Use Me!\n and click on to Check /start**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🤖 Join Updates Channel 🤖", url=f"https://t.me/{update_channel}")]]), parse_mode="markdown")
         return 1


# ------------------------------- Start --------------------------------- #
@app.on_message(filters.private & filters.command(["start"]))
async def start(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   id = message.from_user.id
   user_name = '@' + message.from_user.username if message.from_user.username else None
   await add_user(id, user_name)
   but = InlineKeyboardMarkup([[InlineKeyboardButton("Login✅", callback_data="Login"), InlineKeyboardButton("Adding💯", callback_data="Adding") ],[InlineKeyboardButton("Phone⚙️", callback_data="Edit"), InlineKeyboardButton("PhoneSee💕", callback_data="Ish")],[InlineKeyboardButton("Phone Remove⚙️", callback_data="Remove"), InlineKeyboardButton("AdminPannel", callback_data="Admin")]])
   await message.reply_text(f"**Hi** {message.from_user.first_name} **!\n\nI'm a Scraper Bot \nMade for doing Scraping,\nUsing PyroGram Client.\n\nMade with ❤️ By @ITZ_ROCKSTAR**", reply_markup=but)


text = """
This Bot Maintained By 
@ITZ_ROCKSTAR
"""
print(text)
print("Tsf  Adding Started Sucessfully........")
app.run()
