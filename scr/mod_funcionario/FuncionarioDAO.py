from fastapi import APIRouter
from fastapi import Depends
import db 
from mod_funcionario.FuncionarioModel import FuncionarioDB
from mod_funcionario.Funcionario import Funcionario

from security import get_current_active_user, User

router = APIRouter(dependencies=[Depends(get_current_active_user)])


# Criar os endpoints de Funcionario: GET, POST, PUT, DELETE
@router.get("/funcionario/", tags=["Funcionário"], dependencies=[Depends(get_current_active_user)],)
def get_funcionario():
    try:
        session = db.Session()
        # busca todos
        dados = session.query(FuncionarioDB).all()
        return dados, 200
    except Exception as e:
        return {"msg": "Erro ao listar", "erro": str(e)}, 404
    finally:
        session.close()

# Criar os endpoints de Funcionario: GET, POST, PUT, DELETE
@router.get("/funcionario/{id}", tags=["Funcionário"], dependencies=[Depends(get_current_active_user)],)
def get_funcionario(id: int):
    try:
        session = db.Session()
        # busca um com filtro
        dados = session.query(FuncionarioDB).filter(FuncionarioDB.id == id).all()
        return dados, 200
    except Exception as e:
        return {"msg": "Erro ao listar", "erro": str(e)}, 404
    finally:
        session.close()

@router.post("/funcionario/", tags=["Funcionário"])
def post_funcionario(corpo: Funcionario):
    try:
        session = db.Session()
        dados = FuncionarioDB(None, corpo.nome, corpo.matricula, corpo.cpf, corpo.telefone, corpo.grupo, corpo.senha)

        session.add(dados)
        session.commit()
        return {"msg": "Cadastrado com sucesso!", "id": dados.id}, 200
    except Exception as e:
        session.rollback()
        return {"msg": "Erro ao cadastrar", "erro": str(e)}, 406
    finally:
        session.close()


@router.put("/funcionario/{id}", tags=["Funcionário"])
def put_funcionario(id: int, corpo: Funcionario):
    try:
        session = db.Session()
        dados = session.query(FuncionarioDB).filter(FuncionarioDB.id == id).one()
        dados.nome = corpo.nome
        dados.cpf = corpo.cpf
        dados.telefone = corpo.telefone
        dados.senha = corpo.senha
        dados.matricula = corpo.matricula
        dados.grupo = corpo.grupo
        session.add(dados)
        session.commit()
        return {"id": dados.id}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.delete("/funcionario/{id}", tags=["Funcionário"])
def delete_funcionario(id: int):
    try:
        session = db.Session()
        dados = session.query(FuncionarioDB).filter(FuncionarioDB.id == id).one()
        session.delete(dados)
        session.commit()
        return {"id": dados.id}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()