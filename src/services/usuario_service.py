from repositories.usuario_repository import UsuarioRepository
from models.usuario import Usuario
from utils.password_utils import hash_password, check_password

#class UsuarioService:
    #@staticmethod
    #def UsuarioRepository.get_by_username(data{'usuario'}):
    #    return None, "El nombre de usuario ya existe"
    #data['password'] = hash_password(data['password'])
    #data['bloqueado'] = False
    #data['intentos'] = 0
    #usuario = Usuario(**data)
    #usuario_id = UsuarioRepository.create(usuario.to_dict())
    #return usuario_id, "Usuario creado con éxito"
class UsuarioService:
    @staticmethod
    def create_usuario(data):
        # Verificar si el nombre de usuario ya existe
        existing_user = UsuarioRepository.get_by_username(data['usuario'])
        if existing_user:
            return None, "El nombre de usuario ya existe"
        
        # Preparar los datos para el nuevo usuario
        data['password'] = hash_password(data['password'])
        data['bloqueado'] = False
        data['intentos'] = 0

        # Crear el objeto usuario
        usuario = Usuario(**data)
        usuario_id = UsuarioRepository.create(usuario.to_dict())
        
        return usuario_id, "Usuario creado con éxito"

    
    @staticmethod
    def get_all():
        return UsuarioRepository.get_all()

    @staticmethod
    def get_by_id(usuario_id):
        return UsuarioRepository.get_by_id(usuario_id)
    
    @staticmethod
    def update(usuario_id, data):
        if 'password' in data:
            data['password'] = hash_password(data['password'])
        return UsuarioRepository.update(usuario_id, data)
    
    @staticmethod
    def delete(usuario_id):
        return UsuarioRepository.delete(usuario_id)
    
    @staticmethod
    def get_by_username(username):
        return UsuarioRepository.get_by_username(username)
    
    """ @staticmethod
    def login(username, passeord):
    usuario = UsuarioRepository.get_by_username(username)
    if not usuario:
        return None, "Usuario no encontrado"

    if usuario['bloqueado']:
        return None, "Usuario bloqueado"

    if not check_password(password, usuario ['password']):
        intentos = usuario['intentos'] + 1
        bloqueado = intentos >= 3
        UsuarioRepository.update(usuario['id'], {'intentos': intentos, 'bloqueado': bloqueado})
    return None, "Contraseña incorrecta"
    usuario['intentos'] = 0 """

    @staticmethod
    def login(username, password):
    usuario = UsuarioRepository.get_by_username(username)
    # Verificar si el usuario existe
    if not usuario:
        return None, "Usuario no encontrado"

    if usuario['bloqueado']:
        return None, "Usuario bloqueado"

    if not check_password(password, usuario['password']):
        # Incrementar intentos
        intentos = usuario['intentos'] + 1
        bloqueado = intentos >= 3

        # Actualizar intentos y estado de bloqueo
        UsuarioRepository.update(usuario['id'], {'intentos': intentos, 'bloqueado': bloqueado})
        
        return None, "Contraseña incorrecta"

    # Si la contraseña es correcta, reiniciar intentos
    UsuarioRepository.update(usuario['id'], {'intentos': 0})
    return usuario, "Login exitoso"


    @staticmethod
    def logout(usuario_id):
        return True, "Sesión cerrada con éxito"

    @staticmethod
    def unlock_user(usuario_id):
        usuario = UsuarioRepository.get_by_id(usuario_id)
        if not usuario:
            return None, "Usuario no encontrado"
        if not usuario['bloqueado']:
            return None, "Usuario no está bloqueado"
        UsuarioRepository.update(usuario_id, {'bloqueado': False, 'intentos': 0})
        return True, "Usuario desbloqueado con éxito"