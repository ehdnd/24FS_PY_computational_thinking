import random

rec_genre_list = ["팝", "록", "힙합", "R&B", "컨트리", "재즈", "전자", "클래식"]
rec_music_list_pop = ["Someone Like You", "Look What You Made Me Do", "Billie Jean"]
rec_music_list_rock = ["Paranoid Android", "My Generation", "Stairway To Heaven"]
rec_music_list_hiphop = ["HARD", "Pink Venom", "새삥"]
rec_music_list_rb = ["빛이 나는 너에게", "정이라고 하자", "Thirsty"]
rec_music_list_country = ["10,000 Hours", "Last Night", "Fast Car"]
rec_music_list_jazz = ["손이 참 곱던 그대", "Love in Potofino", "Oye Como Va"]
rec_music_list_electronic = ["Behind The Mask", "Discreet Music", "Spitzenqualitat"]
rec_music_list_classic = ["지금 이 순간", "아무도 잠들지 마라", "위대한 사랑"]

rec_genre = random.choice(rec_genre_list)
rec_music_pop = random.choice(rec_music_list_pop)
rec_music_rock = random.choice(rec_music_list_rock)
rec_music_hiphop = random.choice(rec_music_list_hiphop)
rec_music_rb = random.choice(rec_music_list_rb)
rec_music_country = random.choice(rec_music_list_country)
rec_music_jazz = random.choice(rec_music_list_jazz)
rec_music_electronic = random.choice(rec_music_list_electronic)
rec_music_classic = random.choice(rec_music_list_classic)


print(f"추천음악장르: {rec_genre}")

if rec_genre == "팝":
    print("팝 음악은 1950년대에 시작된 장르로 단순하고 중독성 있는 멜로디와 경쾌한 리듬이 특징입니다.")
    print(f"추천음악: '{rec_music_pop}'")
elif rec_genre == "록":
    print("록 음악은 1950년대와 60년대에 발전한 장르로 일렉트릭 기타, 드럼, 베이스를 사용하는 것이 특징입니다.")
    print(f"추천음악: '{rec_music_rock}'")
elif rec_genre == "힙합":
    print("힙합은 1970년대에 시작된 장르로 랩, 비트박스, 샘플링 등을 사용하는 것이 특징입니다.")
    print(f"추천음악: '{rec_music_hiphop}'")
elif rec_genre == "R&B":
    print("리듬앤블루스은 1940년대에 시작된 장르로 소물풀한 보컬, 블루스 멜로디, 종종 복잡하나 하모니를 사용하는 것이 특징입니다.")
    print(f"추천음악: '{rec_music_rb}'")
elif rec_genre == "컨트리":
    print("컨트리 음악은 미국 남부메서 시작된 장르로 어크스틱 기타, 피들, 밴조를 사용하는 것이 특징입니다.")
    print(f"추천음악: '{rec_music_country}'")
elif rec_genre == "재즈":
    print("재즈는 19세기 말과 20세기 초에 시작된 장르로 즉흥 연주, 스월 리듬, 금관 악기 및 목관 악기 사용이 특징입니다.")
    print(f"추천음악: '{rec_music_jazz}'")
elif rec_genre == "전자":
    print("전자 음악은 1970년대에 시작한 장르로 전자 악기와 디지털 제작 기술을 사용하는 것이 특징입니다.")
    print(f"추천음악: '{rec_music_electronic}'")
else:
    print("클래식 음악은 중세 시대로 거슬러 올라가는 서양 고전 전통의 음악을 포괄하는 장르입니다. 복잡한 화성, 형식적 구조를 사용하는 것이 특징입니다.")
    print(f"추천음악: '{rec_music_classic}'")