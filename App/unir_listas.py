import os

fuentes = [
    "../Fuentes/Zeronet/lista_zeronet.m3u"
#    "../Fuentes/Telegram/lista_telegram.m3u"
#    "../Fuentes/VK_Video/lista_vk.m3u"
]

with open("lista_final.m3u", "w", encoding="utf-8") as salida:
    salida.write("#EXTM3U\n")
    for archivo in fuentes:
        if os.path.exists(archivo):
            with open(archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    if not linea.strip().startswith("#EXTM3U"):
                        salida.write(linea)

print("Listas unificadas con éxito.")

