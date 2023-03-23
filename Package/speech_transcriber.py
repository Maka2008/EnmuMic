import whisper
import soundfile as sf

# Load the tiny model
model = whisper.models.Tiny()

# Load the audio file
audio, sample_rate = sf.read('0318 (1) [vocals].mp3')

# Transcribe the audio to text
transcription = model.transcribe(audio, sample_rate)

# Print the transcription
print(transcription)
