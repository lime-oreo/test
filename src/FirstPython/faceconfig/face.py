import requests
import json

# Azure Face API 설정
subscription_key = "5HuZJJiwD0zBERp6vaS2XXntL70G2IGR5jYUnwgB1zqT2Lgt3UIEJQQJ99AKACNns7RXJ3w3AAAKACOGAghm"  # Azure Portal에서 발급받은 Key
endpoint = "https://sungsun.cognitiveservices.azure.com/"  # Face API의 Endpoint (예: https://<your-resource-name>.cognitiveservices.azure.com/)

# 얼굴 분석 URL
face_api_url = f"{endpoint}/face/v1.0/detect"

# 이미지 URL (Google에서 찾은 이미지 URL 사용)
image_url = "https://img.freepik.com/free-photo/beauty-makeup-concept-close-up-carefree-teenage-girl-smiling-laughing-sincere-having-fun-standing-blue-background_1258-77508.jpg?semt=ais_hybrid"

# 요청 헤더와 데이터
headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/json'
}
params = {
    'returnFaceAttributes': 'headPose,glasses,blur,exposure,noise'
}
data = {
    'url': image_url
}

# API 요청
response = requests.post(face_api_url, headers=headers, params=params, json=data)

# 응답 출력
if response.status_code == 200:
    face_data = response.json()
    print("Face Analysis Result:")
    print(json.dumps(face_data, indent=2))
else:
    print(f"Error: {response.status_code}, {response.json()}")
