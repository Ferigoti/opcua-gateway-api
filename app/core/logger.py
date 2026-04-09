import logging
import sys
from app.core.config import settings

def setup_logger():
    # Formato padronizado: [DATA HORA] [NÍVEL] [ARQUIVO] - MENSAGEM
    log_format = "%(asctime)s [%(levelname)s] [%(name)s] - %(message)s"
    
    # Define o nível de log baseado no ambiente
    log_level = logging.DEBUG if settings.environment == "development" else logging.INFO

    logging.basicConfig(
        level=log_level,
        format=log_format,
        handlers=[
            logging.StreamHandler(sys.stdout) # Joga os logs no console
        ]
    )
    return logging.getLogger("porto_app")

# Instância global do logger
logger = setup_logger()