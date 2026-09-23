import os
import json
import csv
from PIL import Image   # Recuerda haber instalado: pip install Pillow

def main():
    # Nombre exacto de tu carpeta (según tu panel izquierdo)
    carpeta = "Imagens"

    # 1. Archivo JPG (tu imagen se llama GitHub.jpg)
    ruta_jpg = os.path.join(carpeta, "GitHub.jpg")
    try:
        imagen = Image.open(ruta_jpg)
        print("✅ Imagen JPG cargada correctamente")
        print(f"   Tamaño: {imagen.size}")
        imagen.show()   # Abre la imagen
    except FileNotFoundError:
        print(f"❌ No se encontró el archivo '{ruta_jpg}'")

    # 2. Archivo de texto (.txt)
    ruta_txt = os.path.join(carpeta, "datos.txt")
    try:
        with open(ruta_txt, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            print("\n✅ Archivo TXT leído:")
            print(contenido)
    except FileNotFoundError:
        print(f"❌ No se encontró el archivo '{ruta_txt}'")

    # 3. Archivo JSON
    ruta_json = os.path.join(carpeta, "config.json")
    try:
        with open(ruta_json, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            print("\n✅ Archivo JSON leído:")
            print(datos)
    except FileNotFoundError:
        print(f"❌ No se encontró el archivo '{ruta_json}'")

    # 4. Archivo CSV
    ruta_csv = os.path.join(carpeta, "usuarios.csv")
    try:
        with open(ruta_csv, "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            print("\n✅ Archivo CSV leído:")
            for fila in lector:
                print(fila)
    except FileNotFoundError:
        print(f"❌ No se encontró el archivo '{ruta_csv}'")


if __name__ == "__main__":
    main()