from app.models.response import Problema
from app.engine.regras.gramatica import verificar_gramatica
from app.engine.regras.pontuacao import verificar_pontuacao
from app.engine.regras.redacao_oficial import verificar_redacao_oficial

def aplicar_regras(texto: str, tipo_documento: str, perfil: str, unidade: str | None):
    problemas = []
    problemas.extend(verificar_gramatica(texto))
    problemas.extend(verificar_pontuacao(texto))
    problemas.extend(verificar_redacao_oficial(texto, tipo_documento))
    return problemas

def listar_regras():
    return [
        {"id": "GR001", "categoria": "gramatica", "descricao": "Concordância nominal em erro conhecido."},
        {"id": "PT001", "categoria": "pontuacao", "descricao": "Espaços indevidos antes de pontuação."},
        {"id": "RO001", "categoria": "redacao_oficial", "descricao": "Substituição de expressões prolixas por redação objetiva."},
        {"id": "RO002", "categoria": "redacao_oficial", "descricao": "Identificação de gerundismo em construções administrativas."},
    ]
