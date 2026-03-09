import movie_finder
import video_downloader
import clip_creator
import caption_generator
import instagram_poster
import os

def executar_automacao_completa():
    print("--- INICIANDO PROCESSO DE AUTOMAÇÃO ---")

    try:
        # 1. Busca dados do filme no TMDB (movie_finder.py)
        # Retorna um dicionário com titulo, ano, sinopse e genero
        print("Buscando filme em alta...")
        info = movie_finder.buscar_filme()
        titulo = info['titulo']
        print(f"Filme selecionado: {titulo}")

        # 2. Download do trailer via yt-dlp (video_downloader.py)
        # Salva o vídeo em 'videos/video.mp4'
        print(f"Baixando trailer...")
        video_downloader.baixar_video(titulo)
        video_local = "videos/video.mp4"

        # Verifica se o download realmente ocorreu antes de prosseguir
        if not os.path.exists(video_local):
            print("Erro: Arquivo de vídeo não encontrado.")
            return

        # 3. Edição do clipe via MoviePy (clip_creator.py)
        # Aplica o corte de 30s e a correção para evitar a listra
        print("Editando vídeo para Reels...")
        caminho_clipe = clip_creator.criar_clip(video_local)

        # 4. Geração de legenda via OpenAI (caption_generator.py)
        # Usa o GPT-4o-mini para criar um texto com hashtags
        print("Gerando legenda...")
        legenda_final = caption_generator.gerar_legenda(info)

        # 5. Postagem via instagrapi (instagram_poster.py)
        # Faz o upload direto do arquivo local para o Instagram
        print("Postando no Instagram...")
        sucesso = instagram_poster.postar(caminho_clipe, legenda_final)

        if sucesso:
            print("Processo finalizado com sucesso!")
        else:
            print("Falha na etapa de postagem.")

    except Exception as e:
        print(f"Erro geral: {e}")

if __name__ == "__main__":
    executar_automacao_completa()