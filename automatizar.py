import schedule
import time
from main import executar_automacao_completa

# Agenda a execução para todos os dias às 12:00
# Podes alterar o horário para quando preferires (ex: "18:00")
schedule.every().day.at("12:00").do(executar_automacao_completa)

print("🤖 Agente de Cinema ativado! Aguardando o horário agendado...")

while True:
    # Verifica se há alguma tarefa agendada para rodar
    schedule.run_pending()
    # Espera 60 segundos antes de verificar novamente para poupar processamento
    time.sleep(60)