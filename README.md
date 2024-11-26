# Transcriber Component

Este componente realiza a transcrição de áudio em texto de forma simples e eficaz utilizando o Whisper da OpenAI. Ele aceita arquivos de áudio no formato `.wav` e converte o conteúdo em texto utilizando tecnologias integradas.

## Pré-requisitos

### 1. Instalação de Dependências

Antes de utilizar o componente, é necessário instalar todas as extensões listadas no arquivo `requirements.txt`. Para isso, execute o comando abaixo no terminal:

```bash
pip install -r requirements.txt
```

### 2. Instalação do FFmpeg

O FFmpeg é necessário para manipulação e processamento de áudio. Certifique-se de ter o gerenciador de pacotes Chocolatey instalado na sua máquina. Caso não tenha, consulte a [documentação oficial do Chocolatey](https://chocolatey.org/install) para instalação.

Em seguida, instale o FFmpeg utilizando o comando:

```bash
choco install ffmpeg
```

### 3. Git Bash para Execução de Comandos

Para enviar o áudio ao servidor, utilize o terminal Git Bash. Caso ainda não tenha o Git instalado, você pode baixá-lo no [site oficial do Git](https://git-scm.com/downloads).

## Executando o Componente

### 1. Inicialize o Servidor

Certifique-se de que o servidor responsável pelo processamento da transcrição está em execução. Geralmente, ele pode ser iniciado com um comando como:

```bash
python manage.py runserver
```

### 2. Realize a Transcrição

No Git Bash, utilize o comando abaixo para enviar o arquivo de áudio ao servidor e obter a transcrição:

```bash
curl -X POST "http://127.0.0.1:8000/transcribe/" -F "file=@C:/Users/Rhuan/Downloads/Teste.wav"
```

### Observações

- **Formato do Áudio**: Apenas arquivos no formato `.wav` são aceitos.
- **Caminho do Arquivo**: Certifique-se de fornecer o caminho completo e correto do arquivo no comando `curl`.
- **Servidor Local**: O endereço padrão é `http://127.0.0.1:8000`, mas ajuste caso esteja utilizando outra configuração.

## Solução de Problemas

1. **FFmpeg não instalado**: Certifique-se de que o FFmpeg está corretamente configurado no PATH do sistema. Teste a instalação executando `ffmpeg` no terminal.
2. **Dependências faltando**: Verifique se todas as bibliotecas foram instaladas a partir do arquivo `requirements.txt`.
3. **Erro de conexão**: Confirme que o servidor está em execução no endereço e porta esperados.
