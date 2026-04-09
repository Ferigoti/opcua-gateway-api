from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    api_title: str
    api_port: int
    environment: str

    # OPC UA
    opc_ua_server_url: str
    opc_ua_reconnect_timeout_sec: int

    # Diz ao pydantic para ler do arquivo .env
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

# Instância global das configurações
settings = Settings()