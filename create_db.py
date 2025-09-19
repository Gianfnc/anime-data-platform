from sqlalchemy import create_engine
from app.models.anime import Base
from app.core.config import settings

def main():
    print("Criando tabelas no banco de dados...")
    engine = create_engine(settings.DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso!")

if __name__ == "__main__":
    main()