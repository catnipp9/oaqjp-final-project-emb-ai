import requests
import json

def emotion_detector(text_to_analyse):
    if not text_to_analyse.strip():
        # Return None for all emotions if input is blank
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyse}}
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response_json = response.json()['text']
    emotions = json.loads(response_json)
    
    dominant = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant
    
    return emotions