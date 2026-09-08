import re
from app.models.response import Problema

SUBSTITUICOES = [
    ("venho por meio deste solicitar", "solicito", "RO001"),
    ("venho através deste solicitar", "solicito", "RO002"),
    ("através deste", "por meio deste", "RO003"),
]

def verificar_redacao_oficial(texto: str, tipo_documento: str):
    problemas = []

    for errado, correto, codigo in SUBSTITUICOES:
        match = re.search(re.escape(errado), texto, flags=re.IGNORECASE)
        if match:
            problemas.append(Problema(
                id=codigo,
                categoria="redacao_oficial",
                gravidade="media",
                trecho=match.group(0),
                sugestao=correto,
                explicacao="A redação administrativa pode ser simplificada para maior objetividade."
            ))

    if re.search(r"\b(vai estar|vamos estar|irá estar|estará sendo)\b", texto, re.IGNORECASE):
        problemas.append(Problema(
            id="RO004",
            categoria="redacao_oficial",
            gravidade="media",
            trecho="construção com gerundismo",
            sugestao="Reescrever a frase de forma direta.",
            explicacao="Evite construções burocráticas e gerundismo quando uma forma verbal simples transmitir a mesma ideia."
        ))

    return problemas
