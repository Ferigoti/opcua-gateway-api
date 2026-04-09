# Usa uma imagem oficial, leve e estável do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia apenas o arquivo de requisitos primeiro
COPY requirements.txt .

# Instala as bibliotecas sem guardar cache (deixa a imagem mais leve)
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o resto do projeto para dentro do container
COPY . .

# Expõe a porta que a API vai rodar
EXPOSE 8000

# Comando para iniciar o servidor (apontando para o maestro main.py)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]