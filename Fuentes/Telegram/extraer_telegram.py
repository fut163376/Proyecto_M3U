#api_id = 23489544   # API ID de tu aplicación de Telegram
#api_hash = '13a6295b41088add583289a62445559f'  # API Hash de tu aplicación de Telegram



from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaWebPage
import os

api_id = 23489544  # tu API ID
api_hash = '13a6295b41088add583289a62445559f'  # tu API HASH

# Lista de nombres exactos de los grupos (como aparecen en la app de Telegram)
nombres_grupos = [
    "F 1 🏁",
    "MotoGP",
    "BL2",
    "PL2",
    "CH 1 (2)",
    "CH1"
]

salida = os.path.join(os.path.dirname(__file__), 'telegram_resultado.m3u')

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

with TelegramClient('session', api_id, api_hash) as client:
    print("Sesión iniciada correctamente.")
    enlaces_finales = []

    for nombre in nombres_grupos:
        try:
            print(f"Accediendo al grupo: {nombre}")
            entidad = client.get_entity(nombre)
            mensajes = client.iter_messages(entidad, limit=100)
            links = extract_live_streams(mensajes)
            print(f"  → {len(links)} enlaces encontrados.")
            enlaces_finales.extend(links)
        except Exception as e:
            print(f"Error al procesar el grupo '{nombre}': {e}")

    # Guardar archivo .m3u
    with open(salida, 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n")
        for link in enlaces_finales:
            f.write(f"#EXTINF:-1, Telegram Live\n{link}\n")

    print(f"\nArchivo M3U generado: {salida}")

