from flask import jsonify, request
from src.services.Archivos import guardarAudio, eliminarAudio
from src.services.ModelosTranscriptor import transcribirWhisper
from src.models.whisperConfig import whisperConfig
from src import app

import traceback
import time

# Logger
from src.utils.Logger import Logger

#Ruta POST para recibir un archivo y transcribirlo
@app.route('/transcribir', methods=['POST'])
def transcribirArchivo():
    try:
        Logger.add_to_log("info", "{} {}".format(request.method, request.path))
        #Guardar archivo en sistema de archivos - deberia descomprimir a futuro
        if 'audio' not in request.files:
            return jsonify({'message': "Archivo no encontrado", 'success': False})#error
        archivo = request.files['audio']
        if archivo.filename == '':
            return jsonify({'message': "Archivo no seleccionado", 'success': False})#error
        nomArchivo = guardarAudio(request.remote_addr, archivo)
        #Procesar audio con whisper
        #Configuración del modelo
        modelo = request.form['modelo']
        dispositivo = request.form['dispositivo']
        tamLote = int(request.form['tamLote'])
        tipoComputo = request.form['tipoComputo']
        config = whisperConfig(modelo, dispositivo, tamLote, tipoComputo)
        #Proceso de transcripción
        start_time = time.time()
        transcripcion = transcribirWhisper(nomArchivo, config)
        end_time = time.time()
        tiempo_transcurrido = end_time - start_time
        #Eliminar archivo
        eliminarAudio(nomArchivo)
        return jsonify({'texto':transcripcion, 'tiempo':tiempo_transcurrido, 'success': True})
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

        response = jsonify({'message': "Internal Server Error", 'success': False})
        return response, 500