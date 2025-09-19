from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Importando os nossos módulos
from app.core.config import settings
from app.models.anime import Anime
from app.services.jikan_collector import fetch_top_animes

# Configuração da conexão com o banco de dados
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def load_data_to_db():
    """
    Função principal para buscar dados da API e carregar no banco de dados.
    """
    print("Iniciando o processo de carga de dados...")
    db = SessionLocal()

    try:
        # 1. EXTRAIR (Extract): Buscar os dados da API
        animes_data = fetch_top_animes()

        if not animes_data:
            print("Nenhum dado de anime foi encontrado para carregar.")
            return

        print(f"{len(animes_data)} animes encontrados. Processando e salvando no banco...")

        for anime_data in animes_data:
            # 2. TRANSFORMAR (Transform): Limpar e preparar os dados

            # Juntando a lista de gêneros em uma única string
            genres_list = [genre['name'] for genre in anime_data.get('genres', [])]
            genres_str = ", ".join(genres_list)

            # Criando um objeto do nosso modelo Anime
            new_anime = Anime(
                id=anime_data['mal_id'],
                title=anime_data.get('title_english') or anime_data.get('title'),
                score=anime_data.get('score'),
                genres=genres_str,
                synopsis=anime_data.get('synopsis')
            )

            # 3. CARREGAR (Load): Adicionar ao banco de dados
            db.add(new_anime)

        # Confirma (commita) todas as adições de uma vez
        db.commit()
        print("✅ Dados carregados com sucesso no banco de dados!")

    except Exception as e:
        print(f"❌ Ocorreu um erro durante a carga de dados: {e}")
        db.rollback() # Desfaz as alterações em caso de erro
    finally:
        db.close() # Fecha a conexão com o banco

if __name__ == "__main__":
    load_data_to_db()