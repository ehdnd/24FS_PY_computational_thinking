import random

menu = 0
travel_list = []
review_list = []

while menu != 5:
    print("=" * 50)
    print("         여행장소 관리 프로그램          ")
    print("=" * 50)
    print("1. 여행장소 목록 및 리뷰 출력")
    print("2. 여행장소 추가")
    print("3. 여행장소 삭제")
    print("4. 여행장소 추천")
    print("5. 종료하기")
    
    menu = int(input("메뉴를 선택하세요: "))

    if menu == 1:
        for i in range(0, len(travel_list), 1):
            print(f"{i + 1}. {travel_list[i]}: {review_list[i]}")

    elif menu == 2:
        place_append = input("추가할 여행지를 입력하세요: ")
        travel_list.append(place_append)
        place_append_review = input("추가할 여행지의 리뷰를 입력하세요: ") #같은 인덱스 번호를 가진다
        review_list.append(place_append_review)

    elif menu == 3:
        print("====== 여행지 목록 ======")
        n = 0
        for place in travel_list :
            print(f"{n}. {place}")
            n += 1
        place_del_index = int(input("삭제할 여행지 인덱스 번호를 입력하세요: "))
        place_del = travel_list[place_del_index]
        del travel_list[place_del_index]
        del review_list[place_del_index]
        print(f"{place_del} 여행지와 리뷰가 삭제되었습니다.\n여행지 목록: {travel_list}")

    elif menu == 4:
        random_place = random.choice(travel_list)
        print(f"오늘의 추천 여행지: {random_place}")
    
    else:
        print("종료합니다.")