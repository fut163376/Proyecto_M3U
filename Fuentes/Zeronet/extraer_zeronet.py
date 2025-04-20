import requests

url = "http://127.0.0.1:43110/1JKe3VPvFe35bm1aiHdD4p1xcGCkZKhH3Q/data/listas/lista_iptv.m3u"
destino = "lista_zeronet.m3u"

response = requests.get(url)
with open(destino, "w", encoding="utf-8") as f:
    f.write(response.text)
print("Zeronet: Archivo M3U descargado.")

