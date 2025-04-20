from telethon.sync import TelegramClient
from telethon.tl.types import Channel, Chat

# Rellena con tus datos
api_id = 23489544
api_hash = '13a6295b41088add583289a62445559f'

with TelegramClient('session_name', api_id, api_hash) as client:
    dialogs = client.get_dialogs()

    for dialog in dialogs:
        entity = dialog.entity
        if isinstance(entity, (Channel, Chat)):
            print(f"NOMBRE: {dialog.name}")
            print(f"ID: {entity.id}")
            print(f"Username: {getattr(entity, 'username', 'Ninguno')}")
            print("-" * 50)

