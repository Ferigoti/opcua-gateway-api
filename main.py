# main.py
import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, HTTPException 
from app.core.config import settings
from app.core.logger import logger
from app.core.exceptions import global_exception_handler, http_exception_handler
from app.services.opcua_service import opcua_service

# Importação das Rotas
from app.api.routes import router as equipamentos_router
from app.api.health import router as health_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Inicializando o Servidor Porto+...")
    task = asyncio.create_task(opcua_service.iniciar_leitura_ininterrupta())
    yield 
    logger.info("🛑 Encerrando conexões com o maquinário...")
    task.cancel()

app = FastAPI(
    title=settings.api_title,
    version="1.0.0",
    lifespan=lifespan
)

# Registra o Tratador Global de Erros (interceptação de segurança)
app.add_exception_handler(Exception, global_exception_handler)

# Registra as Rotas (Controllers)
app.include_router(health_router)
app.include_router(equipamentos_router)

# Registra os tratadores de erros
app.add_exception_handler(Exception, global_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)