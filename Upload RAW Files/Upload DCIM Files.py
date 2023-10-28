import time
import win32api
import win32file
import os
import threading

# A dictionary to map drive types to their descriptions.
drive_types = {
    win32file.DRIVE_UNKNOWN: "Unknown - Drive type can't be determined.",
    win32file.DRIVE_REMOVABLE: "Removable storage device",
    win32file.DRIVE_FIXED: "Fixed - Drive has fixed (nonremovable) media. This includes all hard drives, including hard drives that are removable.",
    win32file.DRIVE_REMOTE: "Remote - Network drives. This includes drives shared anywhere on a network.",
    win32file.DRIVE_CDROM: "CDROM - Drive is a CD-ROM. No distinction is made between read-only and read/write CD-ROM drives.",
    win32file.DRIVE_RAMDISK: "RAMDisk - Drive is a block of random access memory (RAM) on the local computer that behaves like a disk drive.",
    win32file.DRIVE_NO_ROOT_DIR: "The root directory does not exist.",
}

# Get a list of logical drives.
drives = win32api.GetLogicalDriveStrings().split("\x00")[:-1]

# Variable to track the number of added drives.
added_drives = 0

# Check for removable drives and exit if found.
for device in enumerate(drives):
    type = win32file.GetDriveType(device[1])
    print(f"{device[-1]} {drive_types[type]}")
    if type == 2:
        print(f"{device[-1]} Removable drive already present...")
        exit()

# Function to watch for changes in drives.
def watcher():
    while True:
        global added_drives
        added_drives = win32api.GetLogicalDriveStrings().split("\x00")[:-1]
        time.sleep(1)

# Start a separate thread to watch for drive changes.
watching_thread = threading.Thread(target=watcher)
watching_thread.start()

# Function to check for newly added drives.
def check_watcher_match():
    run_condition = True
    while run_condition:
        if len(drives) == len(added_drives):
            print("No external drives")
            time.sleep(0.1)
        else:
            print("New drive detected")
            run_condition = False
            for device in enumerate(added_drives):
                type = win32file.GetDriveType(device[1])
                print(f"{device[-1]} {drive_types[type]}")
                if not type == 2:
                    print(f"{device[-1]} is not a removable drive")
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

# Start a separate thread to check for newly added drives.
checking_thread = threading.Thread(target=check_watcher_match)
checking_thread.start()
