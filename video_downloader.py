import yt_dlp
import os

def baixar_video(nome):
    # Cria a pasta 'videos' se ela não existir
    if not os.path.exists('videos'):
        os.makedirs('videos')

    busca = f"{nome} trailer oficial dublado" # Adicionei 'oficial dublado' para melhores resultados
    
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best', # Garante a melhor qualidade mp4
        'outtmpl': f'videos/%(title)s.%(ext)s', # Salva com o título do vídeo do YouTube
        'noplaylist': True, # Garante que não baixe uma playlist inteira por engano
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"ytsearch1:{busca}"]) # 'ytsearch1' baixa apenas o primeiro resultado
        print(f"Download de '{nome}' concluído com sucesso!")
    except Exception as e:
        print(f"Erro ao baixar: {e}")

# Exemplo de uso
# baixar_video("Deadpool e Wolverine")