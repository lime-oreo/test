import requests
import datetime

# 기상청 OpenAPI 인증키
API_KEY = "yJx31CfRrU9M2OWzJIVY5SjwfZzIg1/hMrD45fvVr3ORbv1bm0HyKF6R83CpIeSJTuMZ7vBp7qFiLR43cUEllA=="  # 발급받은 인증키를 입력하세요

# 기상청 단기예보 API URL
BASE_URL = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"

# 요청 파라미터 설정
params = {
    "serviceKey": API_KEY,  # 인증키
    "numOfRows": 10,       # 한 번에 가져올 데이터 수
    "pageNo": 1,           # 페이지 번호
    "dataType": "JSON",    # 데이터 타입 (JSON, XML)
    "base_date": datetime.datetime.now().strftime("%Y%m%d"),  # 오늘 날짜
    "base_time": "0500",   # 기준 시간 (예: 0500, 1100, 1700)
    "nx": 61,              # X 좌표 (서울 예시)
    "ny": 127              # Y 좌표 (서울 예시)
}

# 요청 보내기
response = requests.get(BASE_URL, params=params)

# 응답 처리
if response.status_code == 200:
    data = response.json()  # JSON 파싱
    if "response" in data and "body" in data["response"]:
        items = data["response"]["body"]["items"]["item"]
        for item in items:
            print(f"Category: {item['category']}, Value: {item['fcstValue']}")
    else:
        print("No data found.")
else:
    print(f"Error: {response.status_code}")