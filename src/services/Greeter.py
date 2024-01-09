from src.protocode import audio_pb2, audio_pb2_grpc 
from src.services.Archivos import *
from src.services.ModelosTranscriptor import transcribirWhisper, transcribirWhisperDirecto
from src.models.whisperConfig import whisperConfig

import time

class Greeter(audio_pb2_grpc.GreeterServicer):
    def RouteTranscribir(self, request, context):
        nomArchivo = guardarAudioBytes(request.audio, request.frecuencia)
        #Procesar audio con whisper
        #Configuración del modelo
        modelo = request.modelo
        dispositivo = request.dispositivo
        tamLote = request.tamLote
        tipoComputo = request.tipoComputo
        config = whisperConfig(modelo, dispositivo, tamLote, tipoComputo)
        #Proceso de transcripción
        start_time = time.time()
        #transcripcion = transcribirWhisper(nomArchivo, config)
        transcripcion = transcribirWhisperDirecto(config, request.audio)
        end_time = time.time()
        tiempo_transcurrido = end_time - start_time
        #Eliminar archivo
        eliminarAudio(nomArchivo)
        return audio_pb2.TranscribirReply(success=True, texto=transcripcion, tiempo=tiempo_transcurrido)