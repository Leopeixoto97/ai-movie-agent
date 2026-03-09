import threading
from flask import Flask
import os
import movie_finder
import video_downloader
import clip_creator
import caption_generator
import instagram_poster

# --- SERVIDOR DE "SAÚDE" PARA O RAILWAY ---
app = Flask(__name__)

@app.route('/')
def health_check():
    # Isso diz ao Railway: "Estou vivo, não me derrube!"
    return "Automação Rodando!", 200

def rodar_servidor_web():
    # Aqui entra o que você perguntou: pegando a porta do ambiente
    porta = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=porta)

# --- SUA LÓGICA DE AUTOMAÇÃO ---
def executar_automacao_completa():
    print("--- INICIANDO PROCESSO DE AUTOMAÇÃO ---")
    try:
        print("Buscando filme em alta...")
        info = movie_finder.buscar_filme()
        titulo = info['titulo']
        print(f"Filme selecionado: {titulo}")

        print(f"Baixando trailer...")
        video_downloader.baixar_video(titulo)
        video_local = "videos/video.mp4"

        if not os.path.exists(video_local):
            print("Erro: Arquivo de vídeo não encontrado.")
            return

        print("Editando vídeo para Reels...")
        caminho_clipe = clip_creator.criar_clip(video_local)

        print("Gerando legenda...")
        legenda_final = caption_generator.gerar_legenda(info)

        print("Postando no Instagram...")
        sucesso = instagram_poster.postar(caminho_clipe, legenda_final)

        if sucesso:
            print("Processo finalizado com sucesso!")
        else:
            print("Falha na etapa de postagem.")

    except Exception as e:
        print(f"Erro geral: {e}")

if __name__ == "__main__":
    # 1. Inicia o servidor web em paralelo (em uma thread separada)
    # Isso evita que o Railway marque como "Crashed"
    threading.Thread(target=rodar_servidor_web, daemon=True).start()
    
    # 2. Inicia sua automação principal
    executar_automacao_completa()