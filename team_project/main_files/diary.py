import os
from datetime import datetime

DIARY_PATH = "diaries"

def list_diaries():
    if not os.path.exists(DIARY_PATH):
        os.makedirs(DIARY_PATH)
    return os.listdir(DIARY_PATH)
    # return [os.path.splitext(file)[0] for file in os.listdir(DIARY_PATH)]

def write_diary():
    if not os.path.exists(DIARY_PATH):
        os.makedirs(DIARY_PATH)
    
    while 1:
        diary_name = input("일기 이름을 입력하세요 (예: 2024-06-05.txt): ")

        if diary_name not in list_diaries():
            file_path = os.path.join(DIARY_PATH, diary_name)
            
            print("일기 내용을 작성하세요. (* 종료하려면 엔터를 두 번 누르세요.)")
            lines = []
            while 1:
                line = input()
                if line == "":
                    break
                lines.append(line)
            content = "\n".join(lines)
            content = content.encode('utf-8', 'ignore').decode('utf-8')
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            break
        else:
            print("같은 이름의 파일이 있습니다. 다른이름을 입력하세요.")

def load_diary(file_name):
    file_path = os.path.join(DIARY_PATH, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    else:
        return None