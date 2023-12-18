import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, headers=headers, json=input_json)

    if response.status_code == 200:
        response_dict = response.json()
        emotion_predictions = response_dict.get("emotionPredictions", [])
        if emotion_predictions:
            first_prediction = emotion_predictions[0]
            emotion_scores = first_prediction.get("emotion",{})

            dominant_emotion = max(emotion_scores, key=emotion_scores.get)

            output_format = {
                'anger': emotion_scores.get('anger', 0),
                'disgust': emotion_scores.get('disgust', 0),
                'fear': emotion_scores.get('fear', 0),
                'joy': emotion_scores.get('joy', 0),
                'sadness': emotion_scores.get('sadness', 0),
                'dominant_emotion': dominant_emotion
            }

            return output_format
    else:
        print(f"Error: {response.status_code}")
        return None
