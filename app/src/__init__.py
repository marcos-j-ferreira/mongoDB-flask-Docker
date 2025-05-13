from flask import Flask


def create_app():
    app = Flask(__name__)

    from src.routes.routes import tarefas

    app.register_blueprint(tarefas, url_prefix='/tarefas')

    return app