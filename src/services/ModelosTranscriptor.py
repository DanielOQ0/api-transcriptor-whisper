import whisperx
import numpy as np
import librosa

modelDefault = whisperx.load_model("medium", "cuda", compute_type="float16", language="es")


def transcribirWhisper(nomArchivo, config):
    '''Recibe como parámetro la ruta con el nombre del audio a transcribir y la configuración del whisper.
    Esta función recibe le audio, lo procesa con whisperx. Retorna la transcripción resultante.'''

    #Cargar modelo segun la configuración
    model = whisperx.load_model(config.modelo, config.dispositivo, compute_type=config.tipoComputo, language="es")
    #Cargar audio al modelo de whisper seleccionado
    audio = whisperx.load_audio(f'src/uploads/{nomArchivo}')
    #Transcribir
    result = model.transcribe(audio, batch_size=config.tamLote)
    texto_unificado = ""
    # Concatenamos los textos
    for resultado in result["segments"]:
        texto_unificado += resultado['text']
    return texto_unificado

def transcribirWhisperDirecto(config, req):
    '''Recibe como parámetro la ruta con el nombre del audio a transcribir y la configuración del whisper.
    Esta función recibe le audio, lo procesa con whisperx. Retorna la transcripción resultante.'''

    #Cargar audio de forma directa
    audio_np = np.frombuffer(req.audio, dtype=np.int16)
    # Re-muestreo a la frecuencia deseada para whisper que es 16000
    if req.frecuencia != 16000:
        audio_resampled = librosa.resample(audio_np.astype(np.float32), orig_sr=req.frecuencia, target_sr=16000)
        # Normalizar a valores entre -1 y 1
        audio_resampled /= np.max(np.abs(audio_resampled))
    else:
        audio_resampled =audio_np.flatten().astype(np.float32) / 32768.0

    if config.modelo == "default":
        #Transcribir
        result = modelDefault.transcribe(audio_resampled, batch_size=config.tamLote)
    else:
        #Cargar modelo segun la configuración
        model = whisperx.load_model(config.modelo, config.dispositivo, compute_type=config.tipoComputo, language="es")
        #Transcribir
        result = model.transcribe(audio_resampled, batch_size=config.tamLote)
    
    texto_unificado = ""
    # Concatenamos los textos
    for resultado in result["segments"]:
        texto_unificado += resultado['text']
    return texto_unificado