from gpt import diary_summary
from recommend_song import recommend_song
from diary import write_diary, list_diaries, load_diary

while 1:
    print("=" * 20)
    print("기능 선택")
    print("1. 일기 작성")
    print("2. 일기 요약")
    print("3. 음악 추천")
    print("4. 프로그램 종료")
    print("=" * 20)
    main_menu_num = input("번호 입력: ")
    print("-" * 20)

    # 1. 일기 작성
    if main_menu_num == "1":
        # 일기 작성 def 필요
        pass

    # 2. 일기 요약
    elif main_menu_num == "2":
        diary = None                            # 일기 불러오는 def 필요
        diasry_summary = diary_summary(diary)   # 일기 요약 def(불러온 일기) 필요
        print(f"요약한 일기는 다음과 같습니다.\n\"{diary_summary}\"")

    # 3. 음악 추천
    elif main_menu_num == "3":
        while 1:
            print("[3. 음악추천] 불러올 일기 선택")
                                    # 일기 목록 출력; len으로 반복실행
            diary = "날씨가 좋다." 
            print(f"일기: {diary}")           # 일기 불러오는 def 필요
            random_song = recommend_song(diary)   # 음악 추천 def(불러온 일기) 필요
            if random_song != "error":
                print(f"추천곡: {random_song}")
                break
            else:
                print("GPT 요약에 있어 문제가 발생했습니다.")
                print("일기 선택으로 돌아갑니다.")

    # 4. 종료
    else:
        print("프로그램을 종료합니다.")
        break