from moviepy.editor import VideoFileClip
import random
import os

def criar_clip(input_path="videos/video.mp4", output_folder="clips"):
    # 1. Garante que a pasta de destino exista
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 2. Carrega o vídeo original
    video = VideoFileClip(input_path)

    # --- CORREÇÃO PARA A LISTRA (NÚMEROS PARES) ---
    # Pegamos largura (w) e altura (h) e garantimos que sejam pares
    w, h = video.size
    new_w = w if w % 2 == 0 else w - 1
    new_h = h if h % 2 == 0 else h - 1
    
    # Redimensiona levemente se for ímpar para evitar o erro do codec
    video = video.resize(new_size=(new_w, new_h))
    # ----------------------------------------------

    duracao = video.duration
    tempo_clip = 30 # Tempo ideal para Reels/Instagram

    # 3. Define um ponto de início aleatório seguro
    if duracao > tempo_clip + 10:
        inicio = random.randint(10, int(duracao - tempo_clip))
        fim = inicio + tempo_clip
    else:
        inicio, fim = 0, duracao

    # 4. Cria o subclip
    clip = video.subclip(inicio, fim)
    
    # 5. Define o nome do arquivo de saída usando os.path para evitar erros de barra
    nome_arquivo = os.path.join(output_folder, "clip_pronto.mp4")

    print(f"Iniciando a renderização: {nome_arquivo}...")

    # 6. Salva o arquivo (O comando que estava faltando!)
    # pix_fmt yuv420p garante máxima compatibilidade com celulares
    clip.write_video_file(
        nome_arquivo, 
        codec="libx264", 
        audio_codec="aac",
        temp_audiofile='temp-audio.m4a', 
        remove_temp=True,
        ffmpeg_params=["-pix_fmt", "yuv420p"]
    )

    # 7. Libera os arquivos da memória
    video.close()
    clip.close()

    print("Clip criado com sucesso!")
    return nome_arquivo

# Para testar o script sozinho, descomente a linha abaixo:
# criar_clip()