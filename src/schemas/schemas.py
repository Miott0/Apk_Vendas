
from pydantic import BaseModel
from typing import Optional, List


class ProdutoSimples(BaseModel):
    nome: str 
    preco: float 
    disonivel: bool = True
    


    class Config:
        orm_mode = True



class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str 
    senha: str
    produtos : List[ProdutoSimples] = []

    class Config:
        orm_mode = True


class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str

    class Config:
        orm_mode = True



class Produto(BaseModel):
    id: Optional[int] = None
    nome: str 
    detalhes: str 
    preco: float 
    disonivel: bool = True
    usuario_id: Optional[int]
    usuario: Optional[UsuarioSimples]

    class Config:
        orm_mode = True


class Pedido(BaseModel):
    id: Optional[str] = None
    quantidade: int
    entrega: bool = True
    observacoes: Optional[str] = 'Sem obrservações'

    class Config:
        orm_mode = True

