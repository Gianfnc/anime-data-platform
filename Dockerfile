# 1. Use uma imagem oficial do Python como base
FROM python:3.13-slim

# 2. Defina o diretório de trabalho dentro do container
WORKDIR /app

# 3. Adicione o diretório de trabalho ao PYTHONPATH (A CORREÇÃO!)
ENV PYTHONPATH="${PYTHONPATH}:/app"

# 4. Copie o arquivo de dependências primeiro
COPY requirements.txt .

# 5. Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copie o resto do código da sua aplicação
COPY . .

# 7. Defina o comando que será executado quando o container iniciar
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]