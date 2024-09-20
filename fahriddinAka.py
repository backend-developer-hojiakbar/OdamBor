from telethon import TelegramClient, events
api_id = 23410307
api_hash = '109bcbc13ced42c47d9f1dd0c127824e'
phone_number = '+998996043489'
keywords = ['pochta bor', 'odam bor', 'почта бор', 'одам бор']
groups = ['rishton_toshkenN1', 'Bogdod_Buvayda_Toshkent_N_1', 'zakazlarbagdod', 'Buvayda_Yangiqorgon_Toshkenn',
          'QOQON_TOSHKENT0', 'taxi_toshkent_bogdod', 'Bagdod_Buvayda_Toshkent', 'buvayda_bogdod_1',
          'taxi_bogdod_toshkent_rishton', 'bagdod_toshkent_taxi_taksi', 'Bogdod_toshkent_taksi_Buvayda',
          'Bagdod_Buvayda_Toshkent_N1', 'BogdotRishton', 'Toshkent_Rishton_Bogdot_N1', 'Bagdod_Buvaydaa',
          'bogdot_toshkent', 'bogdod_toshkentaxi', 'uch_koprik_toshkent_bogdod_buvay', 'bogdod_toshkent_tax',
          'Toshkent_Bogdod_Buvayda_Toshkent', 'Qoqon_toshkent_taxi_24_7', 'Toshkent_bogdod_buvayda_taksi',
          'BUVAYDA_TOSHKENT_Y', 'toshkent_rishton_bogdod_taksi', 'towkent_Bogdod_buvayda_rishton_t',
          'bogdodtoshkenttaxi', 'buvayda_yangiqorgontoshken_pitak', 'Bogdod_Toshkent_Buvayda_Taxi_N1',
          'Rishton_BogdodBuvayda_Toshkent', 'Toshkent_Buvayda_Bogdod', 'Buvayda_Toshken_taxi',
          'Toshkent_Buvayda_Yangiqorgon', 'BUVAYDA_TOSHKENT_Uchkoprik', 'bogdod_toshkent_buvayda_toshkent', 'taxi125437']

target_group = 'zakazlarbagdod'
client = TelegramClient('session_name', api_id, api_hash)


async def main():
    await client.start(phone=phone_number)
    if not client.is_user_authorized():
        await client.send_code_request(phone_number)
        code = input('Tasdiqlash kodini kiriting: ')
        await client.sign_in(phone_number, code)
        if not client.is_user_authorized():
            password = input('Ikki bosqichli tasdiqlash parolini kiriting: ')
            await client.sign_in(password=password)
    for group in groups:
        @client.on(events.NewMessage(chats=(group)))
        async def handler(event):
            print(f"Yangi xabar ({event.chat.title}): {event.raw_text}")
            message_text = event.raw_text.lower()  # Xabarni kichik harflarga aylantiramiz
            if any(keyword in message_text for keyword in keywords):  # Agar kalit so'z topilsa
                await client.send_message(target_group, f'Guruh: {event.chat.title}\nKalit soʻz topildi: {event.raw_text}')  # Xabarni maqsadli guruhga yuboramiz

    print("Dastur ishga tushdi. Xabarlarni kutyapman...")
    await client.run_until_disconnected()
with client:
    client.loop.run_until_complete(main())