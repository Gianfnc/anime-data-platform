# 1. Use uma imagem oficial do Python como base
FROM python:3.13-slim

# 2. Defina o diretório de trabalho dentro do container
WORKDIR /app

# 3. Copie o arquivo de dependências primeiro (isso otimiza o cache do Docker)
COPY requirements.txt .

# 4. Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copie o resto do código da sua aplicação para dentro do container
COPY ./app /app

# 6. Defina o comando que será executado quando o container iniciar
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]