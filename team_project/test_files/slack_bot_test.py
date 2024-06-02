from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from dotenv import load_dotenv

import json

import requests
from bs4 import BeautifulSoup

load_dotenv()
slack_token = os.getenv("slack_token")

print(slack_token)

all_songs = []

print("발라드: 100, 댄스: 200, 랩/힙합: 300, R&B/Soul: 400, 인디음악: 500, 록/메탈: 600, 트로트: 700, 포크/블루스: 800")
num = input("숫자 입력: ")

song_url = f"https://www.melon.com/genre/song_list.htm?gnrCode=GN0{num}"

response = requests.get(
      song_url,
      headers={
          "User-Agent":
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Whale/3.24.223.18 Safari/537.36"
      })

client = WebClient(token=slack_token)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # 장르별 차트인 경우
    songs = soup.find("div", id="songList").find("tbody").find_all("tr")

    # 멜론차트 TOP100인 경우
    # songs = soup.find_all("tr", class_="lst50") + soup.find_all("tr", class_="lst100")

    for song in songs:
        title = song.find("div", class_="rank01").text.strip('\n')
        artist = song.find("div", class_="rank02").find("a").text.strip('\n')
        songs_data = {
        "title": title,
        "artist": artist
        }
        all_songs.append(songs_data)

    try:
        songs_str = json.dumps(all_songs, ensure_ascii=False, indent=2)

        response = client.chat_postMessage(
            channel="C0631FF2R6U", #채널 id를 입력합니다.
            # text= songs_str
            text= f"{str(len(all_songs))}개 음악 검색됨"
        )
    except SlackApiError as e:
        assert e.response["error"]

else:
    response = client.chat_postMessage(
    channel="C0631FF2R6U", #채널 id를 입력합니다.
    text= "Can't get songs..."
)
