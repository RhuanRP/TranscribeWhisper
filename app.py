from fastapi import FastAPI, File, UploadFile
import whisper
import uvicorn
import os
from tempfile import NamedTemporaryFile
from fastapi.responses import JSONResponse

app = FastAPI()

# Carregar o modelo Whisper
model = whisper.load_model("base")

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    temp_path = None
    try:
        print(f"Recebendo arquivo: {file.filename}")
        
        # Criar um arquivo temporário para salvar o upload
        temp_path = os.path.join(os.getcwd(), "temp_audio" + os.path.splitext(file.filename)[1])
        temp_path = os.path.abspath(temp_path)  # Garante o caminho absoluto
        
        # Salvar o conteúdo do upload no arquivo temporário
        content = await file.read()
        print(f"Tamanho do conteúdo recebido: {len(content)} bytes")
        
        with open(temp_path, "wb") as temp_file:
            temp_file.write(content)
            temp_file.flush()
            os.fsync(temp_file.fileno())  # Força a escrita no disco
        
        print(f"Arquivo temporário salvo em: {temp_path}")
        print(f"O arquivo existe? {os.path.exists(temp_path)}")
        print(f"Tamanho do arquivo: {os.path.getsize(temp_path)} bytes")
        print(f"Permissões do arquivo: {oct(os.stat(temp_path).st_mode)[-3:]}")

        # Verifica se o arquivo pode ser aberto para leitura
        with open(temp_path, "rb") as test_file:
            test_file.read(1024)  # Tenta ler o início do arquivo
            print("Arquivo pode ser lido corretamente")

        # Transcreve o áudio
        try:
            print(f"Iniciando transcrição do arquivo: {temp_path}")
            result = model.transcribe(temp_path, language="pt")
            text = result["text"]
            print(f"Transcrição concluída com sucesso: {text[:100]}...")  # Mostra os primeiros 100 caracteres
            return JSONResponse(content={"transcription": text})
        except Exception as whisper_error:
            print(f"Erro no Whisper: {str(whisper_error)}")
            print(f"Tipo do erro: {type(whisper_error)}")
            import traceback
            print(f"Stack trace completo: {traceback.format_exc()}")
            return JSONResponse(content={"error": f"Erro no Whisper: {str(whisper_error)}"}, status_code=500)
    
    except Exception as e:
        print(f"Erro na API: {str(e)}")
        print(f"Tipo do erro: {type(e)}")
        import traceback
        print(f"Stack trace completo: {traceback.format_exc()}")
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
    finally:
        # Limpar o arquivo temporário apenas se a transcrição foi concluída
        if temp_path and os.path.exists(temp_path):
            try:
                os.remove(temp_path)
                print(f"Arquivo temporário removido com sucesso")
            except Exception as e:
                print(f"Erro ao remover arquivo temporário: {e}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
