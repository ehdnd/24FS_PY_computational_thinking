from openai import OpenAI
import os
from dotenv import load_dotenv

def diary_to_emotion():
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    client = OpenAI(api_key=api_key)
    # defaults to getting the key using os.environ.get("OPENAI_API_KEY")
    # if you saved the key under a different environment variable name, you can do something like:
    # client = OpenAI(
    #   api_key=os.environ.get("CUSTOM_ENV_NAME"),
    # )

    # completion = client.chat.completions.create(
    #   model="gpt-3.5-turbo",
    #   messages=[
    #     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    #     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    #   ]
    # )

    diary = input("일기 입력: ")

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "당신은 감정 분석가입니다. 사용자가 입력한 '오늘 있었던 일'에 대한 내용을 바탕으로 그들의 감정 상태를 추론하세요. 답변에는 '즐거움'과 같이 한 단어만을 사용해 표현해주세요."},
        {"role": "user", "content": diary}
    ]
    )


    print(completion.choices[0].message.content)
