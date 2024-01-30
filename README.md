# API TRANSCRIPTOR WHISPER
El siguiente microservicio permite la transmision de datos de audio para su transcripción con el modelo de whisperx.


## API Referencia

Envio del cuerpo con los parametros necesarios para la configuración y uso del modelo mediante solicitud REST

```http
  POST /transcribir
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `modelo` | `string` | **Requerido**. Modelo de whisper a utilizar "tiny", "base", "small", "medium", "large", "large-v2", "large-v3" |
| `tamLote` | `number` | **Requerido**. Tamaño por lote que whisper va a procesar, se recomienda "8" para trabajo con cpu y "16" para trabajar con gpu |
| `tipoComputo` | `string` | **Requerido**. Tipo de computo que whisper utilizará para procesar el audio, se recomienda "int8" para cpu y "float16" para gpu |
| `dispositivo` | `string` | **Requerido**. Tipo de hardware que utilizara el modelo de whisper para procesar el audio, siendo "cpu" para usar el procesador, o "cuda" para usar la gpu |
| `audio` | `bytes` | **Requerido**. Chunk de bytes del audio a procesar |
| `frecuencia` | `number` | **Requerido**. Frecuencia de muestreo del audio |
 
Envio del cuerpo con los parametros necesarios para la configuración y uso del modelo mediante solicitud GRPC

```http
  rpc RouteTranscribir
```

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `modelo` | `string` | **Requerido**. Modelo de whisper a utilizar "tiny", "base", "small", "medium", "large", "large-v2", "large-v3". Ademas cuenta con el modelo "default"(recomendada) que precarga una configuracion por defecto mas eficiente|
| `tamLote` | `number` | **Requerido**. Tamaño por lote que whisper va a procesar, se recomienda "8" para trabajo con cpu y "16"(recomendada) para trabajar con gpu |
| `tipoComputo` | `string` | **Requerido**. Tipo de computo que whisper utilizará para procesar el audio, se recomienda "int8" para cpu y "float16"(recomendada) para gpu |
| `dispositivo` | `string` | **Requerido**. Tipo de hardware que utilizara el modelo de whisper para procesar el audio, siendo "cpu" para usar el procesador, o "cuda"(recomendada) para usar la gpu |
| `audio` | `bytes` | **Requerido**. Chunk de bytes del audio a procesar |
| `frecuencia` | `number` | **Requerido**. Frecuencia de muestreo del audio |



## Instalacion

1. Tener instalado al menos python 3.10.12 y ffmpeg
```bash
sudo apt update && sudo apt install ffmpeg python3 python3-pip
```
2. Clonar el proyecto con
```bash
  git clone https://danielorozco@172.16.19.36/proyectosespeciales/transcriptor-whisper.git
  cd transcriptor-whisper
```
3. Instalar recursos necesarios para despliegue
#####Nota: si desea instalar en entorno virtual, cree y active el entorno virtual (recomendado). En caso contrario instalar librerias solamente, la instalacion sin entorno virtual se realiza de forma global
- Crear entorno virtual
```bash
  python -m venv nombre_env
  .\nombre_env\Scripts\activate
```
- Instalar Librerias
```bash
  #Intalar librerias
  pip install -r requirements.txt
  
  #Instalar WhisperX
  pip install git+https://github.com/m-bain/whisperx.git --upgrade
  
 #Instalar driver y librerias necesarias para manejo de gpu
 	#Usando pip
	 pip install torch==2.0.0 torchvision==0.15.1 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu118
 	#Usando Conda (recomendado)
	 conda install pytorch==2.0.0 torchaudio==2.0.0 pytorch-cuda=11.8 -c pytorch -c nvidia
```
## Despliegue

Para desplegar este proyecto en modo híbrido,  que permite utilizar REST y GRPC al tiempo, ejecute

```bash
  python index.py
```
Para desplegar este proyecto en modo solo GRPC, ejecute (Recomendado)

```bash
  pyt