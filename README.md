# EnmuMic
The script then sends the audio file to an Automatic Speech Recognition (ASR) webservice to transcribe the audio to text. The transcribed text is then translated from English to Japanese using the Amazon Translate service. The translated text is then used to generate a synthetic voice audio file in Japanese using the voicevox library

**Important Note ** 

>There maybe some issue in it, But I'm Still working on it,
> So Be Patience 

# Setup
1. `git clone https://github.com/Maka2008/EnmuMic`
2. And Downlaod And Extract Voice_Vox Engine in EmmuMIc 
3. `cd EnmuMic`
4. Run the run.bat
5. Make Sure u Install the API Key of Amazon AWS translate key in Your Pc

# OverView 
This is a Python script that continuously listens to audio input from the microphone and transcribes it using an open-source automatic speech recognition (ASR) engine called OpenAI Whisper ASR. The script then translates the transcribed text from English to Japanese using Amazon Translate and synthesizes the translated text into speech using the voice synthesis engine VoiceVox. Finally, the synthesized speech is played back using the Pygame mixer module.

The script is designed to be run continuously in a loop, waiting for the user to press and hold the 'c' key to start recording audio input from the microphone, and releasing the 'c' key to end the recording. When the recording ends, the audio data is saved as a WAV file, and the transcribed text is obtained by calling the transcribe() function, which uses the OpenAI Whisper ASR engine to convert the audio data into text.

The transcribed text is then translated from English to Japanese using the Amazon Translate API. The translated text is synthesized into speech using the VoiceVox engine and saved as a WAV file. The Pygame mixer module is then used to play back the synthesized speech.

The script is designed to run indefinitely until the user presses the 'b' key to stop the playback of the synthesized speech and exit the program.


# How to use 
>1. To Press/Hold C to record and record the Voice for Sec 5
>2. It will start recording your voice and save it as wav file then it will transcribe it 
>3. Then it will translate the into Japanase through Amazon Translate API for VOX Client
>4. Then it will use Japanese text to Create voice of Your waifu and give a playback
>5. Then Voice Send it through VB Virtual Cable as Output

# Credits
@tuna2134 For Voice Vox Client,
@VOICEVOX For Voice Vox and Docker Image,
@ahmetoner For Whisper Docker Image,
