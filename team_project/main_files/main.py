# import requests
# from bs4 import BeautifulSoup
from gpt_api import diary_to_emotion
from melon_chart import get_songs
import random

# all_songs = []

# emotion = diary_to_emotion()
emotion = "fasd" #else
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
    print("gpt 오류")
    num = None

# # print("발라드: 100, 댄스: 200, 랩/힙합: 300, R&B/Soul: 400, 인디음악: 500, 록/메탈: 600, 트로트: 700, 포크/블루스: 800")
# # num = input("숫자 입력: ")

# song_url = f"https://www.melon.com/genre/song_list.htm?gnrCode=GN0{num}"

# response = requests.get(
#       song_url,
#       headers={
#           "User-Agent":
#           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Whale/3.24.223.18 Safari/537.36"
#       })


# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, "html.parser")

#     # 장르별 차트인 경우
#     songs = soup.find("div", id="songList").find("tbody").find_all("tr")

#     # 멜론차트 TOP100인 경우
#     # songs = soup.find_all("tr", class_="lst50") + soup.find_all("tr", class_="lst100")
    
#     n = 1
#     for song in songs:
#         title = song.find("div", class_="rank01").text.strip('\n')
#         artist = song.find("div", class_="rank02").find("a").text.strip('\n')
#         songs_data = {
#         "rank": n,
#         "title": title,
#         "artist": artist
#         }
#         all_songs.append(songs_data)
#         n += 1

#     print(len(all_songs))


# else:
#     print("Can't get Songs.")

all_songs = get_songs(num)

if all_songs == []:
    songs = random.choice(all_songs)
    print(f"추천곡: {songs['title']}, 아티스트: {songs['artist']}")