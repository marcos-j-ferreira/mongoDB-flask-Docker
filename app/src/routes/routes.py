from flask import Blueprint, request
from src.controllers import controller

tarefas = Blueprint('tarefas', __name__)

@tarefas.route('/', methods=['GET'])

def hello():
    return controller.hello()

@tarefas.route('/adicionar', methods=['POST'])

def add():
    dados = request.get_json()
    return controller.insertTask(dados)
