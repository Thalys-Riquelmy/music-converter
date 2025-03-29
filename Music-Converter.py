import yt_dlp as yt
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import threading

# Variável global para armazenar o diretório de destino
pasta_destino = ""

# Função para baixar o áudio
def baixar_audio():
    global pasta_destino

    link = entry_link.get()  # Pega o link da música do campo de entrada
    if not link:
        messagebox.showerror("Erro", "Por favor, insira o link do vídeo.")
        return

    # Se a pasta de destino não estiver definida, solicita ao usuário
    if not pasta_destino:
        pasta_destino = filedialog.askdirectory(title="Escolha a pasta de destino")
        if not pasta_destino:
            messagebox.showerror("Erro", "Por favor, escolha uma pasta para salvar o arquivo.")
            return

    # Exibe o texto "Baixando..." enquanto o download está em andamento
    label_status.config(text="Baixando...", fg="blue")
    root.update()

    try:
        # Extrai informações do vídeo
        info = yt.YoutubeDL().extract_info(url=link, download=False)

        # Configura as opções para o download
        opt = {
            'format': 'bestaudio/best',  # Baixa o melhor formato de áudio
            'keepvideo': False,          # Não mantém o vídeo
            'outtmpl': f"{pasta_destino}/{info['title']}.mp4",  # Salva como MP4 na pasta escolhida
            'extractaudio': False,       # Baixa vídeo e áudio
            'audioquality': 0,           # Melhor qualidade
            'ffmpeg_location': r"C:\Users\thaly\Downloads\ffmpeg-master-latest-win64-gpl-shared\ffmpeg-master-latest-win64-gpl-shared\bin\ffmpeg.exe",  # Caminho para o FFmpeg
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',  # Correção no nome do postprocessador
                'preferedformat': 'mp4',  # Alterado para preferedformat
            }],
        }

        # Baixa o vídeo e áudio
        with yt.YoutubeDL(opt) as y:
            y.download([info['webpage_url']])

        # Exibe mensagem de sucesso
        messagebox.showinfo("Sucesso", "Download concluído com sucesso!")
        label_status.config(text="Download Concluído", fg="green")
        entry_link.delete(0, tk.END)  # Limpa o campo de entrada
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
        label_status.config(text="Erro no Download", fg="red")

# Função para limpar o campo de entrada
def limpar_campo():
    entry_link.delete(0, tk.END)
    label_status.config(text="")

# Função para escolher nova pasta de destino
def escolher_pasta():
    global pasta_destino
    pasta_destino = filedialog.askdirectory(title="Escolha a nova pasta de destino")
    if pasta_destino:
        messagebox.showinfo("Pasta escolhida", f"A pasta de destino foi alterada para:\n{pasta_destino}")

# Função para rodar o download em uma thread separada
def rodar_download():
    threading.Thread(target=baixar_audio).start()

# Criação da janela principal
root = tk.Tk()
root.title("Baixar Áudio do YouTube")
root.geometry("400x250")  # Tamanho da janela

# Label para instruções
label = tk.Label(root, text="Digite o link do vídeo do YouTube:")
label.pack(pady=10)

# Campo de entrada para o link
entry_link = tk.Entry(root, width=40)
entry_link.pack(pady=5)

# Botão de download
btn_download = tk.Button(root, text="Baixar", command=rodar_download, width=20)
btn_download.pack(pady=10)

# Botão de limpar campo
btn_limpar = tk.Button(root, text="Limpar", command=limpar_campo, width=20)
btn_limpar.pack(pady=5)

# Botão de escolher pasta
btn_escolher_pasta = tk.Button(root, text="Escolher Pasta", command=escolher_pasta, width=20)
btn_escolher_pasta.pack(pady=10)

# Label de status (vai mostrar "Baixando..." ou o status do download)
label_status = tk.Label(root, text="", fg="black")
label_status.pack(pady=10)

# Inicia a interface gráfica
root.mainloop()
