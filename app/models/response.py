from typing import List
from pydantic import BaseModel

class Problema(BaseModel):
    id: str
    categoria: str
    gravidade: str
    trecho: str
    sugestao: str
    explicacao: str

class RevisaoResponse(BaseModel):
    nota: int
    total_problemas: int
    problemas: List[Problema]
