import re
from app.models.request import RevisaoRequest
from app.models.response import RevisaoResponse, Problema
from app.engine.regras import aplicar_regras

def revisar_texto(request: RevisaoRequest) -> RevisaoResponse:
    problemas = aplicar_regras(
        request.texto,
        tipo_documento=request.tipo_documento,
        perfil=request.perfil,
        unidade=request.unidade,
    )

    # Nota inicial simples; futuramente poderá usar pesos por categoria/gravidade.
    penalidade = sum({"alta": 8, "media": 5, "baixa": 2}.get(p.gravidade, 2) for p in problemas)
    nota = max(0, min(100, 100 - penalidade))

    return RevisaoResponse(
        nota=nota,
        total_problemas=len(problemas),
        problemas=problemas,
    )
