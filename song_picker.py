import os
from weather_fetcher import WeatherFetcher
class SongPicker:
    @staticmethod
    def player():
        wObj = WeatherFetcher()
        tempState = wObj.whichTempLevel()
        temp = wObj.tempFetch()
        print temp
        file_name = "Music/" + str(tempState)
        print file_name
        os.chdir(file_name)
        os.system('find -type f -iname \\*.mp3 >> playlist.txt')
        os.system('find -type f -iname \\*.wma >> playlist.txt')
        os.system('find -type f -iname \\*.flac >> playlist.txt')
        os.system('find -type f -iname \\*.ogg >> playlist.txt')
        os.system('find -type f -iname \\*.m4a >> playlist.txt')
        os.system('mplayer -shuffle -playlist playlist.txt')
