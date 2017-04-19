import random
import subprocess
import time
import os

'''
Add below if you want to use this at crontab
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
'''
count = 0

def readMacsFile():
    file = open(os.path.abspath("./maclist.txt"))
    macs = []

    for mac in file.read().splitlines():
        if not mac.startswith("#"):
            macs.append(mac)

    return macs

def execute(command):
    subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)


def changeMacAddress(macAddress):
    global count

    execute("killall hostapd")
    execute("ifconfig wlan0 down")
    time.sleep(2)
    execute("ifconfig wlan0 hw ether " + macAddress)
    execute("ifconfig wlan0 up")
    time.sleep(1)

    execute("service isc-dhcp-server restart")
    execute("hostapd " + os.path.abspath("./hostapd.conf"))
    #time.sleep(1)
    #execute("tcpdump -i wlan0 -w " + os.path.abspath(".") + "/dump" + str(count))
    #count += 1


if __name__ == '__main__':
    macList = readMacsFile()
    random.shuffle(macList)
    index = 0

    #execute("bash " + os.path.abspath(".") + "/Firewall.sh")

    while True:
        changeMacAddress(macList[index])
        print("Changed mac address to " + macList[index])

        index += 1
        if index == len(macList): index = 0
        time.sleep(57)
