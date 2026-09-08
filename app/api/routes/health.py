from fastapi import APIRouter

router = APIRouter(tags=["Sistema"])

@router.get("/health")
def health():
    return {"status": "ok", "service": "revisor-sei-api"}
