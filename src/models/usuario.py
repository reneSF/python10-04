from interfaces.usuario_interface import UsuarioInterface

class Usuario:
    def __init__(self, **kwargs):
        self.data: UsuarioInterface = {
            "nombre": kwargs.get("nombre"),
            "apellidoP": kwargs.get("apellidoP"),
            "apellidoM": kwargs.get("apellidoM"),
            "direccion": kwargs.get("direccion"),
            "telefono": kwargs.get("telefono"),
            "ciudad": kwargs.get("ciudad"),
            "estado": kwargs.get("estado"),
            "usuario": kwargs.get("usuario"),
            "password": kwargs.get("password"),
            "rol": kwargs.get("rol"),
            "bloqueado": kwargs.get("bloqueado", False),
            "intentos": kwargs.get("intentos", 0),
        }

    def to_dict(self):
        return self.data