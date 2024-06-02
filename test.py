import requests

response = requests.get(
      "https://www.melon.com/genre/song_list.htm?gnrCode=GN00sajdifoealkjsdf",
      headers={
          "User-Agent":
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Whale/3.24.223.18 Safari/537.36"
      })

print(response.status_code)