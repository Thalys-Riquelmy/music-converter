Aqui está um exemplo de um README para o seu projeto:

---

# Music Converter - Baixar Áudio do YouTube

Este é um aplicativo simples desenvolvido com Python e Tkinter que permite ao usuário baixar o áudio de vídeos do YouTube diretamente para o seu computador. Ele utiliza o `yt-dlp` para o download e conversão de vídeos, e o `Tkinter` para a interface gráfica.

## Requisitos

Antes de executar o projeto, verifique se você tem as dependências necessárias:

- Python 3.x
- yt-dlp: para baixar o áudio do YouTube
- ffmpeg: para a conversão de vídeos e áudios
- Tkinter: para a interface gráfica

### Instalação de Dependências

1. Instale o `yt-dlp` com o seguinte comando:
   ```bash
   pip install yt-dlp
   ```

2. Instale o `Tkinter` (geralmente já vem com o Python, mas caso não tenha, pode instalar via seu gerenciador de pacotes):
   ```bash
   pip install tk
   ```

3. Baixe o [FFmpeg](https://ffmpeg.org/download.html) e descompacte a pasta em um diretório no seu computador. Lembre-se de alterar o caminho no código para onde o `ffmpeg` foi descompactado.

## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Thalys-Riquelmy/music-converter.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd music-converter
   ```

3. Execute o script Python:
   ```bash
   python app.py
   ```

4. O aplicativo irá abrir uma interface gráfica onde você pode:
   - Inserir o link do vídeo do YouTube no campo de entrada.
   - Escolher o diretório onde o arquivo será salvo.
   - Iniciar o download do áudio clicando no botão "Baixar".

## Funcionalidades

- **Baixar Áudio**: Insira o link do vídeo do YouTube e o áudio será baixado no formato MP4 (apenas áudio).
- **Escolher Pasta de Destino**: Permite ao usuário escolher o diretório onde o arquivo será salvo.
- **Limpar Campo de Entrada**: Limpa o campo de entrada para inserir outro link.

## Estrutura do Código

- **`baixar_audio()`**: Função principal para realizar o download do áudio.
- **`limpar_campo()`**: Função para limpar o campo de entrada.
- **`escolher_pasta()`**: Permite ao usuário escolher a pasta de destino.
- **`rodar_download()`**: Faz o download do áudio em uma thread separada para não bloquear a interface gráfica.

## Problemas Conhecidos

- O caminho para o FFmpeg no código (`'ffmpeg_location'`) está configurado para uma instalação específica do Windows. Certifique-se de ajustar o caminho de acordo com a sua plataforma e onde o FFmpeg está instalado.

## Contribuição

Sinta-se à vontade para abrir um **pull request** ou um **issue** se encontrar algum bug ou tiver sugestões de melhorias.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
