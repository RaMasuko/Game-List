from flask import Flask
from .controllers.tarefa_controller import tarefa_controller 

def create_app():

    app = Flask(__name__, template_folder='views') 

    app.register_blueprint(tarefa_controller)

    return app