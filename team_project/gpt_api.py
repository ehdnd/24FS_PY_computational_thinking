from openai import OpenAI
import os
from dotenv import load_dotenv

def diary_to_emotion():
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    client = OpenAI(api_key=api_key)

    diary = input("일기 입력: ")

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "당신은 감정 분석가입니다. 사용자가 입력한 '오늘 있었던 일'에 대한 내용을 바탕으로 그들의 감정 상태를 추론하세요. 답변에는 '즐거움'과 같이 한 단어만을 사용해 표현해주세요. 감정 상태는 '기쁨, 슬픔, 분노, 두려움, 혐오, 놀람, 사랑, 외로움' 만을 사용하세요."},
        {"role": "user", "content": diary}
    ]
    )


    return (completion.choices[0].message.content)