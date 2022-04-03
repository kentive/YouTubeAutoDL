from pytube import YouTube
import requests
import time
import random
import datetime as dt
import channels
import delete
import config

start_time = time.time()

KEY = config.KEY # YouTubeAPIのアクセスキー
VIDEOS_DIR = config.VIDEOS_DIR # 動画のダウンロード先

today = dt.datetime.today()
yesterday = today - dt.timedelta(1)
yesterdayUTC = yesterday - dt.timedelta(hours=9)

# 前日分の動画を削除
delete.all_delete()

for channel in channels.channel_list.values():
    if channel['rule']:
        req1 = requests.get(channel['url'] + '&part=snippet' + '&maxResults=1' + '&key=' + KEY)
        # 最新動画があればダウンロード
        if req1.json()['items'][0]['snippet']['publishedAt'] >= yesterdayUTC.isoformat():
            yt = YouTube("https://www.youtube.com/watch?v=" + req1.json()['items'][0]['id']['videoId'])
            yt.streams.get_highest_resolution().download(VIDEOS_DIR)
        else:
            req2 = requests.get(channel['url'] + '&maxResults=50' + '&key=' + KEY) # 50の絞り方、もうちょっとランダム性を持たせたい。
            yt = YouTube("https://www.youtube.com/watch?v=" + random.choice(req2.json()['items'])['id']['videoId'])
            yt.streams.get_highest_resolution().download(VIDEOS_DIR)

# txtファイルで重複管理したらなお良い
# txtファイルをリセットできるファンクションを作ってもいいかも

end_time = time.time()
print("処理時間:{0}".format(end_time - start_time))