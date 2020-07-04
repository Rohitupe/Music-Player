import os

# This is to get the directory that the program
# is currently running in.
# dir_path = os.path.dirname(os.path.realpath(__file__))

dir_path = ["C:\\","D:\\"]
fileExtension = (".mp3",".wav",".m4p",".aac",".3gp")

allSongs = []

for path in dir_path:
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(fileExtension):
                # print(root + '/' + str(file))
                allSongs.append(file)

print(allSongs)