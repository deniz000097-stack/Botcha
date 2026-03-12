from pyrogram import Client, filters

# Kendi api_id ve api_hash'ini tırnakları bozmadan yaz
api_id = 32655541 
api_hash = "6e517dee10db443b79498531dd0d1d86"

app = Client("my_bot", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.me & filters.reply)
async def save_media(client, message):
    # Yanıt verilen mesajda medya varsa (foto/video/dosya)
    if message.reply_to_message.media:
        try:
            # Medyayı "Kayıtlı Mesajlar"ına kopyalar
            await client.copy_message(
                chat_id="me",
                from_chat_id=message.chat.id,
                message_id=message.reply_to_message.id
            )
            await message.edit("✅ Kaydedildi!")
        except Exception as e:
            await message.edit(f"❌ Hata: {e}")

app.run()
