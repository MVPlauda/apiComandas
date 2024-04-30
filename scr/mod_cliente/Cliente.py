
from pydantic import BaseModel
class Cliente(BaseModel):
    id: int = None
    nome: str
    matricula: str
    cpf: str
    telefone: str = None
    login: str = None
    senha: str = None
    