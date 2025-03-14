from telethon import TelegramClient, events
from telethon.tl.types import UserStatusOnline, UserStatusOffline, User
import asyncio
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
SESSION_NAME = os.getenv('SESSION_NAME')
USER_ID_TO_TRACK = int(os.getenv('USER_ID_TO_TRACK'))
LOG_CHAT_ID = int(os.getenv('LOG_CHAT_ID'))

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

def get_current_time():
    return datetime.now().strftime('%H:%M:%S')

async def check_user_status():
    user = await client.get_entity(USER_ID_TO_TRACK)
    status = user.status
    current_time = get_current_time()
    if isinstance(status, UserStatusOnline):
        await client.send_message(LOG_CHAT_ID, f"✅ Користувач [{user.first_name}](tg://user?id={USER_ID_TO_TRACK}) зараз в мережі. Час: {current_time}")
    elif isinstance(status, UserStatusOffline):
        await client.send_message(LOG_CHAT_ID, f"❌ Користувач [{user.first_name}](tg://user?id={USER_ID_TO_TRACK}) зараз офлайн. Час: {current_time}")

@client.on(events.UserUpdate)
async def user_update_handler(event):
    if event.user_id == USER_ID_TO_TRACK:
        user = await client.get_entity(USER_ID_TO_TRACK)
        current_time = get_current_time()
        if isinstance(event.status, UserStatusOnline):
            await client.send_message(LOG_CHAT_ID, f"✅ Користувач [{user.first_name}](tg://user?id={USER_ID_TO_TRACK}) зайшов в мережу. Час: {current_time}")
        elif isinstance(event.status, UserStatusOffline):
            await client.send_message(LOG_CHAT_ID, f"❌ Користувач [{user.first_name}](tg://user?id={USER_ID_TO_TRACK}) вийшов з мережі. Час: {current_time}")

async def main():
    await check_user_status()
    print(f"✅ Юзербот запущено та відстежує користувача {USER_ID_TO_TRACK}")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
