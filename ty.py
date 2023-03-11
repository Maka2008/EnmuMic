while True:
    while True:
        import os
        import pyaudio
        import wave
        import sys
        from pynput import keyboard
        import requests
        import boto3
        import urllib.parse
        import winsound
        import time
        import subprocess
        

        CHUNK = 8192
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        WAVE_OUTPUT_FILENAME = "mic.wav"
        p = pyaudio.PyAudio()
        frames = []
        docker_cmd = "docker run -d --gpus all -p 9888:9000 -e ASR_MODEL=base onerahmet/openai-whisper-asr-webservice:latest-gpu"
        BASE_URL = "http://127.0.0.1:9000"

        def transcribe(filepath):
            with open(filepath, 'rb') as infile:
                files = {'audio_file': infile}
                r = requests.post(f'{BASE_URL}/asr?task=transcribe&language=en&output=json', files=files)
                return r.json()['text']

        def callback(in_data, frame_count, time_info, status):
            frames.append(in_data)
            return (in_data, pyaudio.paContinue)

        class MyListener(keyboard.Listener):
            def __init__(self):
                super(MyListener, self).__init__(self.on_press, self.on_release)
                self.key_pressed = None
                self.wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
                self.wf.setnchannels(CHANNELS)
                self.wf.setsampwidth(p.get_sample_size(FORMAT))
                self.wf.setframerate(RATE)

            def on_press(self, key):
                try:
                    if key.char == 'c':
                        self.key_pressed = True
                    return True
                except AttributeError:
                    sys.exit()

            def on_release(self, key):
                if key.char == 'c':
                    self.key_pressed = False
                return True

        listener = MyListener()
        listener.start()
        started = False
        stream = None

        def callback(in_data, frame_count, time_info, status):
            frames.append(in_data)
            return (in_data, pyaudio.paContinue)

        def recorder():
            global started, p, stream, frames

            while True:
                try:
                    if listener.key_pressed and not started:
                        # Start the recording
                        try:
                            stream = p.open(format=FORMAT,
                                            channels=CHANNELS,
                                            rate=RATE,
                                            input=True,
                                            frames_per_buffer=CHUNK,
                                            stream_callback = callback)
                            print("Stream active:", stream.is_active())
                            started = True
                            print("start Stream")
                        except KeyboardInterrupt:
                            print('\nRecording finished: ' + repr(WAVE_OUTPUT_FILENAME))
                            quit()

                    elif not listener.key_pressed and started:
                        # Stop recording
                        print("Stop recording")
                        stream.stop_stream()
                        stream.close()
                        p.terminate()

                        listener.wf.writeframes(b''.join(frames))
                        listener.wf.close()
                        print("You should have a wav file in the current directory")

                        # Do something with the audio file here
                        # For example, you could call a transcribe function
                        # and print out the transcription
                        # transcription = transcribe(WAVE_OUTPUT_FILENAME)
                        # print(f"Transcription: {transcription}")

                        return

                except KeyboardInterrupt:
                    print('\nRecording finished: ' + repr(WAVE_OUTPUT_FILENAME))
                    quit()
                except AttributeError:
                    quit()

        print ("-> Press and hold the 'c' key to record your audio")
        print ("-> Release the 'c' key to end recording")
        recorder()

        try:
                transcription = transcribe(WAVE_OUTPUT_FILENAME)
                print(f"Transcription: {transcription}")
                break
        except Exception as e:
                print("No audio could be transcribed. Restarting program...")
                time.sleep(5)  # wait for 5 seconds before restarting the program
                continue


    import boto3
    from voicevox import Client
    import asyncio
    from pydub import AudioSegment
    from pydub.playback import play

        # Initialize the Amazon Translate client
    translate = boto3.client('translate')

        # The text to translate
    text_to_translate = transcription

        # The source language (auto-detected if not specified)
    source_language = 'en'

        # The target language
    target_language = 'ja'

        # Translate the text
    response = translate.translate_text(
            Text=text_to_translate,
            SourceLanguageCode=source_language,
            TargetLanguageCode=target_language
        )

        # Get the translated text
    translated_text = response['TranslatedText']

        # Print the translated text
    print("Translated Text: ", translated_text)

   
   

    async def main():
        # Start the first program
        process = subprocess.Popen("./windows-nvidia/run.exe")

        await p_main()

        # Wait for the processes to finish and close them
        try:
            process.kill()
        except Exception:
            pass

    async def p_main():
        async with Client() as client:
            audio_query = await client.create_audio_query(translated_text, speaker=1)
            audio_bytes = await audio_query.synthesis()
            with open("voice.wav", "wb") as f:
                f.write(audio_bytes)
            audio = AudioSegment.from_file("voice.wav", format="wav")
            play(audio)

    if __name__ == "__main__":
        asyncio.run(main())

    import time
    from pygame import mixer
    import keyboard


    mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')
    mixer.music.load("voice.wav")
    mixer.music.play()

        # Loop while music is playing
    while mixer.music.get_busy():
            # Check if the "b" key is being held down
            if keyboard.is_pressed('b'):
                # Stop the music and exit the program
                mixer.music.stop()
                mixer.quit()
                exit()

            time.sleep(1)

    mixer.quit()

        

