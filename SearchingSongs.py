import os

dir_path = ["C:\\","D:\\","F:\\"]
fileExtension = (".mp3",".wav",".m4p",".aac",".3gp")

allSongs = []

for path in dir_path:
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(fileExtension):
                allSongs.append(file)

for song in allSongs:
    print(song)