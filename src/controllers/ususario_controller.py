from services.usuario_service import UsuarioService

class UsuarioController:
    @staticmethod
    def create(req, res):
        usuario_id, message = UsuarioService.create(req.json)
        if usuario_id:
            return res.json ({"id": usuario_id, "message": message}), 201
        else:
            return res.json({"message": message}), 400
    
    @staticmethod
    def get_all(req, res):
        usuarios = UsuarioService.get_all()
        return res.json(usuarios), 200
    
    @staticmethod
    def get_by_id(req, res, usuario_id):
        usuario = UsuarioService.get_by_id(usuario_id)
        if usuario:
            return res.json(usuario), 200
        else:
            return res.json({"message": "Usuario no encontrado"}), 404
    
    @staticmethod
    def update(req, res):
        usuario_id = req.params['id']
        data = req.json
        updated = UsuarioService.update(usuario_id, data)
        if updated:
            return res.json({"message": "Usuario actualizado con éxito"}), 200
        else:
            return res.json({"message": "Error al actualizar el usuario"}), 400
        
    @staticmethod
    def delete(req, res):
        delete_id = req.params['id']
        deleted = UsuarioService.delete(delete_id)
        if deleted:
            return res.json({"message": "Usuario eliminado con éxito"}), 200
        else:
            return res.json({"message": "Error al eliminar el usuario"}), 400
    
    @staticmethod
    def login(req, res):
        username = req.json['usuario']
        password = req.json['password']
        usuario, message = UsuarioService.login(username, password)
        if usuario:
            return res.json({"message": "Inicio de sesión exitoso", "usuario": usuario}), 200
        else:
            return res.json({"message": message}), 401

    @staticmethod
    def logout(req, res):
        return res.json({"message": "Sesión cerrada con éxito"}), 200
    
    @staticmethod
    def unlock_user(req, res):
        usuario_id = req.params['id']
        desbloqueado = UsuarioService.unlock_user(usuario_id)
        if desbloqueado:
            return res.json({"message": "Usuario desbloqueado con éxito"}), 200
        else:
            return res.json({"message": "Error al desbloquear el usuario"}), 400
        
    
