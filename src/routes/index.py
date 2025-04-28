from flask import Blueprint
from routes.usuario_routes import usuario_routes

router = Blueprint('router', __name__)
router.register_blueprint(usuario_routes, url_prefix='/usuarios')
