from datetime import datetime

import os
import wave

def guardarAudio(nom, archivo):
    # Guardar el archivo en tu sistema de archivos
    nomArchivo = f'{nom}({datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}).wav'
    archivo.save(os.path.join("src/uploads",nomArchivo))
    return nomArchivo
def eliminarAudio(nom):
    os.remove(os.path.join("src/uploads",nom))
def guardarAudioBytes(bytes_audio, frecuencia):
    # Crea la carpeta si no existe
    if not os.path.exists("src/uploads"):
        os.makedirs("src/uploads")
    nomArchivo = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.wav'

    # Crea un archivo .wav y escribe los bytes
    with wave.open(os.path.join("src/uploads",nomArchivo), 'wb') as archivo_wav:
        archivo_wav.setnchannels(1)  # Número de canales (1 para mono)
        archivo_wav.setsampwidth(2)  # Ancho de muestra en bytes (2 para 16 bits)
        archivo_wav.setframerate(frecuencia)  # Frecuencia de muestreo
        archivo_wav.writeframes(bytes_audio)  # Escribe los frames de audio

    return nomArchivo