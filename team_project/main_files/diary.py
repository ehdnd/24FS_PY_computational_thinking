import os
from datetime import datetime

DIARY_PATH = "diaries"

def write_diary():
    if not os.path.exists(DIARY_PATH):
        os.makedirs(DIARY_PATH)
    
    diary_name = input("일기 이름을 입력하세요 (예: 2024-06-05.txt): ")
    file_path = os.path.join(DIARY_PATH, diary_name)
    
    content = input("일기 내용을 작성하세요:\n")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print("일기가 저장되었습니다.")

def list_diaries():
    if not os.path.exists(DIARY_PATH):
        os.makedirs(DIARY_PATH)
    return os.listdir(DIARY_PATH)

def load_diary(file_name):
    file_path = os.path.join(DIARY_PATH, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    else:
        return None

def main():
    while 1:
        print("=" * 20)
        print("기능 선택")
        print("1. 일기 작성")
        print("2. 일기 불러오기")
        print("3. 프로그램 종료")
        print("=" * 20)
        main_menu_num = input("번호 입력: ")
        print("-" * 20)
        
        if main_menu_num == "1":
            write_diary()
        elif main_menu_num == "2":
            diaries = list_diaries()
            if diaries:
                print("저장된 일기 목록:")
                for diary in diaries:
                    print(diary)
                diary_name = input("불러올 일기의 파일명을 입력하세요: ")
                content = load_diary(diary_name)
                if content:
                    print("일기 내용:")
                    print(content)
                else:
                    print("파일을 찾을 수 없습니다.")
            else:
                print("저장된 일기가 없습니다.")
        elif main_menu_num == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()
