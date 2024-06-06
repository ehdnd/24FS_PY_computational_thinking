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
        print("일기 이름을 입력하세요.")
        print("(엔터를 누를 경우 오늘 날짜로 제목이 생성됩니다.)")
        print("-" * 50)
        diary_name = input()
        print("-" * 50)

        if diary_name == "":
            diary_name = datetime.now().strftime("%Y-%m-%d")

        if diary_name not in list_diaries():
            file_path = os.path.join(DIARY_PATH, diary_name)
            
            print("일기 내용을 작성하세요.")
            print("(* 종료하려면 엔터를 두 번 누르세요.)")
            print("-" * 50)
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
            print("-" * 50)
            break
        else:
            print("같은 이름의 파일이 있습니다. 다른이름을 입력하세요.")
            print("-" * 50)

def load_diary(file_name):
    file_path = os.path.join(DIARY_PATH, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    else:
        return None