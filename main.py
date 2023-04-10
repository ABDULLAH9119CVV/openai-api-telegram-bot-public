#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from pytz import timezone
from telebot import types
from telebot import util
from sys import platform
import requests
import telebot
import random
import openai
import shutil
import pydub
import time
import sys
import os

from botapiconfig import openaiapi, telegrambotapi, session_key

openai.api_key = openaiapi
bot = telebot.TeleBot(telegrambotapi)

last_messages_chatgpt = {}
last_messages_dalletwo = {}
last_whisper = {}

start_time = time.time()

botname = "avencoreschatgpt_bot"

timebot = "Europe/Moscow"

stickerstart = "stickers/hjkhjkhjkuiy.gif"

adminsid = ['872108002', '1087968824']

q,w,e,r,t,y,u,i,o,p  = ['dhfdhdfhf.webp', 'fgjgfjfgj.webp', 'fhfdhfdh.webp', 'fjfgjurturt.webp', 'hdfhdfhdfh.webp', 'rtutrurtutru.webp', 'sticker.webp', 'sticker-animenazi.webp', 'trutrutrur.webp', 'urturturtutru.webp', 'rutrutrutrurt.webp', 'jfjfgjfgjg.webp', 'fjgfjfgjgfj.webp', 'jfgjturtur.webp', 'rtutrurtjfgj.webp', 'urturutrurt.webp']
numbers = (q,w,e,r,t,y,u,i,o,p)

