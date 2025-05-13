from config.database import connect

app = connect()

def insertDate(obj):

    data = {
        'tarefa':obj['tarefa'],
        'tempo':obj['tempo'],
        'estado':obj['estado']
    }
    if app is None:
        return "Erro com banco de dados"
    
    if  not isinstance(obj, dict) or not obj:
        return "Dados vazios"
    try:
        nameColecao = app[obj['type']]
        result = nameColecao.insert_one(data)

        return f"Tarefa adiciona com sucesso"
    
    except Exception as e:
        return f"Erro no servidor: {e}"

    # exp = {
    #     'type':"lazer",
    #     'tarefa':"assistir filme",
    #     'tempo': "1 hora",
    #     'estado': False
    # }
# Esse serviço vai receber qutros dados, como:
# tipo: lazer, estuods, jogos -> que será coleções
# tarefa: O que ele vai ter que fazer
# tempo: Quanto tempo ele tem para fazer a tarefa 
# estado: se a tafera já foi concluida ou não


