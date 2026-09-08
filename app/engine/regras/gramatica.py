from app.models.response import Problema

PADROES = [
    ("duas permanencia", "duas permanências", "GR001"),
    ("das documentação", "da documentação", "GR002"),
    ("os documentação", "a documentação", "GR003"),
    ("as documento", "o documento", "GR004"),
]

def verificar_gramatica(texto: str):
    problemas = []
    for errado, correto, codigo in PADROES:
        if errado.lower() in texto.lower():
            trecho = _preservar_caso(texto, errado)
            problemas.append(Problema(
                id=codigo,
                categoria="gramatica",
                gravidade="alta",
                trecho=trecho,
                sugestao=correto,
                explicacao="A construção apresenta erro de concordância ou flexão nominal."
            ))
    return problemas

def _preservar_caso(texto, alvo):
    pos = texto.lower().find(alvo.lower())
    return texto[pos:pos+len(alvo)] if pos >= 0 else alvo
