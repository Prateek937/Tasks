import subprocess as sb
from time import sleep

def check_disks():
    sb.call("fdisk -l", shell=True)

def mounted():
    sb.call("df -hT", shell=True)

def pvcreate(disk):
    print("Creating physical Volume of {}".format(disk))
    sleep(1)
    sb.call("pvcreate {}".format(disk), shell = True)
    return 0

def pvdisplay():
    sb.call("pvdisplay", shell = True)

def vgcreate(vg_name,disk):
    print("Creating the Volume group...")
    sleep(1)
    sb.call("vgcreate {} {}".format(vg_name, disk), shell = True)
    return 0

def vgdisplay():
    sb.call("vgdisplay", shell = True)

def lvcreate(size, lv_name, vg_name):
    print("Creating the logical volume of {} GB from {}...".format(size, vg_name))
    sleep(1)
    sb.call("lvcreate --size {}G --name {} {}".format(size, lv_name, vg_name), shell = True)
    return "/dev/{}/{}".format(vg_name, lv_name)

def lvdisplay():
    sb.call("lvdisplay", shell = True)

def format(lv_path):
    print("Formatting the Volume...")
    sleep(1)
    sb.call("mkfs.ext4 {}".format(lv_path), shell = True)
    return 0

def mount(mpoint, lv_path):
    sb.call("mkdir {}".format(mpoint), shell = True)
    print("Mounting to {}".format(mpoint))
    sleep(1)
    sb.call("mount {} {}".format(lv_path, mpoint), shell = True)
    return 0

def increase(size_ex, lv_path):
    print("Extending the size by {} GiB...".format(size_ex))
    sleep(1)
    sb.call("lvextend --size +{}G {}".format(size_ex, lv_path))
    print("Resizing the partition...")
    sleep(1)
    sb.call("resize2fs {}".format(lv_path), shell = True)
    return 0

while True:
    
    print("""
        --------------------------------------------------------
        LVM:
        --------------------------------------------------------
        1. Check Disks
        2. See Mounted disks/prtitions
        3. Create a Physical volume
        4. Diplay Physical Volumes
        5. Create a Volume Group
        6. Display Volume Groups
        7. Create Logical Volume
        8. Display all Logical Volumes
        9. Format Logical Volume
       10. Mount Volume 
       11. CREATE LOGICAL VOLUME PARTITION
       12. Increase LV size
       13. Exit the program
    """)

    ch = ''
    while ch == '':
        ch = input("Choice: ")
    ch = int(ch)

    if ch == 1:
        check_disks()
        input()
    elif ch == 2:
        mounted()
        input()
    elif ch == 3:
        disk_name = input("Enter Disk Name: ")
        pvcreate(disk_name)
        input()
    elif ch == 4:
        pvdisplay()
        input()
    elif ch == 5:
        vg_name = input("Volume Group name: ")
        disk_name = input("Disk name: ")
        vgcreate(vg_name, disk_name)
        input()
    elif ch == 6:
        vgdisplay()
        input()
    elif ch == 7:
        size = input("Size of logical volume: ")
        lv_name = input("LV name: ")
        vg_name = input("VG name: ")
        lv_path = lvcreate()
        input()
    elif ch == 8:
        lvdisplay()
        input()
    elif ch == 9:
        format(lv_path)
        input()
    elif ch == 10:
        mpoint = input("Mount point: ")
        mount(mpoint, lv_path)
        input()
    elif ch == 12:
        size = input("Size to increase: ")
        lv_path = input("LV: ")
        increase(size, lv_path)
        input()
    elif ch == 11:
        disk_name = input("Disk Name: ")
        vg_name = input("Volume Group name: ")
        lv_name = input("LV name: ")
        mpoint = input("Mount point: ")
        pvcreate(disk_name)
        vgcreate(vg_name, disk_name)
        lv_path = lvcreate()
        format(lv_path)
        mount(mpoint, lv_path)
        input()
    elif ch == 13:
        exit()

    else:
        print("Not Supported!")
        input()