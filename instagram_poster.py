from instagrapi import Client
import os

# Credenciais (Recomendado usar variáveis de ambiente no futuro por segurança)
USUARIO = "Leopeixoto97"
SENHA = "0675"

def postar(caminho_video, legenda):
    cl = Client()
    
    # Define um tempo de espera para evitar bloqueios
    cl.delay_range = [2, 5]

    print(f"🔐 Tentando login para: {USUARIO}")
    
    try:
        # Tenta carregar uma sessão anterior para não logar do zero toda vez
        session_file = "session.json"
        if os.path.exists(session_file):
            cl.load_settings(session_file)
        
        cl.login(USUARIO, SENHA)
        cl.dump_settings(session_file)
        
        print("🎬 Fazendo upload do Reel (isso pode demorar uns minutos)...")
        
        # O instagrapi cuida de converter e enviar o vídeo
        media = cl.clip_upload(
            path=caminho_video,
            caption=legenda
        )
        
        print(f"✅ Sucesso! Postado com o ID: {media.pk}")
        return True

    except Exception as e:
        print(f"❌ Erro na postagem: {e}")
        return False