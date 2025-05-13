from db import db

#client = MongoClient(uri, server_api=ServerApi('1'))

#data = db.colecao

# def connectDB():
#     try:
#         client.admin.command('ping')
#         return True
#     except Exception as e:
#         print(e)

def firtData()a:
    colecao = db["usuarios"]

    # if not connectDB():
    #     print("banco de dados não conectado ")

    try:
        user = {
            'name':"Ana",
            'age':19
        }

        result = colecao.insert_one(a)

        print({"id_inserido": str(result.inserted_id)})
    
    except Exception as e:
        print("Erro", e)

def search_all():

    colecao = db["usuarios"]

    try:

        for doc in colecao.find():
            print(f"{doc['name']} {doc['age']}")


            # Resposta, todos os usuários e suas idades

            # marcos 20
            # Luiz 20
            # Ana 19

    except Exception as e:
        print(f"Error: {e}")

def search ():

    colecao = db["usuarios"]
    
    try:

        for doc in colecao.find({'name':"Luiz"}):
            print(f"Usuário: {doc['name']} Tem: {doc['age']} anos")

            # filtrar por um usuario especifico 

            #Usuário: Luiz Tem: 20 anos



    except Exception as e:
        print(f"Erro: {e}")

obj = {
    
}

#firtData(a)