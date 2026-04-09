# app/api/health.py
from fastapi import APIRouter
from app.core.config import settings
from app.services.opcua_service import opcua_service

router = APIRouter(tags=["Observabilidade"])

@router.get("/health", summary="Verifica a saúde do container")
async def health_check():
    """
    Endpoint consumido pelo orquestrador (Docker/Kubernetes).
    """
    return {
        "status": "UP", 
        "ambiente": settings.environment,
        "conexoes_ativas": len(opcua_service.obter_dados_todas_maquinas())
    }