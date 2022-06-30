from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base



class Usuario(Base):
    __tablename__ = 'Usuario'

    id = Column(Integer, primary_key = True, index = True)
    nome = Column(String)
    telefone = Column(String)
    senha = Column(String)

    produtos = relationship('Produto', back_populates = 'usuario')
    


class Produto(Base):

    __tablename__ = 'Produto'

    id = Column(Integer, primary_key = True, index = True)
    nome = Column(String)
    preco = Column(Float)
    detalhes = Column(String)
    disponivel = Column(Boolean)
    tamanhos = Column(String)
    usuario_id = Column(Integer, ForeignKey('Usuario.id', name='fk_usuario'))

    usuario = relationship("Usuario", back_populates = 'produtos')

