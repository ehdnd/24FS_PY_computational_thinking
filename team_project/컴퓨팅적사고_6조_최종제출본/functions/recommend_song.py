from functions.gpt import diary_to_emotion
from functions.scrape_melon_chart import get_genre_all_songs
import random

# diary 변수로 받으면 추천곡
def recommend_song(diary):
    emotion = diary_to_emotion(diary)   #gpt에 있는 함수
    # emotion = "else인 경우확인"
    # emotion = '즐거움'

    print(f"일기에 따른 감정은 '{emotion}'입니다. ")

    if emotion in ('기쁨', '즐거움'):
        num = 200
        genre = "댄스"
    elif emotion == '슬픔':
        num = 100
        genre = "발라드"
    elif emotion == '분노':
        num = 600
        genre = "록/메탈"
    elif emotion == '두려움':
        num = 500
        genre = "인디음악"
    elif emotion == '혐오':
        num = 300
        genre = "랩/힙합"
    elif emotion == '놀람':
        num = 100
        genre = "발라드"
    elif emotion == '외로움':
        num = 400
        genre = "R&B/Soul"
    else:
        num = None
        genre = None

    all_songs = get_genre_all_songs(num)    # [ {곡 정보} 모인 ] 리스트 반환
    
    # 오류 -> all_songs = [] / "error" return

    # 오류가 아니라면 랜덤으로 뽑은 { 음악 데이터 } return
    if all_songs != []:
        song = random.choice(all_songs)
        song["genre"] = genre
        # print(f"[{song['rank']}위] 추천곡: {song['title']}, 아티스트: {song['artist']}")
        return song
    else:
        return "error"