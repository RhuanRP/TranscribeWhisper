import whisper

model = whisper.load_model("base")
transcription = model.transcribe("C:/Users/Rhuan/Downloads/Teste.wav", language="pt")
print(transcription["text"])
