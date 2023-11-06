import os

devices_dir = '/media/pi'
devices_list = []
playlist = []

for d in os.listdir(devices_dir):
    if d != 'SETTINGS':
        devices_list.append(d)
music_dir = devices_dir + '/' + devices_list[0]
for current_dir, sub_dirs, contained_files in os.walk(music_dir):
    for file in contained_files:
        name, extension = os.path.splitext(file)
        if extension == '.mp3':
            playlist.append(file)
