import yt_dlp
import os

def baixar_video(nome):
    if not os.path.exists('videos'):
        os.makedirs('videos')

    busca = f"{nome} trailer oficial dublado"
    
    # Verifique se o nome aqui é 'cookies.txt' (igual ao que aparece no seu VS Code agora)
    caminho_cookie = os.path.join(os.getcwd(), 'cookies.txt')

    ydl_opts = {
    'format': 'best[ext=mp4]/best', 
    'outtmpl': 'videos/video.mp4',
    'cookiefile': 'cookies.txt',
    'noplaylist': True,
}

    try:
        print(f"Tentando usar cookies em: {caminho_cookie}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"ytsearch1:{busca}"])
        print(f"Download de '{nome}' concluído com sucesso!")
    except Exception as e:
        print(f"Erro ao baixar: {e}")