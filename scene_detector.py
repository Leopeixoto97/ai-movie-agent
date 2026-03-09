import cv2

def detectar_cenas(video_path):
    cap = cv2.VideoCapture(video_path)
    
    # Pegamos o FPS (Frames por Segundo) do vídeo para calcular o tempo real
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    cenas = []
    frame_anterior = None
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Redimensionar o frame acelera MUITO o processamento sem perder precisão na detecção
        small_frame = cv2.resize(frame, (320, 180))
        gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
        
        # Aplicar um leve desfoque ajuda a ignorar "ruído" digital
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if frame_anterior is not None:
            # Calcula a diferença entre os frames
            diff = cv2.absdiff(frame_anterior, gray)
            score = diff.mean()

            # Se a mudança for brusca, marca o tempo em segundos
            if score > 30:
                tempo_segundos = count / fps
                cenas.append(round(tempo_segundos, 2))

        frame_anterior = gray
        count += 1

    cap.release()
    return cenas

# Exemplo:
# tempos = detectar_cenas("videos/meu_trailer.mp4")
# print(f"Cortes detectados nos segundos: {tempos}")