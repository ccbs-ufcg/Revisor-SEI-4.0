from fastapi import APIRouter
from app.engine.regras import listar_regras

router = APIRouter(tags=["Regras"])

@router.get("/regras")
def regras():
    return {"regras": listar_regras()}

@router.get("/tipos-documento")
def tipos_documento():
    return {
        "tipos": [
            {"id": "oficio", "nome": "Ofício"},
            {"id": "despacho", "nome": "Despacho"},
            {"id": "parecer", "nome": "Parecer"},
            {"id": "relatorio", "nome": "Relatório"},
            {"id": "comunicado", "nome": "Comunicado"},
            {"id": "outro", "nome": "Outro"},
        ]
    }
