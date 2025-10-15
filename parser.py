import asyncio

from pyrogram import Client, idle
from Bot.user_manager import UserManager
from time import time
import random

class Parser:
    def __init__(self, api_id, api_hash):
        self.api_hash = api_hash
        self.api_id = api_id

        self.us = UserManager()
        self.app = Client("my_session", api_id=self.api_id, api_hash=self.api_hash)

    async def start(self):
        print("Parsing started")
        await self.app.start()

    async def stop(self):
        print(f"{self.us.new_user_count} new users added")
        if self.us.new_user_count > 0:
            self.us.save_users_to_json()
        print("Parsing finished")
        await self.app.stop()

    async def get_user_by_id_from_chat(self, chat_id, username):
        try:
            data = await self.app.get_chat_member(chat_id, username)
            user = self.us.create_user(data.user.id, data.user.username,
                                       data.user.first_name, data.user.last_name,
                                       data.user.phone_number)
            self.us.add_user(user)
        except Exception as e:
            print(e)

    async def get_all_users(self, chat_id):
        async for member in self.app.get_chat_members(chat_id):
            self.us.add_user(self.us.create_user(member.user.id,
                                               member.user.username,
                                               member.user.first_name,
                                               member.user.last_name,
                                               member.user.phone_number))

    async def send_message(self, user_id, text):
        await self.app.send_message(user_id, text)

    async def send_message_in_random_time(self, user_id, text):
        await self.app.send_message(user_id, text)

    async def idle(self):
        await idle()
