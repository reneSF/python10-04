import config.firebase_config as firebase_config

from models.usuario import Usuario
class UsuarioRepository:
    @staticmethod
    def create(data):
        usuario = db.collection("usuarios_python").document()
        usuario.set(data)
        return usuario.id
    
    @staticmethod
    def get_all():
        return [{"id": doc.id, **doc.to_dict()} for doc in db.collection("usuarios_python").stream()]
        
    @staticmethod
    def get_by_id(usuario_id):
        usuario = db.collection("usuarios_python").document(usuario_id).get()
        if usuario.exists:
            return Usuario(**usuario.to_dict())
        else:
            return None
    
    @staticmethod
    def update(usuario_id, data):
        usuario = db.collection("usuarios_python").document(usuario_id)
        usuario.update(data)
        return True
    
    @staticmethod
    def delete(usuario_id):
        usuario = db.collection("usuarios_python").document(usuario_id)
        usuario.delete()
        return True
    
    @staticmethod
    def get_by_username(username):
        usuario = db.collection("usuarios_python").where("usuario", "==", username).get()
        if usuario:
            return [{ "id": doc.id, **doc.to_dict()} for doc in usuario]
        else:
            return None