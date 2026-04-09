import asyncio
from asyncua import Client
from app.core.config import settings
from app.core.logger import logger

# O sistema escala apenas adicionando itens aqui.
MAPA_EQUIPAMENTOS = {
    "RTG_01": {
        "balanca_pesagem": "ns=2;i=2",
        "sensor_acoplamento": "ns=2;i=3"
    },
    "RTG_02": {
        "balanca_pesagem": "ns=2;i=5",
        "sensor_acoplamento": "ns=2;i=6"
    }
}

class OpcUaService:
    def __init__(self):
        self.url = settings.opc_ua_server_url
        self.dados_maquinas = {} # Guarda os dados separados por máquina

    async def iniciar_leitura_ininterrupta(self):
        logger.info(f"Iniciando serviço OPC UA. Conectando em: {self.url}")
        
        while True:
            try:
                async with Client(url=self.url) as client:
                    logger.info("✅ Conexão estabelecida com sucesso!")
                    
                    while True:
                        # Varre todas as máquinas mapeadas
                        for maquina_id, tags in MAPA_EQUIPAMENTOS.items():
                            # Inicializa o dicionário da máquina se não existir
                            if maquina_id not in self.dados_maquinas:
                                self.dados_maquinas[maquina_id] = {}
                                
                            # Varre e lê as tags da máquina atual
                            for nome_amigavel, node_id in tags.items():
                                try:
                                    node = client.get_node(node_id)
                                    valor = await node.read_value()
                                    self.dados_maquinas[maquina_id][nome_amigavel] = valor
                                except Exception as e:
                                    logger.error(f"Erro ao ler {node_id} da {maquina_id}: {e}")
                        
                        await asyncio.sleep(2)
                        
            except Exception as e:
                logger.warning(f"⚠️ Reconectando em {settings.opc_ua_reconnect_timeout_sec}s... Erro: {e}")
                await asyncio.sleep(settings.opc_ua_reconnect_timeout_sec)

    def obter_dados_todas_maquinas(self) -> dict:
        return self.dados_maquinas
        
    def obter_dados_maquina(self, maquina_id: str) -> dict:
        maquina_id_formatado = maquina_id.upper()
        return self.dados_maquinas.get(maquina_id_formatado)

opcua_service = OpcUaService()