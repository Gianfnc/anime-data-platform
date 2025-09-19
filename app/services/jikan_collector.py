import httpx
import time

# URL base da API Jikan para buscar os animes mais populares
JIKAN_API_URL = "https://api.jikan.moe/v4/top/anime"

def fetch_top_animes():
    """
    Busca os animes mais populares da API Jikan.
    """
    print("Iniciando a busca por animes na API Jikan...")
    try:
        # Faz a requisição para a API
        response = httpx.get(JIKAN_API_URL, timeout=30.0)

        # Levanta um erro se a resposta não for bem-sucedida (ex: erro 404, 500)
        response.raise_for_status()

        # Extrai os dados em formato JSON
        json_data = response.json()

        print("Busca realizada com sucesso!")

        # A API retorna os animes dentro de uma chave 'data'
        return json_data.get("data", [])

    except httpx.RequestError as e:
        print(f"Ocorreu um erro ao fazer a requisição para a API: {e}")
        return []

    # Pausa de 1 segundo para não sobrecarregar a API com muitas requisições
    time.sleep(1)