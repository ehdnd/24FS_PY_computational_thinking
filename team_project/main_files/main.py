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
    
    if main_menu_num == "1":
        # 일기 작성 def 필요
        pass
    elif main_menu_num == "2":
        # 일기 불러오는 def 필요
        # 일기 요약 def(불러온 일기) 필요
        pass
    elif main_menu_num == "3":
        while 1:
            print("[3. 음악추천] 불러올 일기 선택")
            # 일기 목록 출력; len으로 반복실행
            # 일기 불러오는 def 필요                
            # 음악 추천 def(불러온 일기) 필요
            break
    else:
        print("프로그램을 종료합니다.")
        break