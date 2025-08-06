from pyrogram import Client
from bot.handlers import register_handlers
from config.config import API_ID, API_HASH, BOT_TOKEN

app = Client("url_bypass_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

register_handlers(app)

print("Bot is running...")

app.run()
