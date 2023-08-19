import time

import telethon.tl.types
from telethon.sync import TelegramClient, events
from datetime import datetime

import anekdot
import randstuff

# Setting variables
session_name = 'egorich'
sanya_id = 810634195
api_id = 2724818
api_hash = '6c677b0f0e2af14a53cbf0c0eafe5886'
white_list_map = {1058082172: 'Client'}
direct_history = {}

# Code execution
white_list = list(white_list_map.keys())
with TelegramClient(session_name, api_id, api_hash) as client:
    @client.on(events.UserUpdate())
    async def handler(event):
        if event.original_update.user_id in white_list:
            current_time = datetime.now().strftime("%H:%M:%S")
            if event.action:
                last_update = 0
                if event.original_update.user_id in direct_history.keys():
                    last_update = direct_history[event.original_update.user_id]
                direct_history[event.original_update.user_id] = time.time()
                if last_update != 0 and time.time() - last_update < 5:
                    return

                print(white_list_map[event.original_update.user_id], 'печатает в', current_time)
                await client.send_message(entity=sanya_id, message="Пользователь печатает")

            if type(event.status) == telethon.tl.types.UserStatusOnline:
                print(white_list_map[event.original_update.user_id], 'зашел в сеть в', current_time)
                await client.send_message(entity=sanya_id, message="Пользователь зашел в сеть")
            if type(event.status) == telethon.tl.types.UserStatusOffline:
                print(white_list_map[event.original_update.user_id], 'вышел из сети в', current_time)
                await client.send_message(entity=sanya_id, message="Пользователь вышел из сети")

    client.run_until_disconnected()
