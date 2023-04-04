import asyncio
import os
import shutil

async def examenes(archivo):
    nombre = archivo.name
    nombre = nombre[1:-4]
    destino = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    try:
        destinor = destino + f"\Expediente-00{nombre}\Examen_00{nombre} (F).pdf"
        shutil.move(archivo.path, destinor)
    except FileNotFoundError:
        destino_carpeta = destino + f"\Expediente-00{nombre}"
        os.mkdir(destino_carpeta)
        destino = destino + f"\Expediente-00{nombre}\Examen_00{nombre} (F).pdf"
        shutil.move(archivo.path, destino)

async def solicitudes(archivo):
    nombre = archivo.name
    nombre = nombre[1:-4]
    destino = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    try:
        destinor = destino + f"\Expediente-00{nombre}\Solicitud de Certificacion_00{nombre} (F).pdf"
        shutil.move(archivo.path, destinor)
    except FileNotFoundError:
        destino_carpeta = destino + f"\Expediente-00{nombre}"
        os.mkdir(destino_carpeta)
        destino = destino + f"\Expediente-00{nombre}\Solicitud de Certificacion_00{nombre} (F).pdf"
        shutil.move(archivo.path, destino)

async def separadore(archivo):
    nombre = archivo.name
    nombre = nombre[1:-4]
    numeros = nombre.split("-")
    destino = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for numero in numeros:
        try:
            destinor = destino + f"\Expediente-00{numero}\Examen_00{numero} (F).pdf"
            shutil.copyfile(archivo.path, destinor)
        except FileNotFoundError:
            destino_carpeta = destino + f"\Expediente-00{numero}"
            os.mkdir(destino_carpeta)
            destino = destino + f"\Expediente-00{numero}\Examen_00{numero} (F).pdf"
            shutil.copyfile(archivo.path, destino)
    os.rename(archivo.path)

async def separadors(archivo):
    nombre = archivo.name
    nombre = nombre[1:-4]
    numeros = nombre.split("-")
    destino = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for numero in numeros:
        try:
            destinor = destino + f"\Expediente-00{numero}\Solicitud de Certificacion_00{numero} (F).pdf"
            shutil.copyfile(archivo.path, destinor)
        except FileNotFoundError:
            destino_carpeta = destino + f"\Expediente-00{numero}"
            os.mkdir(destino_carpeta)
            destinoc = destino + f"\Expediente-00{numero}\Solicitud de Certificacion_00{numero} (F).pdf"
            shutil.copyfile(archivo.path, destinoc)
    os.remove(archivo.path)

def main():
    archivos = os.scandir("Documentos a Organizar")
    for archivo in archivos:
        if archivo.name.startswith("e"):
            if "-" in archivo.name:
                asyncio.run(separadore(archivo))
            else:
                asyncio.run(examenes(archivo))
        if archivo.name.startswith("s"):
            if "-" in archivo.name:
                asyncio.run(separadors(archivo))
            else:
                asyncio.run(solicitudes(archivo))

if __name__ == "__main__":
    main()
