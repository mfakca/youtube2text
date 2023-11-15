from faster_whisper import WhisperModel

model_size = 'large-v2'

model = WhisperModel(model_size, compute_type = 'int8')

segments, info = model.transcribe('deneme.mp3', beam_size= 5)

print(info.language)

for i in segments:
    print(i.start, i.end, i.text)