#!/bin/bash

# Cambiar a la carpeta Fuentes y ejecutar los scripts de extracción
echo "Ejecutando extracción de fuentes..."

# Extracción de Zeronet
cd Fuentes/Zeronet
python3 extraer_zeronet.py
cd ../../

# Extracción de Telegram
#cd Fuentes/Telegram
#python3 extraer_telegram.py
#cd ../../

# Extracción de VK
#cd Fuentes/VK_Video
#python3 extraer_vk.py
#cd ../../

# Unificar las listas en la carpeta App
echo "Unificando listas..."
cd App
python3 unir_listas.py
cd ../

# Subir a GitHub
echo "Subiendo a GitHub..."
git add .
git commit -m "Actualización automática de la lista: $(date '+%Y-%m-%d %H:%M:%S')"
git push
echo "Archivos subidos --> URL: https://github.com/fut163376/Proyecto_M3U/blob/master/App/lista_final.m3u "

# Levantar servidor o cualquier otra acción final
#echo "Levantando servidor..."
#cd Despliegue
#python3 servidor.py  # Si estás levantando un servidor para servir el archivo

