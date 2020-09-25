import http.client

conn = ""
settings = ""
connected = False

def printBreak():
    print("------------------------------")

def printMenu():
    printBreak()
    print("Current settings:\n")
    print(settings)
    printBreak()
    print("| A: change framesize")
    print("| B: change image quality")
    print("| C: change AVI length")
    print("| D: begin recording")
    print("| Q: quit")
    printBreak()

def getSettings():
    global settings

    conn.request("GET", "/settings")
    response = conn.getresponse()

    if response.status != 200:
        raise RuntimeError
    else:
        settings = response.read().decode('utf-8')

def connect(ip):
    global conn
    conn = http.client.HTTPConnection(ip, timeout=30)

    print("Attempting connection...")
    getSettings()
    

def changeFramesize():
    printBreak()
    size = input("Enter desired framesize: ")

    conn.request("PUT", "/framesize", size)
    response = conn.getresponse()
    print(response.read().decode('utf-8'))
    getSettings()

def changeQuality():
    printBreak()
    quality = input("Enter desired image quality: ")

    conn.request("PUT", "/quality", quality)
    response = conn.getresponse()
    print(response.read().decode('utf-8'))
    getSettings()

def changeAviLength():
    printBreak()
    length = input("Enter desired AVI length (seconds): ")

    conn.request("PUT", "/avilength", length)
    response = conn.getresponse()
    print(response.read().decode('utf-8'))
    getSettings()

def record():
    printBreak()

    conn.request("PUT", "/record")
    response = conn.getresponse()
    print(response.read().decode('utf-8'))
    getSettings()

#================================

while not connected:
    ip = input("Enter IP address: ")
    try:
        connect(ip)
        connected = True
    except Exception as e:
        print("\nCould not connect to server.\n")

while True:
    printMenu()
    sel = input("Make selection: ")

    try:
        if sel.lower() == 'q':
            break  
        elif sel.lower() == 'a':
            changeFramesize()
        elif sel.lower() == 'b':
            changeQuality()
        elif sel.lower() == 'c':
            changeAviLength()
        elif sel.lower() == 'd':
            record()
    except http.client.RemoteDisconnected:
        connect(ip)
