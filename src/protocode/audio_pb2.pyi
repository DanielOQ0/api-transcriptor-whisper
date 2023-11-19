from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TranscribirRequest(_message.Message):
    __slots__ = ["modelo", "tamLote", "tipoComputo", "dispositivo", "audio", "frecuencia"]
    MODELO_FIELD_NUMBER: _ClassVar[int]
    TAMLOTE_FIELD_NUMBER: _ClassVar[int]
    TIPOCOMPUTO_FIELD_NUMBER: _ClassVar[int]
    DISPOSITIVO_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    FRECUENCIA_FIELD_NUMBER: _ClassVar[int]
    modelo: str
    tamLote: int
    tipoComputo: str
    dispositivo: str
    audio: bytes
    frecuencia: int
    def __init__(self, modelo: _Optional[str] = ..., tamLote: _Optional[int] = ..., tipoComputo: _Optional[str] = ..., dispositivo: _Optional[str] = ..., audio: _Optional[bytes] = ..., frecuencia: _Optional[int] = ...) -> None: ...

class TranscribirReply(_message.Message):
    __slots__ = ["success", "texto", "tiempo"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    TEXTO_FIELD_NUMBER: _ClassVar[int]
    TIEMPO_FIELD_NUMBER: _ClassVar[int]
    success: bool
    texto: str
    tiempo: float
    def __init__(self, success: bool = ..., texto: _Optional[str] = ..., tiempo: _Optional[float] = ...) -> None: ...
