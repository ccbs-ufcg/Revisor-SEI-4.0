from fastapi import APIRouter
from app.models.request import RevisaoRequest
from app.models.response import RevisaoResponse
from app.engine.revisao import revisar_texto

router = APIRouter(tags=["Revisão"])

@router.post("/revisar", response_model=RevisaoResponse)
def revisar(request: RevisaoRequest):
    return revisar_texto(request)
