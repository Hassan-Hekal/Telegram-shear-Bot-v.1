import json
import asyncio
import re
from telethon import TelegramClient

# قراءة ملف الإعدادات
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

api_id = config["api_id"]
api_hash = config["api_hash"]
groups = config["groups"]
message = config["message"]
interval_minutes = config.get("interval_minutes", 30)

# إنشاء جلسة تيليجرام
client = TelegramClient("session", api_id, api_hash)

# الوظيفة الرئيسية
async def main():
    while True:
        for group in groups:
            try:
                # لو اللينك فيه t.me/ هياخده زي ما هو
                if "t.me/" in group:
                    await client.send_message(group, message)
                else:
                    # لو رقم ID أو username
                    await client.send_message(group.strip(), message)

                print(f"✅ تم إرسال الرسالة إلى: {group}")
            except Exception as e:
                print(f"❌ خطأ في الإرسال لـ {group}: {e}")

        await asyncio.sleep(interval_minutes * 60)

# تشغيل البوت
with client:
    client.loop.run_until_complete(main())