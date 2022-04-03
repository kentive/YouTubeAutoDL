import datetime as dt

today = dt.datetime.today()

# ダウンロードしたいチャンネルリスト
channel_list = {
    # 東海オンエア
    'tokai':{
        'url': 'https://www.googleapis.com/youtube/v3/search?q=東海オンエア&order=relevance&type=video',
        'rule': today.weekday() != 1 and today.hour == 12
    },
    # 東海オンエアの控え室
    'tokai_sub':{
        'url': 'https://www.googleapis.com/youtube/v3/search?q=東海オンエアの控え室&order=relevance&type=video',
        'rule': today.weekday() == 1 and today.hour == 12
    },
    # オカリナ
    'okarina':{
        'url': 'https://www.googleapis.com/youtube/v3/search?channelId=UCryxFw2ogq1iBVBwvPkQOvg&order=date&type=video',
        'rule': today.hour == 12
    }
}