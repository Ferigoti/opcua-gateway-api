# 🏗️ Gateway de Integração Industrial (OPC UA)

API desenvolvida em Python (FastAPI) para atuar como middleware de comunicação direta com maquinário e CLPs industriais utilizando o protocolo de rede OPC UA. 

O projeto foi construído para cenários de missão crítica, seguindo rigorosos padrões arquiteturais (Clean Architecture, Clean Code e observabilidade estruturada), focado em alta disponibilidade, resiliência de rede e conteinerização.

## 🚀 Tecnologias e Padrões
* **Backend:** Python 3.14, FastAPI
* **Protocolo Industrial:** OPC UA (via biblioteca assíncrona `asyncua`)
* **Arquitetura:** Layered Architecture (Core, API, Services, Models)
* **Infraestrutura:** Docker
* **Padrões aplicados:** Tratamento de erros global (sem vazamento de stacktrace), logs padronizados e injeção de dependências via variáveis de ambiente.

## 📦 Estrutura do Projeto
A aplicação foi modularizada para isolar responsabilidades de negócio e infraestrutura:
* `/app/core`: Configurações de ambiente (`.env`), Logger estruturado global e Exception Handlers para respostas padronizadas.
* `/app/models`: DTOs (Data Transfer Objects) e schemas de validação com Pydantic e documentação Swagger.
* `/app/services`: Regras de negócio, mapeamento de NodeIDs e cliente assíncrono de leitura em background para o OPC UA.
* `/app/api`: Rotas e endpoints REST.

## ⚙️ Como Executar Localmente (Ambiente de Testes)

Para facilitar os testes sem a necessidade de um CLP físico, o projeto acompanha um **Servidor Mock** (`mock_server.py`) que simula o comportamento dos equipamentos industriais gerando dados de sensores em tempo real.

**1. Clone o repositório e prepare o ambiente:**
```bash
git clone [https://github.com/Ferigoti/seu-repositorio.git](https://github.com/Ferigoti/seu-repositorio.git)

cd seu-repositorio

cp .env.example .env
```

**2. Inicie o Servidor Mock (Terminal 1):**
```bash
python mock_server.py
```

**3. Execute a API principal com Docker (Terminal 2):**

```bash
docker build -t opcua-gateway-api .
docker run -p 8000:8000 --env-file .env opcua-gateway-api
```

**4. Acesse a Documentação e Teste as Rotas:**

Abra o navegador em: http://127.0.0.1:8000/docs para acessar a interface do Swagger UI. Você poderá testar a rota de observabilidade (/health) e a leitura dos equipamentos simulados (/api/v1/equipamentos).
