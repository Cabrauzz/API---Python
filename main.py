#api com FASTAPI - 26/01/2022
#uvicorn main:app --reload
#http://127.0.0.1:8000/docs      para acessar a documentação da api

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def raiz():
    return {"Olá: Mundo"}

#criação da classe

class usuario(BaseModel):
    id: int
    email: str
    senha: str

#base de dados

base_de_dados = [

    usuario(id = 1, email = "vitor.csaluno@faculdadeimpacta.com.br", senha = "vitor123"),
    usuario(id = 2, email = "vitor.cs11@gmail.com", senha = "palmeiras1914")
]

@app.get("/usuario")
def get_todos_usuarios():
    return base_de_dados

# retornar por id

@app.get("/usuario/{id_usuario}")
def get_usuario_id(id_usuario: int):
    for usuario in base_de_dados:
        if usuario.id == id_usuario:
            return usuario
    return{"Status": 404, "Aviso": "Não encontrado"}

# acrescentar novos usuario no sistema

@app.post("/usuario")
def inserir_usuario(usuario: usuario):
    base_de_dados.append(usuario)
    return usuario

# retornar senha
@app.get("/usuario/{senha_usuario}")
def get_usuario_senha(senha_usuario: str):
    for x in base_de_dados:
        if usuario.senha == senha_usuario:
            return x
    return ("Senha inválida")
