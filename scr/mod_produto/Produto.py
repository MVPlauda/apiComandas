
from pydantic import BaseModel

class Produto(BaseModel):
    id: int = None
    nome: str = None
    valor_unitario: float
    descricao: str = None
    foto: bytes