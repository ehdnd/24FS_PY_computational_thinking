from functions.gpt import diary_summary
from functions.recommend_song import recommend_song
from functions.diary import write_diary, list_diaries, load_diary

print("=" * 50)
print("[ 컴퓨팅적사고와코딩기초 6조 팀프로젝프 프로그램 ]")

while 1:
    print("=" * 50)
    print("[ 기능을 선택하세요 ]")
    print("1. 일기 작성")
    print("2. 일기 요약")
    print("3. 음악 추천")
    print("4. 프로그램 종료")
    print("-" * 50)
    main_menu_num = input("번호 입력: ")
    print("-" * 50)

    # 1. 일기 작성
    if main_menu_num == "1":
        write_diary()
        print("일기를 저장했습니다.")
        print("=" * 50)
            
    # 2. 일기 요약
    elif main_menu_num == "2":
        diary_list = list_diaries()
        if len(diary_list) > 0:
            # 올바른 인덱스 선택할떄까지 코드 반복
            while 1:
                print("일기를 선택하세요.")
                print("[ 일기 목록 ]")
                # 일기 목록 인덱스 붙혀 출력
                n = 1
                for diary in diary_list:
                    print(f"{n}. {diary}")
                    n += 1
                print("-" * 50)
                num = int(input("번호 입력: "))
                print("-" * 50)
                if 1 <= num <= len(diary_list):
                    break
            diary_name = diary_list[num - 1]
            diary = load_diary(diary_name)
            diary_summary = diary_summary(diary)
            print(f"[{diary_name}] 일기의 요약 내용은 다음과 같습니다.\n")
            print(diary_summary)
            print("=" * 50)

        # 작성한 일기 없으면 메인 메뉴로
        else:
            print("저장된 일기가 없습니다. 일기를 작성해주세요.")
            print("=" * 50)

    # 3. 음악 추천
    elif main_menu_num == "3":
        while 1:
            print("불러올 일기를 선택하세요.")
            diary_list = list_diaries()
            print("[ 일기 목록 ]")
            # 일기 목록 인덱스 붙혀 출력
            n = 1
            for diary in diary_list:
                print(f"{n}. {diary}")
                n += 1
            print("-" * 50)
            num = int(input("번호 입력: "))
            print("-" * 50)
            if num <= len(diary_list):
                break
        diary_name = diary_list[num - 1]
        diary = load_diary(diary_name)                 
        random_song = recommend_song(diary)
        print("=" * 50)

        if random_song != "error":
            print("[ 추천곡 ]")
            print(f"곡명: {random_song['title']}")
            print(f"아티스트명: {random_song['artist']}")
            print(f"장르: {random_song['genre']}")
            print(f"멜론차트 {random_song['genre']} 장르에서 {random_song['rank']}위")
            print("=" * 50)
        else:
            print("*** gpt 오류 ***\n정의되지 않은 감정입니다.")
            print("일기 선택으로 돌아갑니다.")
            print("=" * 50)

    # 4. 종료
    else:
        print("프로그램을 종료합니다.")
        print("=" * 50)
        break