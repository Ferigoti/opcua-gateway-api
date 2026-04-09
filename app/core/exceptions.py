# app/core/exceptions.py
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from app.core.logger import logger

async def global_exception_handler(request: Request, exc: Exception):
    """ Captura erros críticos não previstos (Erro 500) """
    logger.error(f"Erro Crítico não tratado: {exc}")
    
    return JSONResponse(
        status_code=500,
        content={
            "enTag": "INTERNAL.SERVER_ERROR", 
            "errorMessage": "Ocorreu um erro interno no servidor. A equipe já foi notificada."
        }
    )

async def http_exception_handler(request: Request, exc: HTTPException):
    """ Captura os erros normais de regra de negócio lançados nas rotas """
    if isinstance(exc.detail, dict) and "enTag" in exc.detail:
        conteudo = exc.detail
    else:
        conteudo = {
            "enTag": f"HTTP_ERROR_{exc.status_code}",
            "errorMessage": str(exc.detail)
        }

    return JSONResponse(status_code=exc.status_code, content=conteudo)