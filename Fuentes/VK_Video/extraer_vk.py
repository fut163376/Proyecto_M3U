import requests
from bs4 import BeautifulSoup
import urllib.parse
import os

# URL del canal de VK
VK_CHANNEL_URL = "https://vkvideo.ru/@vitalsport11"

# Archivo de salida
output_path = os.path.join(os.path.dirname(__file__), "vk_resultado.m3u")

def obtener_directo_vk():
    print(f"Extrayendo directo de: {VK_CHANNEL_URL}")

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(VK_CHANNEL_URL, headers=headers)
        response.raise_for_status()
    except Exception as e:
        print(f"Error al acceder a VK: {e}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    # Buscar enlaces con z=video
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if "z=video" in href:
            full_url = urllib.parse.urljoin(VK_CHANNEL_URL, href)
            parsed = urllib.parse.urlparse(full_url)
            query = urllib.parse.parse_qs(parsed.query)

            if "z" in query:
                video_info = query["z"][0]  # e.g. video-21620613_456250057/club21620613
                video_id = video_info.split("/")[0]  # Solo nos quedamos con video-xxx_yyy
                video_url = f"https://vk.com/{video_id}"
                return video_url

    print("No se encontró ningún directo.")
    return None

def generar_m3u(video_url):
    with open(output_path, "w") as f:
        f.write("#EXTM3U\n")
        f.write("#EXTINF:-1 tvg-id=\"\" tvg-name=\"VK Live\" tvg-logo=\"\" group-title=\"VK\",VK En Vivo\n")
        f.write(video_url + "\n")
    print(f"Archivo M3U generado: {output_path}")

if __name__ == "__main__":
    url_directo = obtener_directo_vk()
    if url_directo:
        generar_m3u(url_directo)

