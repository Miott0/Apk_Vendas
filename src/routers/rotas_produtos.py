from fastapi import APIRouter, FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, ProdutoSimples
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.config.database import get_db, criar_bd


router = APIRouter()



@router.post('/produtos', status_code=status.HTTP_201_CREATED, response_model= ProdutoSimples)
def criar_produto(produto: Produto, db: Session =Depends(get_db) ):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado
    

@router.get('/produtos', response_model=List[Produto])
def listar_produtos(db: Session = Depends(get_db)):
    try:
        produtos = RepositorioProduto(db).listar()
        return produtos
    except:
        return{"msg": "deu algum problema"}



@router.get('/produtos/{produto_nome}')
def obter_produto(produto_nome, db: Session = Depends(get_db)):
    try:
        produto = RepositorioProduto(db).obter(produto_nome)
        return produto
    except:
        return{"msg":"produto nao existe"} 


@router.put('/produtos/{produto_id}', response_model = Produto)
def editar_produto(produto_id: int, produto : Produto, db: Session = Depends(get_db)):
    RepositorioProduto(db).editar(produto_id, produto)
    return produto



@router.delete('/produtos/{produto_id}', status_code=status.HTTP_200_OK)
def deletar_produto(produto_id, db: Session = Depends(get_db)):
    RepositorioProduto(db).remover(produto_id)
    return{"msg":"produto removido"}  #colocar o nome do produto na mensagem