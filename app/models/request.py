from typing import Optional
from pydantic import BaseModel, Field

class RevisaoRequest(BaseModel):
    texto: str = Field(..., min_length=1, description="Texto do documento a revisar.")
    tipo_documento: str = Field(default="outro")
    perfil: str = Field(default="ufcg")
    unidade: Optional[str] = Field(default=None, description="Ex.: CCBS")
