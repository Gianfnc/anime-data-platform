from contextlib import asynccontextmanager
from fastapi import FastAPI

# Nossas importações para a inicialização
from app.api import endpoints
from create_db import create_tables
from load_data import load_initial_data

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código que será executado ANTES da aplicação começar a receber requisições
    print("Iniciando a aplicação...")
    print("Verificando e preparando o banco de dados...")
    create_tables()       # Cria a tabela se não existir
    load_initial_data()   # Carrega os dados se a tabela estiver vazia
    print("Setup do banco de dados concluído.")
    
    yield  # A aplicação roda aqui
    
    # Código que será executado DEPOIS que a aplicação for finalizada (não usaremos, mas é bom saber)
    print("Aplicação finalizada.")


app = FastAPI(
    lifespan=lifespan, # Adicionamos o lifespan aqui
    title="Anime Data Platform API",
    description="Uma API para servir dados de animes coletados da API Jikan.",
    version="1.0.0"
)

app.include_router(endpoints.router)

@app.get("/", tags=["Root"])
def read_root():
    """Rota raiz para verificar se a API está no ar."""
    return {"message": "Bem-vindo à API de Animes!"}