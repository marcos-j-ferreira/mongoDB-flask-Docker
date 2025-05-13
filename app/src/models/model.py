from config.database import connect

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

# Esse serviço vai receber qutros dados, como:
# tipo: lazer, estuods, jogos -> que será coleções
# tarefa: O que ele vai ter que fazer
# tempo: Quanto tempo ele tem para fazer a tarefa 
# estado: se a tafera já foi concluida ou não


