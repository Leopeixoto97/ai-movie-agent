import yt_dlp
import os

def baixar_video(nome):
    # Cria a pasta 'videos' se ela não existir
    if not os.path.exists('videos'):
        os.makedirs('videos')

    busca = f"{nome} trailer oficial dublado"
    
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        # Ajustei aqui para salvar sempre como 'video.mp4' para o seu main.py encontrar
        'outtmpl': 'videos/video.mp4', 
        'noplaylist': True,
        # A LINHA MÁGICA: Aqui ele lê os cookies que você subiu
        'cookiefile': 'cookie.txt', 
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"ytsearch1:{busca}"])
        print(f"Download de '{nome}' concluído com sucesso!")
    except Exception as e:
        print(f"Erro ao baixar: {e}")