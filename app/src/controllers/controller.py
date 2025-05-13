from flask import Flask, jsonify
from models.model import *


def insertTask(data):
    
    if  not isinstance(data, dict) or not data:
        return "Dados vazios"
    
    try:

        db = {
            'type':str(data['type']),
            'tarefa':str(data['tarefa']),
            'tempo':str(data['tempo']),
            'estado':bool(data['estado'])

        }

        insertDate(db)
        
    except Exception as e:
        return jsonify(error="Dados invalidos")


def hello():
    return jsonify(messagen="Sua Api está rodando com sucesso!!")



