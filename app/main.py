from fastapi import FastAPI

# Importando o roteador que criaremos a seguir
from app.api import endpoints

app = FastAPI(
    title="Anime Data Platform API",
    description="Uma API para servir dados de animes coletados da API Jikan.",
    version="1.0.0"
)

# Incluindo as rotas definidas em endpoints.py
app.include_router(endpoints.router)

@app.get("/", tags=["Root"])
def read_root():
    """Rota raiz para verificar se a API está no ar."""
    return {"message": "Bem-vindo à API de Animes!"}