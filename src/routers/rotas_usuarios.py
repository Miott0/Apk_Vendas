from fastapi import APIRouter
from fastapi import APIRouter, FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Usuario
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db, criar_bd

router = APIRouter()
 


@router.post('/usuarios', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuario(usuario: Usuario, db: Session =Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado


@router.get('/usuarios', response_model=List[Usuario])
def listar_usuario(db: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios


@router.get('/usuario/{usuario_nome}', status_code=status.HTTP_200_OK)
def obter_usuario():
    pass


@router.delete('/usuario/{usuario_nome}', status_code=status.HTTP_200_OK)
def deletar_usuario():
    pass