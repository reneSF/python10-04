from flask import Flask
from flask_cors import CORS
from routes.index import router

app = Flask(__name__)
CORS(app)
app.register_blueprint(router, url_prefix='/api')
if __name__ == '__main__':
    app.run(port=5050, debug=True)