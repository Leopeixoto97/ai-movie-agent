import google.generativeai as genai
import os

# Configuramos a chave do Gemini que você vai pegar no AI Studio
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def gerar_legenda(info):
    # O prompt continua a mesma ideia, o que muda é como chamamos a IA
    prompt = f"""
    Crie uma legenda para Instagram.
    
    Filme: {info['titulo']}
    Ano: {info['ano']}
    Sinopse: {info['sinopse']}
    
    Inclua 5 hashtags.
    """

    try:
        # Selecionamos o modelo 1.5 Flash (é o mais rápido e gratuito)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        
        # O Gemini retorna o texto direto no atributo .text
        return response.text
    except Exception as e:
        print(f"Erro ao gerar legenda com Gemini: {e}")
        # Retorno de segurança caso a API falhe (o famoso 'fallback')
        return f"Assista {info['titulo']}! #cinema #filmes #reels #dicas #movie"