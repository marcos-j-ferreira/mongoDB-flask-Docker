from flask import Flask


def create_app():
    app = Flask(__name__)

    from .routes.routes import routes

    app.register_blueprint(routes, url_prefix='/tarefas')

    return app