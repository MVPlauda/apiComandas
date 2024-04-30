import db
from sqlalchemy import Column, VARCHAR, Integer, FLOAT, BLOB
# ORM

class ProdutoDB(db.Base):
    __tablename__ = 'tb_produto'
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    valor_unitario = Column(FLOAT(precision=10, decimal_return_scale=None), nullable=False)
    foto = Column(BLOB, nullable=False)
    descricao = Column(VARCHAR(255), nullable=False)

    def __init__(self, id, nome, valor_unitario, foto, descricao):
        self.id = id
        self.nome = nome
        self.valor_unitario = valor_unitario
        self.foto = foto
        self.descricao = descricao