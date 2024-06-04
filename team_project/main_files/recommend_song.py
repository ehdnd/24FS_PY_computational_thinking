from gpt import diary_to_emotion
from scrape_melon_chart import get_genre_all_songs
import random

# diary 변수로 받으면 추천곡
def recommend_song(diary):
    emotion = diary_to_emotion(diary)   #gpt에 있는 함수
    # emotion = "else인 경우확인"
    # emotion = '즐거움'

    print(emotion)

    if emotion in ('기쁨', '즐거움'):
        num = 200
    elif emotion == '슬픔':
        num = 100
    elif emotion == '분노':
        num = 600
    elif emotion == '두려움':
        num = 500
    elif emotion == '혐오':
        num = 300
    elif emotion == '놀람':
        num = 100
    elif emotion == '외로움':
        num = 400
    else:
        num = None

    all_songs = get_genre_all_songs(num)    # [ {곡 정보} 모인 ] 리스트 반환
    
    # 오류 -> all_songs = [] / "error" return

    # 오류가 아니라면 랜덤으로 뽑은 { 음악 데이터 } return
    if all_songs != []:
        songs = random.choice(all_songs)
        # print(f"[{songs['rank']}위] 추천곡: {songs['title']}, 아티스트: {songs['artist']}")
        return songs
    else:
        return "error"