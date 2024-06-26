import db
from sqlalchemy import Column, VARCHAR, CHAR, Integer
# ORM

class ClienteDB(db.Base):
    __tablename__ = 'tb_cliente'
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    matricula = Column(CHAR(10), nullable=False)
    cpf = Column(CHAR(15), unique=True, nullable=False)
    telefone = Column(CHAR(15), nullable=False)
    login = Column(VARCHAR(200), nullable=False)
    senha = Column(VARCHAR(200), nullable=False)

    def __init__(self, id, nome, matricula, cpf, telefone,login, senha):
        self.id = id
        self.nome = nome
        self.matricula = matricula
        self.cpf = cpf
        self.telefone = telefone
        self.login = login
        self.senha = senha