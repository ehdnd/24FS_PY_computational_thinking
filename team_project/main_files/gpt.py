# pip install openai

from openai import OpenAI
import os
from dotenv import load_dotenv

# diary 변수로 받으면 '감정' return
def diary_to_emotion(diary):
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "당신은 감정 분석가입니다. 사용자가 입력한 '오늘 있었던 일'에 대한 내용을 바탕으로 그들의 감정 상태를 추론하세요. 답변에는 '즐거움'과 같이 한 단어만을 사용해 표현해주세요. 감정 상태는 '기쁨, 슬픔, 분노, 두려움, 혐오, 놀람, 사랑, 외로움' 만을 사용하세요."},
        {"role": "user", "content": diary}
    ]
    )


    return (completion.choices[0].message.content)


# diary 변수로 받으면 요약 내용 return
def diary_summary(diary):
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "사용자가 제공한 일기입니다. 일기의 내용을 요약하세요."},
        {"role": "user", "content": diary}
    ]
    )


    return (completion.choices[0].message.content)