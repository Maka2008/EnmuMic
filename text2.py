import os
import pyaudio
import wave
import whisper
from Package import translate_text, run_background_exe, generate_voicevox_audio, play_audio, V_B
import asyncio
import time
import keyboard

# Define the audio settings
CHUNK = 1024  # Number of frames per buffer
FORMAT = pyaudio.paInt16  # Sample size and format
CHANNELS = 2  # Number of audio channels (stereo)
RATE = 44100  # Sample rate (Hz)
RECORD_SECONDS = 5  # Duration of recording (in seconds)

# Load the model
model = whisper.load_model("tiny.en")

async def record_and_transcribe_audio():
    # Get the name of the next output file
    WAVE_OUTPUT_FILENAME = "output.wav"

    # Create an instance of the PyAudio class
    audio = pyaudio.PyAudio()

    # Open a new stream to record audio
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                        input=True, frames_per_buffer=CHUNK)

    print("Recording...")

    # Create a buffer to store the audio data
    frames = []

    # Record audio for the specified duration
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording!")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()

    # Terminate the PyAudio object
    audio.terminate()

    # Save the recorded audio as a WAV file
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    # Transcribe the audio file
    result = model.transcribe(WAVE_OUTPUT_FILENAME, fp16=False)
    transcription = result["text"]
    print(transcription)

    # Remove the audio file
    os.remove(WAVE_OUTPUT_FILENAME)

    # Translate the transcription
    translated_text = translate_text(transcription)
    print(translated_text)

    exe_path = "./windows-nvidia/run.exe"
    run_background_exe(exe_path)

    # Generate audio from the translated text
    await generate_voicevox_audio(translated_text, speaker=3, output_path="voice.wav")

    # Play the generated audio
    audio_file_path = "voice.wav"
    play_audio(audio_file_path)

    # Perform some action based on the translated text
    V_B()

async def main():
    while True:
        if keyboard.is_pressed('c'):
            print("The 'c' key is pressed. Hold it for 5 seconds to record audio.")
            start_time = time.time()
            while time.time() - start_time < 0.1:
                if not keyboard.is_pressed('c'):
                    print("Recording cancelled.")
                    break
            else:
                await record_and_transcribe_audio()

# Call the async function
asyncio.run(main())

