from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, ProdutoSimples, Usuario
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db, criar_bd

#criar_bd() # isso aqui vai ser substitutido por uma outra ferramenta 

app = FastAPI()

#CORS 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#PRODUTOS

@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model= ProdutoSimples)
def criar_produto(produto: Produto, db: Session =Depends(get_db) ):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado
    

@app.get('/produtos', response_model=List[Produto])
def listar_produtos(db: Session = Depends(get_db)):
    try:
        produtos = RepositorioProduto(db).listar()
        return produtos
    except:
        return{"msg": "deu algum problema"}



@app.get('/produtos/{produto_nome}')
def obter_produto(produto_nome, db: Session = Depends(get_db)):
    try:
        produto = RepositorioProduto(db).obter(produto_nome)
        return produto
    except:
        return{"msg":"produto nao existe"} 


@app.put('/produtos/{produto_id}', response_model = Produto)
def editar_produto(produto_id: int, produto : Produto, db: Session = Depends(get_db)):
    RepositorioProduto(db).editar(produto_id, produto)
    return produto



@app.delete('/produtos/{produto_id}', status_code=status.HTTP_200_OK)
def deletar_produto(produto_id, db: Session = Depends(get_db)):
    RepositorioProduto(db).remover(produto_id)
    return{"msg":"produto removido"}  #colocar o nome do produto na mensagem



#USUARIOS

@app.post('/usuarios', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuario(usuario: Usuario, db: Session =Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado


@app.get('/usuarios', response_model=List[Usuario])
def listar_usuario(db: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios


@app.get('/usuario/{usuario_nome}', status_code=status.HTTP_200_OK)
def obter_usuario():
    pass


@app.delete('/usuario/{usuario_nome}', status_code=status.HTTP_200_OK)
def deletar_usuario():
    pass