import re
from app.models.response import Problema

def verificar_pontuacao(texto: str):
    problemas = []
    for match in re.finditer(r"\s+([,.;:!?])", texto):
        trecho = match.group(0)
        problemas.append(Problema(
            id="PT001",
            categoria="pontuacao",
            gravidade="baixa",
            trecho=trecho,
            sugestao=match.group(1),
            explicacao="Não deve haver espaço antes de vírgula, ponto ou outro sinal de pontuação."
        ))
    return problemas
