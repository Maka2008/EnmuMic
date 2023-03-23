from voicevox import Client
import asyncio


async def generate_voicevox_audio(text, speaker=1, output_path="voice.wav"):
    async with Client() as client:
        audio_query = await client.create_audio_query(text, speaker=speaker)
        with open(output_path, "wb") as f:
            f.write(await audio_query.synthesis(speaker=speaker))
