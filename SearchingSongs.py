import os
import psutil  # pip install psutil


def allSong():
    dir_path = []
    disks = psutil.disk_partitions()
    for disk in disks:
        dir_path.append(disk.device)

    fileExtension = (".mp3",".3gp")
    allSongs = []

    for path in dir_path:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(fileExtension):
                    allSongs.append(root+"\\"+file)
    return allSongs
    # for song in allSongs:
    #     return song

print(allSong())