from sqlalchemy.orm import Session
from sqlalchemy import delete, select, update
from src.schemas import schemas
from src.infra.sqlalchemy.models import models



class RepositorioProduto():

    def __init__(self, db: Session):
        self.db = db


    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(nome = produto.nome, 
                                    detalhes = produto.detalhes,
                                    preco = produto.preco,
                                    disponivel = produto.disonivel, 
                                    usuario_id = produto.usuario_id)

        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto                            


    def listar(self):
        produtos = self.db.query(models.Produto).all()
        return produtos


    def obter(self, produto_nome: str):
        stmt = select(models.Produto).where(models.Produto.nome==produto_nome)
        produto = self.db.execute(stmt).one()
        return produto


    def remover(self, produto_id:int):
        stmt = delete(models.Produto).where(models.Produto.id==produto_id)
        self.db.execute(stmt)
        self.db.commit()


    def editar(self,produto_id:int,  produto: schemas.Produto):

        update_stmt = update(models.Produto).where(models.Produto.id == produto_id).values(nome = produto.nome,
                                                                                            detalhes = produto.detalhes,
                                                                                            preco = produto.preco,
                                                                                            disponivel = produto.disonivel)

        self.db.execute(update_stmt)
        self.db.commit()



