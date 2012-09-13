import datetime
from song_picker import SongPicker
while(1==1):
    now = datetime.datetime.now()
    if (now.hour == 20 and now.minute == 29):
        SongPicker.player()
