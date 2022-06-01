from concurrent.futures import thread
import time
import win32api, win32con, win32gui, win32file, win32event, win32service, win32serviceutil
import shutil
import os
import threading

drive_types = {
    win32file.DRIVE_UNKNOWN: "Unknown\nDrive type can't be determined.",
    win32file.DRIVE_REMOVABLE: "\nRemovable storage device",
    win32file.DRIVE_FIXED: "Fixed\nDrive has fixed (nonremovable) media. This includes all hard drives, including hard drives that are removable.",
    win32file.DRIVE_REMOTE: "Remote\nNetwork drives. This includes drives shared anywhere on a network.",
    win32file.DRIVE_CDROM: "CDROM\nDrive is a CD-ROM. No distinction is made between read-only and read/write CD-ROM drives.",
    win32file.DRIVE_RAMDISK: "RAMDisk\nDrive is a block of random access memory (RAM) on the local computer that behaves like a disk drive.",
    win32file.DRIVE_NO_ROOT_DIR: "The root directory does not exist.",
}
drives = win32api.GetLogicalDriveStrings().split("\x00")[:-1]
added_drives = 0

for device in enumerate(drives):
    type = win32file.GetDriveType(device[1])
    print(f"{device[-1]} {drive_types[type]}")
    if type == 2:
        print(f"{device[-1]} Removable drive already present...")
        exit()


def watcher():
    while True:
        global added_drives
        added_drives = win32api.GetLogicalDriveStrings().split("\x00")[:-1]
        time.sleep(1)


watching_thread = threading.Thread(target=watcher).start()


def check_watcher_match():
    run_condition = True
    while run_condition:
        if len(drives) == len(added_drives):
            print("No external drives")
            time.sleep(0.1)
        else:
            for index, drive in enumerate(added_drives):
                index, drive
            print("New drive detected")
            run_condition = False
            for device in enumerate(added_drives):
                type = win32file.GetDriveType(device[1])
            print(f"{device[-1]} {drive_types[type]}")
            if not type == 2:
                print(f"{device[-1]} is not removable drive")
                break
            for i in os.listdir(added_drives[-1]):
                if i == "DCIM":
                    print("This is a camera SD card")
                    print("Opening DCIM folders")
                    for ii in os.listdir(os.path.join(device[-1], i)):
                        print(f"{device[-1]} -> {i} -> {ii}")
                        for iii in os.listdir(os.path.join(device[-1], i, ii)):
                            fname, ext = os.path.splitext(iii)
                            print(f"File:{fname} located in {ii} with extension: {ext}")
                            shutil.copy(
                                os.path.join(device[-1], i, ii, iii),
                                f"{os.path.join(device[-1], i, ii, iii)} - COPY{ext}",
                            )
            while True:
                if not len(drives) == len(added_drives):
                    """print("Drive still inserted")
                    time.sleep(1)"""
                    continue
                else:
                    print("Drive removed")
                    check_watcher_match()


checking_thread = threading.Thread(target=check_watcher_match).start()
