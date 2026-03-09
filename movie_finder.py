import requests

API_KEY = "09b46d881337aa89abbbc6036f7cbc34"

# Dicionário simples para converter IDs em nomes de gêneros
GENRES = {28: "Ação", 12: "Aventura", 16: "Animação", 35: "Comédia", 80: "Crime", 99: "Documentário", 18: "Drama", 10751: "Família", 14: "Fantasia", 36: "História", 27: "Terror", 10402: "Música", 9648: "Mistério", 10749: "Romance", 878: "Ficção Científica", 10770: "Cinema TV", 53: "Suspense", 10752: "Guerra", 37: "Faroeste"}

def buscar_filme():
    try:
        url = f"https://api.themoviedb.org/3/trending/movie/day?api_key={API_KEY}&language=pt-BR"
        r = requests.get(url)
        r.raise_for_status() # Verifica se a requisição deu certo
        data = r.json()
        
        if data["results"]:
            filme = data["results"][0]
            genero_id = filme["genre_ids"][0]
            
            return {
                "titulo": filme["title"],
                "ano": filme["release_date"][:4],
                "sinopse": filme["overview"],
                "genero": GENRES.get(genero_id, "Outros")
            }
    except Exception as e:
        return f"Erro ao buscar filme: {e}"

# Testando a função
print(buscar_filme())