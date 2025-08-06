from pyrogram import Client, filters
from bot.bypass import bypass_url

def register_handlers(app: Client):
    @app.on_message(filters.private & filters.text)
    async def handle_message(client, message):
        url = message.text.strip()
        await message.reply_text("🔄 Bypassing URL, please wait...")

        try:
            bypassed = bypass_url(url)
            await message.reply_text(f"✅ Bypassed URL:\n{bypassed}")
        except Exception as e:
            await message.reply_text(f"❌ Error:\n{str(e)}")
