# app/models/schemas.py
from pydantic import BaseModel, Field

class ComandoEquipamento(BaseModel):
    """
    DTO (Data Transfer Object) para envio de comandos de escrita aos equipamentos via OPC UA.
    """
    tag: str = Field(
        ..., 
        title="Nome da Tag",
        description="Nome amigável da tag configurada no mapa (ex: balanca_pesagem)",
    )
    valor: float | bool = Field(
        ..., 
        title="Novo Valor do Equipamento",
        description="O valor que será escrito diretamente no CLP da máquina.",
    )

    # O ConfigDict cria exemplos visuais na tela do Swagger do FastAPI
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "tag": "balanca_pesagem",
                    "valor": 35.5
                }
            ]
        }
    }