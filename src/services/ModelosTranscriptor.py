import whisperx

def transcribirWhisper(nomArchivo, config):
    '''Recibe como parámetro la ruta con el nombre del audio a transcribir y la configuración del whisper.
    Esta función recibe le audio, lo procesa con whisperx. Retorna la transcripción resultante.'''

    #Cargar modelo segun la configuración
    model = whisperx.load_model(config.modelo, config.dispositivo, compute_type=config.tipoComputo, language="es")
    #Cargar audio al modelo de whisper seleccionado
    audio = whisperx.load_audio(f'src/uploads/{nomArchivo}')
    result = model.transcribe(audio, batch_size=config.tamLote)
    texto_unificado = ""
    # Concatenamos los textos
    for resultado in result["segments"]:
        texto_unificado += resultado['text']
    return texto_unificado