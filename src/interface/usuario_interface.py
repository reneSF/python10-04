from typing import TypedDict
from typing import Optional

class UsuarioInterface(TypedDict):
    nombre: str
    apellidoP: str
    apellidoM: str
    direccion: str
    telefono: str
    ciudad: str
    estado: str
    usuario: str
    password: str
    rol: str
    bloqueado: str
    intentos: int
    