from flask import Blueprint, request
from controllers.ususario_controller import UsuarioController

usuario_routes = Blueprint('usuario_routes', __name__)

usuario_routes.route('/', methods=['GET'])(UsuarioController.get_all)
usuario_routes.route('/create', methods=['POST'])(UsuarioController.create)
usuario_routes.route('/update/<id>', methods=['PUT'])(UsuarioController.update)
usuario_routes.route('/delete/<id>', methods=['DELETE'])(UsuarioController.delete)
usuario_routes.route('/login', methods=['POST'])(UsuarioController.login)
usuario_routes.route('/logout', methods=['POST'])(UsuarioController.logout)
usuario_routes.route('/unlock/<id>', methods=['POST'])(UsuarioController.unlock_user)
usuario_routes.route('/<id>', methods=['GET'])(UsuarioController.get_by_id)

