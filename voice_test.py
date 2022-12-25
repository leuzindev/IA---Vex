from vosk import Model, KaldiRecognizer
import pyaudio

# Inicializa o modelo e o reconhecedor de áudio
model = Model('model')
rec = KaldiRecognizer(model, 16000)

# Inicializa o PyAudio e abre o stream de áudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

# Loop para processar o áudio em pedaços
while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        # Verifica se o usuário falou "pensando"
        if 'pensando' in rec.Result():
            print("O usuário falou 'pensando'.")
            break
    else:
        print(rec.PartialResult())

# Fecha o stream de áudio e o PyAudio
stream.stop_stream()
stream.close()
p.terminate()

# Imprime o resultado final da transcrição
print(rec.FinalResult())
