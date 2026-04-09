from fastapi import APIRouter, HTTPException
from app.services.opcua_service import opcua_service

# Cria o roteador
router = APIRouter(prefix="/api/v1/equipamentos", tags=["Equipamentos v1"])

@router.get("", summary="Lista os dados de todos os equipamentos")
async def get_todos_equipamentos():
    dados = opcua_service.obter_dados_todas_maquinas()
    if not dados:
        raise HTTPException(
            status_code=503, 
            detail={
                "enTag": "OPC_UA.NO_DATA",
                "errorMessage": "Aguardando coleta de dados do chão de fábrica..."
            }
        )
    
    return {
        "status": "sucesso",
        "total_equipamentos": len(dados),
        "dados": dados
    }

@router.get("/{maquina_id}", summary="Busca os dados de um equipamento específico")
async def get_equipamento(maquina_id: str):
    dados = opcua_service.obter_dados_maquina(maquina_id)
    if not dados:
        raise HTTPException(
            status_code=404, 
            detail={
                "enTag": "OPC_UA.EQUIPMENT_NOT_FOUND",
                "errorMessage": f"Equipamento '{maquina_id}' não encontrado ou sem dados na memória."
            }
        )
    
    return {
        "status": "sucesso",
        "maquina_id": maquina_id,
        "dados": dados
    }