from sqlalchemy import create_engine, inspect
from app.models.anime import Base
from app.core.config import settings

# Criamos o engine fora da função para que possa ser reutilizado
engine = create_engine(settings.DATABASE_URL)

def create_tables():
    """Cria as tabelas no banco de dados se elas não existirem."""
    inspector = inspect(engine)
    if not inspector.has_table("animes"):
        print("Criando tabela 'animes'...")
        Base.metadata.create_all(bind=engine)
        print("Tabela 'animes' criada com sucesso!")
    else:
        print("Tabela 'animes' já existe.")

if __name__ == "__main__":
    create_tables()