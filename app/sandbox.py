from src.config.database import connect

app = connect()

def insertDate():

    exp = {
        'type':"lazer",
        'tarefa':"assistir filme",
        'tempo': "1 hora",
        'estado': False
    }

    nameColecao = exp['type']
    
    print(nameColecao)

insertDate()