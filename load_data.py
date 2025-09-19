from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.models.anime import Anime
from app.services.jikan_collector import fetch_top_animes
from create_db import engine # Importando o engine do create_db

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def load_initial_data():
    """Busca dados da API e carrega no banco de dados."""
    db = SessionLocal()
    try:
        # Verifica se já existem dados na tabela
        if db.query(Anime).count() > 0:
            print("O banco de dados já contém dados. Abortando a carga inicial.")
            return

        print("Iniciando o processo de carga de dados inicial...")
        animes_data = fetch_top_animes()
        
        if not animes_data:
            print("Nenhum dado de anime foi encontrado para carregar.")
            return

        print(f"{len(animes_data)} animes encontrados. Processando e salvando no banco...")
        for anime_data in animes_data:
            genres_list = [genre['name'] for genre in anime_data.get('genres', [])]
            genres_str = ", ".join(genres_list)
            new_anime = Anime(
                id=anime_data['mal_id'],
                title=anime_data.get('title_english') or anime_data.get('title'),
                score=anime_data.get('score'),
                genres=genres_str,
                synopsis=anime_data.get('synopsis')
            )
            db.add(new_anime)
        
        db.commit()
        print("✅ Dados iniciais carregados com sucesso no banco de dados!")
        
    except Exception as e:
        print(f"❌ Ocorreu um erro durante a carga de dados: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    load_initial_data()