import openai

OPENAI_YOUR_KEY = "sk-proj-lsFSdcytOyeSgcUkY3UPT3BlbkFJ3Rvko1uAMcy5o2jBdNI4"
openai.api_key = OPENAI_YOUR_KEY

MODEL = "gpt-3.5-turbo"
USER_INPUT_MSG = "chatGPT에 대해 설명해줘."

response = openai.ChatCompletion.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": USER_INPUT_MSG}, 
        {"role": "assistant", "content": "Who's there?"},
    ],
    temperature=0,
)

response