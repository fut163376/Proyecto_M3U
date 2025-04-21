#api_id = 23489544   # API ID de tu aplicación de Telegram
#api_hash = '13a6295b41088add583289a62445559f'  # API Hash de tu aplicación de Telegram



from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaWebPage
import os

# Configuración de la API
api_id = 23489544
api_hash = '13a6295b41088add583289a62445559f'

# Lista de nombres exactos de los grupos (como aparecen en la app de Telegram)
nombres_grupos = [
    "F 1 🏁",
    "MotoGP",
    "BL2",
    "PL2",
    "CH 1 (2)",
    "CH1"
]

# Ruta de salida del archivo .m3u
salida = os.path.join(os.path.dirname(__file__), 'telegram_resultado.m3u')

# Función para extraer enlaces de transmisiones en los mensajes
def extraer_streamings(mensajes):
    links = []
    for msg in mensajes:
        if msg.media and isinstance(msg.media, MessageMediaWebPage):
            web_page = msg.media.webpage
            if hasattr(web_page, 'url'):
                links.append(web_page.url)
        elif msg.message and 'http' in msg.message:
            for word in msg.message.split():
                if word.startswith('http'):
                    links.append(word)
    return links

# Inicio de sesión con el cliente de Telegram
with TelegramClient('session', api_id, api_hash) as client:
    print("Sesión iniciada correctamente.")
    enlaces_finales = []

    for dialog in client.iter_dialogs():
        if dialog.is_group or dialog.is_channel:
            if dialog.name in nombres_grupos:
                try:
                    print(f"Accediendo al grupo: {dialog.name}")
                    mensajes = client.iter_messages(dialog.entity, limit=100)
                    links = extraer_streamings(mensajes)
                    print(f"  → {len(links)} enlaces encontrados.")
                    enlaces_finales.extend(links)
                except Exception as e:
                    print(f"Error al procesar el grupo '{dialog.name}': {e}")

    # Guardar archivo M3U
    with open(salida, 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n")
        for link in enlaces_finales:
            f.write(f"#EXTINF:-1, Telegram Live\n{link}\n")

    print(f"\nArchivo M3U generado: {salida}")

