import win32file
import os
import vlc
import random
import time


def locate_usb_drive(index):
    drive_list = []
    drivebits = win32file.GetLogicalDrives()
    for d in range(1,26):
        mask = 1 << d
        if drivebits & mask:
            # here if the drive is at least there
            drname = '%c:\\' % chr(ord('A')+d)
            t = win32file.GetDriveType(drname)
            if t == win32file.DRIVE_REMOVABLE:
                drive_list.append(drname)
    if not drive_list == []:
        return drive_list[index]
    else:
        return None


def locate_audio_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp3') or file.endswith('.wav') or file.endswith('.ogg'):
                file_list.append(os.path.join(root, file))
    if not file_list == []:
        return file_list
    else:
        return None


drive = locate_usb_drive(0)
print(drive)
mp3_files = locate_audio_files(drive)
print(mp3_files)
to_play = random.choice(mp3_files)
player = vlc.MediaPlayer(to_play)
player.play()
time.sleep(4)
player.stop()
