from pydub import AudioSegment
from pydub.playback import play
import os
import time

def play_audio(audio_file_path):
    audio = AudioSegment.from_file(audio_file_path)
    play(audio)
    time.sleep(1)
    