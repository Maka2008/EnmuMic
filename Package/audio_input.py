import os
import boto3

def translate_text(transcription):
    if isinstance(transcription, dict):
        transcription = transcription.get('text', '')
    if not isinstance(transcription, str) or len(transcription) == 0:
        return ""
    translate = boto3.client('translate')
    try:
        response = translate.translate_text(
            Text=transcription,
            SourceLanguageCode='en',
            TargetLanguageCode='ja'
        )
        translated_text = response['TranslatedText']
        return translated_text
    except Exception as e:
    
        return ""