def mainstarter():
    @bot.message_handler(commands=['start'])
    def start_message(message):
        if message.chat.type != 'private':
            if message.text.lower() == "/start":
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                markdown = """🚨 *ПРЕДУПРЕЖДЕНИЕ*: Пожалуйста, обратите внимание, что команда `/start` доступна только в *личных сообщениях* с данным ботом. Использование этой команды в групповых чатах или каналах может вызвать непредвиденные ошибки и нарушения конфиденциальности.

🙏 Пожалуйста, следуйте этому правилу, чтобы избежать любых проблем. Если у вас есть какие-либо вопросы или проблемы, пожалуйста, обратитесь к нашей документации или напишите в техническую поддержку. Спасибо за понимание!"""
                markup.add(button1)
                markup.add(button2)
                bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

            elif message.text.lower() == f"/start@{botname}":
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                markdown = f"""🚨 *ПРЕДУПРЕЖДЕНИЕ*: Пожалуйста, обратите внимание, что команда `/start@{botname}` доступна только в *личных сообщениях* с данным ботом. Использование этой команды в групповых чатах или каналах может вызвать непредвиденные ошибки и нарушения конфиденциальности.

🙏 Пожалуйста, следуйте этому правилу, чтобы избежать любых проблем. Если у вас есть какие-либо вопросы или проблемы, пожалуйста, обратитесь к нашей документации или напишите в техническую поддержку. Спасибо за понимание!"""
                markup.add(button1)
                markup.add(button2)
                bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")
            return
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.InlineKeyboardButton("Мои проекты")
        button2 = types.InlineKeyboardButton("Мои чаты")
        button3 = types.InlineKeyboardButton("Поддержать автора монетой")
        button4 = types.InlineKeyboardButton("Техническая поддержка")
        button5 = types.InlineKeyboardButton("Исходный код")
        button6 = types.InlineKeyboardButton("Статус бота")
        markup.add(button1, button2, button3, button4, button5, button6)
        random_number = random.choice(numbers)
        sticker = open(f"stickers/{random_number}", "rb")
        bot.send_sticker(message.chat.id, sticker)
        markdown = """Привет друг! 👋\n\nДанный телеграм бот основан на технологии ChatGPT, DALLE-2 и Whisper. 💻\n\nВы можете добавить данного бота к себе в чат и так же полноценно использовать, но учтите, что ограничения бота будут действовать на всех участников беседы сразу. 🤖\n\n*Что такое ChatGPT?* ❓\nChatGPT - это модель языкового обработки, разработанная OpenAI. Она была обучена на множестве текстов и может генерировать тексты, отвечать на вопросы и выполнять другие задачи обработки языка. 💡\n\n*Что такое DALLE-2?* ❓\nDALLE-2 - это продвинутая модель глубокого обучения, созданная OpenAI, которая может генерировать изображения и текстовые описания на основе заданного текстового ввода. 💡\n\n*Что такое Whisper?* ❓\nWhisper - это модель, которая позволяет переводить голосовое сообщение в текст.\n\n*Как задать вопрос ChatGPT?* ❓\nЛегко! Просто напиши /chatgpt ВАШ-ЗАПРОС 😉\n\n*Как получить картинку от DALLE-2?* ❓\nЛегко! Просто напиши /dalle2 ВАШ-ЗАПРОС 😉\n\n*Как воспользоваться Whisper?* ❓\nЛегко! Просто отправь или перешли голосовое сообщение боту 😉"""
        bot.send_message(message.chat.id, markdown, reply_markup=markup, parse_mode="Markdown")

    @bot.message_handler(commands=['dalle2'])
    def dalletwo(message):
        if message.text.lower() == f"/dalle2@{botname}":
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
            button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
            markdown = f"""🚫 *Ошибка:* Команда `/dalle2@{botname}` оказалась пустой, запрос не может быть выполнен.

Пожалуйста, укажите текст после команды `/dalle2@{botname}`, чтобы DALLE-2 мог обработать ваш запрос. Если проблема сохраняется, обратитесь к документации или к нашей службе поддержки. 🤖"""
            markup.add(button1)
            markup.add(button2)
            bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")
        if message.text.lower() == "/dalle2":
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
            button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
            markdown = """🚫 *Ошибка*: Команда `/dalle2` оказалась пустой, запрос не может быть выполнен.

Пожалуйста, укажите текст после команды `/dalle2`, чтобы DALLE-2 мог обработать ваш запрос. Если проблема сохраняется, обратитесь к документации или к нашей службе поддержки. 🤖"""
            markup.add(button1)
            markup.add(button2)
            bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")
        elif len(message.text.split(maxsplit=1)[1]) > 500:
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
            button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
            markdown = "🚫 *Сообщение слишком длинное! Максимальная длина сообщения - 500 символов.*"
            markup.add(button1)
            markup.add(button2)
            bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")
        elif message.chat.id in last_messages_dalletwo and time.time() - last_messages_dalletwo[message.chat.id] < 30:
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
            button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
            markdown = "🚫 *Слишком быстро! Пожалуйста, подождите 30 секунд перед отправкой нового сообщения.*"
            markup.add(button1)
            markup.add(button2)
            bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")
        else:

            if message.from_user.id in last_messages_dalletwo:
                elapsed_time = time.time() - last_messages_dalletwo[message.from_user.id]
                if elapsed_time < 30:
                    time.sleep(30 - elapsed_time)

            msg = bot.reply_to(message, "🔎 Идет загрузка, подождите...")

            try:
                response = openai.Image.create(
                    prompt=message.text,
                    n=1,
                    size="1024x1024"
                )

                username = message.from_user.first_name
                output = response['data'][0]['url']
                inputuser = message.text.split(maxsplit=1)[1]
                bot.delete_message(message.chat.id, msg.message_id)
                bot.reply_to(message, text="✅ Ответ получен!")


                bot.send_message(message.chat.id, text=f"👨 *Запрос отправлен пользователем*: `{username}`\n\n🎈 *Айди сообщения*: `{message.message_id}`\n\n🤔 *Запрос*: `{inputuser}`\n\n👾 *Ответ от DALLE-2*: [картинка от DALLE-2]({output})", parse_mode="Markdown")


                message_date = datetime.fromtimestamp(message.date, timezone(timebot))
                message_date_string = message_date.strftime('%Y-%m-%d %H:%M:%S')

                f = open("chatlog.txt", "a")
                f.writelines('---------------------------------------------------------------------------')
                f.writelines('\n')
                f.writelines('Model: DALLE-2')
                f.writelines('\n')
                f.writelines(f'ChatID: {message.chat.id}')
                f.writelines('\n')
                f.writelines(f'MessageID: {message.message_id}')
                f.writelines('\n')
                f.writelines(f'UserID: {message.from_user.id}')
                f.writelines('\n')
                f.writelines(f'Username: {message.from_user.username}')
                f.writelines('\n')
                f.writelines(f'Date and Time: {message_date_string}')
                f.writelines('\n')
                f.writelines(f'Prompt: {message.text.split(maxsplit=1)[1]}')
                f.writelines('\n')
                f.writelines(f'AI reply: {output}')
                f.writelines('\n')
                f.writelines('---------------------------------------------------------------------------')
                f.writelines('\n\n')
                f.close

            except openai.error.Timeout as e:
                print(e)
                bot.delete_message(message.chat.id, msg.message_id)
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                markup.add(button1)
                markup.add(button2)
                markdown = f"❌ *OpenAI API не смог обработать запрос*: `{e}`"
                bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

            except openai.error.APIError as e:
                print(e)
                bot.delete_message(message.chat.id, msg.message_id)
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                markup.add(button1)
                markup.add(button2)
                markdown = f"❌ *OpenAI API вернул ошибку API*: `{e}`"
                bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

            except openai.error.APIConnectionError as e:
                print(e)
                bot.delete_message(message.chat.id, msg.message_id)
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                markup.add(button1)
                markup.add(button2)
                markdown = f"❌ *Невозможно подключиться к OpenAI API*: `{e}`"
                bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

            except openai.error.InvalidRequestError as e:
                print(e)
                bot.delete_message(message.chat.id, msg.message_id)
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                markup.add(button1)
                markup.add(button2)
                markdown = f"❌ *OpenAI API запрос оказался недействительным*: `{e}`"
                bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

            except openai.error.AuthenticationError as e:
                print(e)
                bot.delete_message(message.chat.id, msg.message_id)
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                markup.add(button1)
                markup.add(button2)
                markdown = f"❌ *OpenAI API запрос не был авторизован*: `{e}`"
                bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

            except openai.error.PermissionError as e:
                print(e)
                bot.delete_message(message.chat.id, msg.message_id)
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                markup.add(button1)
                markup.add(button2)
                markdown = f"❌ *Запрос OpenAI API не был разрешен*: `{e}`"
                bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

            except openai.error.RateLimitError as e:
                print(e)
                bot.delete_message(message.chat.id, msg.message_id)
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                markup.add(button1)
                markup.add(button2)
                markdown = f"❌ *Превышены лимиты OpenAI API*: `{e}`"
                bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

            last_messages_dalletwo[message.chat.id] = time.time()

    @bot.message_handler(commands=['chatgpt'])
    def chatgpt(message):
        if message.text.lower() == f"/chatgpt@{botname}":
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
            button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
            markdown = f"""🚫 *Ошибка*: Команда `/chatgpt@{botname}` оказалась пустой, запрос не может быть выполнен.

Пожалуйста, укажите текст после команды `/chatgpt@{botname}`, чтобы ChatGPT мог обработать ваш запрос. Если проблема сохраняется, обратитесь к документации или к нашей службе поддержки. 🤖"""
            markup.add(button1)
            markup.add(button2)
            bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")
        if message.text.lower() == "/chatgpt":
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
            button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
            markdown = """🚫 *Ошибка*: Команда `/chatgpt` оказалась пустой, запрос не может быть выполнен.

Пожалуйста, укажите текст после команды `/chatgpt`, чтобы ChatGPT мог обработать ваш запрос. Если проблема сохраняется, обратитесь к документации или к нашей службе поддержки. 🤖"""
            markup.add(button1)
            markup.add(button2)
            bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")
        elif len(message.text.split(maxsplit=1)[1]) > 500:
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
            button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
            markdown = "🚫 *Сообщение слишком длинное! Максимальная длина сообщения - 500 символов.*"
            markup.add(button1)
            markup.add(button2)
            bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")
        elif message.chat.id in last_messages_chatgpt and time.time() - last_messages_chatgpt[message.chat.id] < 30:
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
            button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
            markdown = "🚫 *Слишком быстро! Пожалуйста, подождите 30 секунд перед отправкой нового сообщения.*"
            markup.add(button1)
            markup.add(button2)
            bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")
        else:

            if message.from_user.id in last_messages_chatgpt:
                elapsed_time = time.time() - last_messages_chatgpt[message.from_user.id]
                if elapsed_time < 30:
                    time.sleep(30 - elapsed_time)

            msg = bot.reply_to(message, "🔎 Идет загрузка, подождите...")

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": message.text}],
                )

                total_tokens = response['usage']['total_tokens']
                output = response["choices"][0]["message"]["content"]
                username = message.from_user.first_name
                inputuser = message.text.split(maxsplit=1)[1]
                bot.delete_message(message.chat.id, msg.message_id)
                bot.reply_to(message, text="✅ Ответ получен!")


                if 'output' in locals():
                    splitted_text = util.smart_split(output, chars_per_string=2000)
                    for text in splitted_text:
                        bot.send_message(message.chat.id, text=f"👨 Запрос отправлен пользователем: {username}\n\n🎈 Айди сообщения: {message.message_id}\n\n💰 Затрачено токенов: {total_tokens}\n\n🤔 Запрос: {inputuser}\n\n👾 Ответ от ChatGPT: {text}")


                message_date = datetime.fromtimestamp(message.date, timezone(timebot))
                message_date_string = message_date.strftime('%Y-%m-%d %H:%M:%S')

                f = open("chatlog.txt", "a")
                f.writelines('---------------------------------------------------------------------------')
                f.writelines('\n')
                f.writelines('Model: ChatGPT')
                f.writelines('\n')
                f.writelines(f'Tokens used: {total_tokens}')
                f.writelines('\n')
                f.writelines(f'ChatID: {message.chat.id}')
                f.writelines('\n')
                f.writelines(f'MessageID: {message.message_id}')
                f.writelines('\n')
                f.writelines(f'UserID: {message.from_user.id}')
                f.writelines('\n')
                f.writelines(f'Username: {message.from_user.username}')
                f.writelines('\n')
                f.writelines(f'Date and Time: {message_date_string}')
                f.writelines('\n')
                f.writelines(f'Prompt: {message.text.split(maxsplit=1)[1]}')
                f.writelines('\n')
                f.writelines(f'AI reply: {output}')
                f.writelines('\n')
                f.writelines('---------------------------------------------------------------------------')
                f.writelines('\n\n')
                f.close

            except openai.error.Timeout as e:
                print(e)
                bot.delete_message(message.chat.id, msg.message_id)
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                markup.add(button1)
                markup.add(button2)
                markdown = f"❌ *OpenAI API не смог обработать запрос*: `{e}`"
                bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

            except openai.error.APIError as e:
                print(e)
                bot.delete_message(message.chat.id, msg.message_id)
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                markup.add(button1)
                markup.add(button2)
                markdown = f"❌ *OpenAI API вернул ошибку API*: `{e}`"
                bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

            except openai.error.APIConnectionError as e:
                print(e)
                bot.delete_message(message.chat.id, msg.message_id)
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                markup.add(button1)
                markup.add(button2)
                markdown = f"❌ *Невозможно подключиться к OpenAI API*: `{e}`"
                bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

            except openai.error.InvalidRequestError as e:
                print(e)
                bot.delete_message(message.chat.id, msg.message_id)
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                markup.add(button1)
                markup.add(button2)
                markdown = f"❌ *OpenAI API запрос оказался недействительным*: `{e}`"
                bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

            except openai.error.AuthenticationError as e:
                print(e)
                bot.delete_message(message.chat.id, msg.message_id)
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                markup.add(button1)
                markup.add(button2)
                markdown = f"❌ *OpenAI API запрос не был авторизован*: `{e}`"
                bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

            except openai.error.PermissionError as e:
                print(e)
                bot.delete_message(message.chat.id, msg.message_id)
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                markup.add(button1)
                markup.add(button2)
                markdown = f"❌ *Запрос OpenAI API не был разрешен*: `{e}`"
                bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

            except openai.error.RateLimitError as e:
                print(e)
                bot.delete_message(message.chat.id, msg.message_id)
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                markup.add(button1)
                markup.add(button2)
                markdown = f"❌ *Превышены лимиты OpenAI API*: `{e}`"
                bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

            last_messages_chatgpt[message.chat.id] = time.time()

    @bot.message_handler(commands=['log'])
    def logsend(message):
        if message.chat.type == 'private':
            if str(message.from_user.id) in adminsid:
                if os.path.isfile("chatlog.txt"):
                    markup = types.InlineKeyboardMarkup()
                    button1 = types.InlineKeyboardButton("✅ Да, отправь мне лог!", callback_data="yesdownload")
                    button2 = types.InlineKeyboardButton("❌ Нет, я передумал!", callback_data="delerrorandmsguser")
                    markup.add(button1)
                    markup.add(button2)
                    bot.send_message(message.chat.id, text="🤔 *Вы уверены, что хотите скачать логи?*", reply_markup=markup, parse_mode="Markdown")
                else:
                    markup = types.InlineKeyboardMarkup()
                    button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                    button2 = types.InlineKeyboardButton("Скрыть уведомление и ваше сообщение", callback_data="delerrorandmsguser")
                    markup.add(button1)
                    markup.add(button2)
                    bot.send_message(message.chat.id, text="❌ *Увы, но на данный момент нету логов!*", reply_markup=markup, parse_mode="Markdown")
            else:
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                button2 = types.InlineKeyboardButton("Скрыть уведомление и ваше сообщение", callback_data="delerrorandmsguser")
                markup.add(button1)
                markup.add(button2)
                bot.send_message(message.chat.id, text="❌ *Данная команда доступна только администрации!*", reply_markup=markup, parse_mode="Markdown")
        elif message.chat.type in ['group', 'supergroup']:
            if message.text.lower() == "/log":
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                markdown = """🚨 *ПРЕДУПРЕЖДЕНИЕ*: Пожалуйста, обратите внимание, что команда `/log` доступна только в *личных сообщениях* с данным ботом. Использование этой команды в групповых чатах или каналах может вызвать непредвиденные ошибки и нарушения конфиденциальности.

🙏 Пожалуйста, следуйте этому правилу, чтобы избежать любых проблем. Если у вас есть какие-либо вопросы или проблемы, пожалуйста, обратитесь к нашей документации или напишите в техническую поддержку. Спасибо за понимание!"""
                markup.add(button1)
                markup.add(button2)
                bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

            elif message.text.lower() == f"/log@{botname}":
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                markdown = f"""🚨 *ПРЕДУПРЕЖДЕНИЕ*: Пожалуйста, обратите внимание, что команда `/log@{botname}` доступна только в *личных сообщениях* с данным ботом. Использование этой команды в групповых чатах или каналах может вызвать непредвиденные ошибки и нарушения конфиденциальности.

🙏 Пожалуйста, следуйте этому правилу, чтобы избежать любых проблем. Если у вас есть какие-либо вопросы или проблемы, пожалуйста, обратитесь к нашей документации или напишите в техническую поддержку. Спасибо за понимание!"""
                markup.add(button1)
                markup.add(button2)
                bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

    @bot.message_handler(commands=['id'])
    def logsend(message):
        message_date = datetime.fromtimestamp(message.date, timezone(timebot))
        message_date_string = message_date.strftime('%Y-%m-%d %H:%M:%S')
        if message.chat.type == 'private':
            if str(message.from_user.id) in adminsid:
                markdown = f"*Ваш айди*: `{message.from_user.id}`\n*Айди чата*: `{message.chat.id}`\n*Ваш username*: `{message.from_user.username}`\n*Дата и время на сервере*: `{message_date_string}`\n*Являетесь ли вы Администратором*: `Да`"
                bot.send_message(message.chat.id, text=markdown, parse_mode="Markdown")
            else:
                markdown = f"*Ваш айди*: `{message.from_user.id}`\n*Айди чата*: `{message.chat.id}`\n*Ваш username*: `{message.from_user.username}`\n*Дата и время на сервере*: `{message_date_string}`\n*Являетесь ли вы Администратором*: `Да`"
                bot.send_message(message.chat.id, text=markdown, parse_mode="Markdown")
        elif message.chat.type in ['group', 'supergroup']:
            if str(message.from_user.id) in adminsid:
                markdown = f"*Ваш айди*: `{message.from_user.id}`\n*Айди беседы*: `{message.chat.id}`\n*Ваш username*: `{message.from_user.username}`\n*Дата и время на сервере*: `{message_date_string}`\n*Являетесь ли вы Администратором*: `Да`"
                bot.send_message(message.chat.id, text=markdown, parse_mode="Markdown")
            else:
                markdown = f"*Ваш айди*: `{message.from_user.id}`\n*Айди беседы*: `{message.chat.id}`\n*Ваш username*: `{message.from_user.username}`\n*Дата и время на сервере*: `{message_date_string}`\n*Являетесь ли вы Администратором*: `Да`"
                bot.send_message(message.chat.id, text=markdown, parse_mode="Markdown")


    @bot.message_handler(content_types=['voice'])
    def save_voice(message):
        if message.chat.type == 'private':
            if message.chat.id in last_whisper and time.time() - last_whisper[message.chat.id] < 30:
                markup = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                button2 = types.InlineKeyboardButton("Скрыть уведомление и ваше сообщение", callback_data="delerrorandmsguser")
                markup.add(button1)
                markup.add(button2)
                bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")
            else: 
                
                if message.voice.file_id in last_whisper:
                    elapsed_time = time.time() - last_whisper[message.voice.file_id]
                    if elapsed_time < 30:
                        time.sleep(30 - elapsed_time)

                msg = bot.reply_to(message, "🔎 Идет загрузка, подождите...")

                file_info = bot.get_file(message.voice.file_id)
                file_path = file_info.file_path

                downloaded_file = bot.download_file(file_path)

                try:
                    os.mkdir("voices")
                except:
                    pass

                file_name = 'voice{}.ogg'.format(message.message_id)
                file_path = os.path.join('voices', file_name)

                with open(file_path, 'wb') as f:
                    f.write(downloaded_file)
                    f.close()

                try:
                    sound = pydub.AudioSegment.from_file(f"voices/voice{message.message_id}.ogg", format="ogg")
                    sound.export(f"voices/voice{message.message_id}.mp3", format="mp3")

                    try:
                        os.remove("voices/voicelove.mp3")
                    except:
                        pass

                    one = f"voices/voice{message.message_id}.mp3"
                    two = "voices/voicelove.mp3"
                    shutil.copyfile(one, two)
                    fileaudio = open("voices/voicelove.mp3", "rb")
                    response = openai.Audio.transcribe("whisper-1", fileaudio)
                    fileaudio.close()

                    username = message.from_user.first_name
                    bot.delete_message(message.chat.id, msg.message_id)
                    bot.reply_to(message, text="✅ Ответ получен!")
                    sendmsg = response["text"]


                    if 'sendmsg' in locals():
                        splitted_text = util.smart_split(sendmsg, chars_per_string=2000)
                        for text in splitted_text:
                                bot.send_message(message.chat.id, text=f"👨 *Запрос отправлен пользователем*: `{username}`\n\n🎈 *Айди сообщения*: `{message.message_id}`\n\n👾 *Ответ от Whisper*: {text}", parse_mode="Markdown")


                    message_date = datetime.fromtimestamp(message.date, timezone(timebot))
                    message_date_string = message_date.strftime('%Y-%m-%d %H:%M:%S')

                    f = open("chatlog.txt", "a")
                    f.writelines('---------------------------------------------------------------------------')
                    f.writelines('\n')
                    f.writelines('Model: Whisper')
                    f.writelines('\n')
                    f.writelines(f'ChatID: {message.chat.id}')
                    f.writelines('\n')
                    f.writelines(f'MessageID: {message.message_id}')
                    f.writelines('\n')
                    f.writelines(f'UserID: {message.from_user.id}')
                    f.writelines('\n')
                    f.writelines(f'Username: {message.from_user.username}')
                    f.writelines('\n')
                    f.writelines(f'Date and Time: {message_date_string}')
                    f.writelines('\n')
                    f.writelines(f'AI reply: {sendmsg}')
                    f.writelines('\n')
                    f.writelines('---------------------------------------------------------------------------')
                    f.writelines('\n\n')
                    f.close

                    shutil.rmtree("voices")

                except openai.error.Timeout as e:
                    shutil.rmtree("voices")
                    print(e)
                    bot.delete_message(message.chat.id, msg.message_id)
                    markup = types.InlineKeyboardMarkup()
                    button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                    button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                    markup.add(button1)
                    markup.add(button2)
                    markdown = f"❌ *OpenAI API не смог обработать запрос*: `{e}`"
                    bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

                except openai.error.APIError as e:
                    shutil.rmtree("voices")
                    print(e)
                    bot.delete_message(message.chat.id, msg.message_id)
                    markup = types.InlineKeyboardMarkup()
                    button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                    button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                    markup.add(button1)
                    markup.add(button2)
                    markdown = f"❌ *OpenAI API вернул ошибку API*: `{e}`"
                    bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

                except openai.error.APIConnectionError as e:
                    shutil.rmtree("voices")
                    print(e)
                    bot.delete_message(message.chat.id, msg.message_id)
                    markup = types.InlineKeyboardMarkup()
                    button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                    button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                    markup.add(button1)
                    markup.add(button2)
                    markdown = f"❌ *Невозможно подключиться к OpenAI API*: `{e}`"
                    bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

                except openai.error.InvalidRequestError as e:
                    shutil.rmtree("voices")
                    print(e)
                    bot.delete_message(message.chat.id, msg.message_id)
                    markup = types.InlineKeyboardMarkup()
                    button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                    button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                    markup.add(button1)
                    markup.add(button2)
                    markdown = f"❌ *OpenAI API запрос оказался недействительным*: `{e}`"
                    bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

                except openai.error.AuthenticationError as e:
                    shutil.rmtree("voices")
                    print(e)
                    bot.delete_message(message.chat.id, msg.message_id)
                    markup = types.InlineKeyboardMarkup()
                    button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                    button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                    markup.add(button1)
                    markup.add(button2)
                    markdown = f"❌ *OpenAI API запрос не был авторизован*: `{e}`"
                    bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

                except openai.error.PermissionError as e:
                    shutil.rmtree("voices")
                    print(e)
                    bot.delete_message(message.chat.id, msg.message_id)
                    markup = types.InlineKeyboardMarkup()
                    button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                    button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                    markup.add(button1)
                    markup.add(button2)
                    markdown = f"❌ *Запрос OpenAI API не был разрешен*: `{e}`"
                    bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

                except openai.error.RateLimitError as e:
                    shutil.rmtree("voices")
                    print(e)
                    bot.delete_message(message.chat.id, msg.message_id)
                    markup = types.InlineKeyboardMarkup()
                    button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
                    button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
                    markup.add(button1)
                    markup.add(button2)
                    markdown = f"❌ *Превышены лимиты OpenAI API*: `{e}`"
                    bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

                last_whisper[message.chat.id] = time.time()

        elif message.chat.type in ['group', 'supergroup']:
            pass

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.chat.type != 'private':
            return
        if message.text.lower() == "мои проекты":
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Группа VK", url="https://vk.com/chatgptcontent")
            button2 = types.InlineKeyboardButton("Telegram канал", url="https://t.me/hzfnews")
            markup.add(button1, button2)
            markdown = """*Подпишись на нашу группу ВК и Telegram канал 📢*

Мы будем рады видеть вас в нашей группе ВКонтакте и канале в Telegram! 🔍 Там вы сможете узнать о наших новостях, анонсах и мероприятиях, а также общаться с другими пользователями. 💬

Подпишитесь на оба канала, чтобы быть в курсе всех новостей и обновлений, связанных с данным ботом. 🤖

Благодарим за использование нашего бота! 🙏"""
            bot.send_message(message.chat.id, markdown, reply_markup=markup, parse_mode="Markdown")

        elif message.text.lower() == "поддержать автора монетой":
            markdown = """ *Поддержать автора монетой 💰*

Если вам нравится использовать этот бот и вы хотите поддержать наш проект, мы будем очень благодарны за любую помощь.

Вы можете сделать донат нашему проекту через следующие платежные системы:

*QIWI*: [Нажми на меня](https://qiwi.com/n/AVENCORESDONATE) 💳
*Сбер*: `2202 2050 7215 4401` 💵
*ВТБ*: `2200 2404 1001 8580` 💶

Ваша поддержка поможет нам продолжать развивать этот бот и добавлять новые функции. 🚀

Благодарим за использование нашего бота и за вашу поддержку! 🙏"""
            bot.send_message(message.chat.id, markdown, parse_mode="Markdown")

        elif message.text.lower() == "техническая поддержка":
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Я в VK", url="https://vk.com/avencores")
            button2 = types.InlineKeyboardButton("Я в Telegram", url="https://t.me/avencores")
            markup.add(button1, button2)
            markdown = """*Техническая поддержка 🛠️*

Если у вас возникли проблемы с использованием этого бота или у вас есть вопросы по поводу его функциональности, наша команда технической поддержки всегда готова помочь вам.

Вы можете связаться с нами через наши страницы в социальных сетях, для этого просто нажмите на кнопки снизу. 👇

Мы гарантируем быстрый и профессиональный ответ на все ваши запросы. 💬

Благодарим за использование нашего бота! 🙏"""
            bot.send_message(message.chat.id, markdown, reply_markup=markup, parse_mode="Markdown")

        elif message.text.lower() == "статус бота":
            url = "https://api.openai.com/dashboard/billing/credit_grants"
            headers = {
                "Content-Type": "application/json",
                f"Authorization": f"Bearer {session_key}"
            }

            response = requests.get(url, headers=headers)
            data = response.json()
            balance = data['total_used']
            totalbalance = data['total_granted']
            totalavailable = data['total_available']

            pyver = sys.version.split()[0]
            current_time = time.time()
            uptime = int(current_time - start_time)
            uptime_str = f"{uptime // (24 * 3600)} день(-ней), {uptime // 3600 % 24} час(-ов), {uptime // 60 % 60} минут(-а), {uptime % 60} секунд(-а)"
            markdown = datetime.now().strftime(f"""*Бот работает в штатном режиме.* 🤖\n
*Время на сервере*: `%H:%M:%S` ⏰
*Дата на сервере*: `%d.%m.%y` 📅

*Общий баланс токена*: 💸`{totalbalance}`
*Использовано баланса токена*: 💸`{balance}`
*Осталось денег на балансе токена*: 💸`{totalavailable}`

*Платформа на сервере*: `{platform}` 💻
*Версия Python на сервере*: `{pyver}` 🐍
*Аптайм бота*: `{uptime_str}` ⌛""")
            bot.send_message(message.chat.id, markdown, parse_mode="Markdown")

        elif message.text.lower() == "исходный код":
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("GitHub Page", url="https://github.com/AvenCores/openai-api-telegram-bot-public")
            button2 = types.InlineKeyboardButton("Full GNU GPL V3", url="https://www.gnu.org/licenses/quick-guide-gplv3.ru.html")
            markdown = """⚠️ *Предупреждение* ⚠️

Данный телеграм бот распространяется под лицензией GNU GPL 3. Это означает, что вы имеете право свободно использовать, распространять и изменять исходный код этого бота, при условии, что все ваши изменения также будут распространяться под той же лицензией. 🆓

Мы просим вас уважать авторские права и не использовать этот бот в незаконных целях. Если вы не согласны с условиями GNU GPL 3, пожалуйста, прекратите использование этого бота немедленно. ❌

Спасибо за понимание и уважение к правам авторов! 🙏"""
            markup.add(button1, button2)
            bot.send_message(message.chat.id, markdown, reply_markup=markup, parse_mode="Markdown")

        elif message.text.lower() == "мои чаты":
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Telegram Chat", url="https://t.me/+MDOUaUZzWlEwNjRi")
            button2 = types.InlineKeyboardButton("VK Chat", url="https://vk.me/join/VqYKejk4a/QQvIXq6DhW6huxyAJ/A7cCiD4=")
            markdown = """📣 *Присоединяйтесь к нашему Telegram и VK чату!* 🚀

👥 Здесь вы найдете единомышленников, с которыми сможете обсуждать интересные темы, делиться опытом и получать полезные советы.

💬 Общение с людьми, которые разделяют ваши интересы, может стать настоящей находкой! А еще у нас вы сможете научиться новым навыкам и расширить свой кругозор.

👉 Присоединяйтесь к нам прямо сейчас, чтобы не пропустить ни одного интересного обсуждения! 💻📱"""
            markup.add(button1, button2)
            bot.send_message(message.chat.id, markdown, reply_markup=markup, parse_mode="Markdown")


        else:
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
            button2 = types.InlineKeyboardButton("Скрыть уведомление и запрос", callback_data="delerrorandmsguser")
            markdown = """❌ Ошибка! Команда не найдена 🤔

Чтобы узнать, как использовать этот Telegram бот, отправьте сообщение /start 👉👀

Это поможет вам ознакомиться со всеми доступными функциями и начать работу с ботом. Если у вас возникнут какие-либо вопросы, не стесняйтесь обращаться в техническая поддержку нашего Telegram бота 🤗

Спасибо за ваше понимание! 🙏"""
            markup.add(button1)
            markup.add(button2)
            bot.reply_to(message, text=markdown, reply_markup=markup, parse_mode="Markdown")

    @bot.callback_query_handler(func=lambda call: call.data == "dellthiserror")
    def dellthiserror(call):
        bot.answer_callback_query(callback_query_id=call.id, text="Уведомление скрыто")
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

    @bot.callback_query_handler(func=lambda call: call.data == "delerrorandmsguser")
    def delerrorandmsguser(call):
        bot.answer_callback_query(callback_query_id=call.id, text="Уведомление скрыто")
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)

    @bot.callback_query_handler(func=lambda call: call.data == "delerrorandmsguserbot")
    def delerrorandmsguserbot(call):
        bot.answer_callback_query(callback_query_id=call.id, text="Уведомление скрыто")
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 2)

    @bot.callback_query_handler(func=lambda call: call.data == "yesdownload")
    def yesdownload(call):
        try:
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            bot.answer_callback_query(callback_query_id=call.id, text="Лог был отправлен")
            with open('chatlog.txt', 'rb') as log_file:
                bot.send_document(chat_id=call.message.chat.id, document=log_file, caption="📃 Это все логи, которые бот успел собрать на момент отправки.")
                log_file.close()
            os.remove("chatlog.txt")
        except Exception as e:
            print(e)
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Cкрыть уведомление", callback_data="dellthiserror")
            button2 = types.InlineKeyboardButton("Скрыть уведомление и ваше сообщение", callback_data="delerrorandmsguserbot")
            markup.add(button1)
            markup.add(button2)
            bot.send_message(chat_id=call.message.chat.id, text=f"❌ *Файл логов оказался пустым, что привело к ошибке*: {e}", reply_markup=markup, parse_mode="Markdown")

    bot.polling(none_stop=True)


while True:
    try:
        mainstarter()
    except Exception as e:
        print(e)
        continue
