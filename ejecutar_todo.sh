#!/data/data/com.termux/files/usr/bin/bash

echo "Ejecutando extracción de fuentes..."
cd Fuentes/Zeronet && python3 extraer_zeronet.py && cd ../..
#cd Fuentes/Telegram && python3 extraer_telegram.py && cd ../..
#cd Fuentes/VK_Video && python3 extraer_vk.py && cd ../..

echo "Unificando listas..."
cd App && python3 unir_listas.py && cd ..

echo "Levantando servidor..."
cd Despliegue && python3 servidor.py

