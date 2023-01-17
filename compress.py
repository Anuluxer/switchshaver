import os
import time

choice = ""
options = list(os.listdir(os.getcwd()))
while not choice in range(len(options)):
    for i in range(len(options)):
        print(f"[{i}] {options[i]}")
    try:
        choice = int(input("Please choose the number of the file you would like to compress: "))
    except:
        print("Please enter a number from the following choices")

FILENAME = options[choice]
SIZE = os.path.getsize(os.getcwd() + "//" + FILENAME)
FILE = open(FILENAME, "rb")

FILE.seek(SIZE - 1)
endHex = hex(ord(FILE.read(1).decode("ANSI")))[2:]

def getHexAt(pos):
    oldPos = FILE.tell()
    FILE.seek(pos)
    try:
        toRet = hex(ord(FILE.read(1).decode("ANSI")))[2:]
        FILE.seek(oldPos)
        return toRet
    except:
        FILE.seek(oldPos)
        return ""

def getFirstF():
    while getHexAt(FILE.tell() - 1) in ["ff", ""] and getHexAt(FILE.tell()) in ["ff", ""] and getHexAt(FILE.tell() + 1) in ["ff", ""]:
        FILE.seek(-1000, 1)
    while not (getHexAt(FILE.tell()) in ["ff", ""] and getHexAt(FILE.tell() + 1) in ["ff", ""] and getHexAt(FILE.tell() + 2) in ["ff", ""]):
        FILE.seek(1, 1)

if endHex == "ff":
    startTime = time.time()
    getFirstF()
    truncStart = FILE.tell()
    FILE.close()
    FILE = open(FILENAME, "a")
    FILE.truncate(truncStart)
    newSize = os.path.getsize(os.getcwd() + "//" + FILENAME)
    print(newSize, SIZE)
    input(f"Compression complete! {round((newSize / SIZE) / 10000000000, 2)}GB saved in {round(startTime - time.time(),2)} seconds.")
else:
    print("File either has an error or is already compressed.")
    input()