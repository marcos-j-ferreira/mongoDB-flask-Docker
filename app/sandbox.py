from src.config.database import connect

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

objt = { 
    'type':"lazer",
    'tarefa':"assistir filme",
    'tempo':"dois dias",
    'estado':False
}

# InsertOneResult(ObjectId('682357377284cb5f5af667a2'), acknowledged=True)

a = insertDate(objt)

print(a)