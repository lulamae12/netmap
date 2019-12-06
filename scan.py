from getmac import getmac
import socket,subprocess,os


validAddresses = []

def saveToFile(list):
    with open("ipMacAdds.json","w") as outfile:
        outfile.dumps(validAddresses)


def decodeMac(ip,mac):


def scan(firs,las):
    address = firs + las
    IP = address
    macAddress = getmac.get_mac_address(ip=str(address))
    
    if macAddress:
        addressDict = {
            "IP": IP,
            "MAC": macAddress
        }
        print("Received",IP)
        validAddresses.append(addressDict)


hostname = socket.gethostname()
hostIPAdress = socket.gethostbyname(hostname)
print("\nHost Name: "+hostname)
print("Host IP: "+hostIPAdress)
print("\n")


print("Starting Scan.\nThis will take a while....")

for i in range(1,256):
    scan("192.168.56.",str(i))




print("\nDone!")
print(validAddresses)
# Changing the port used for updating ARP table (UDP packet)
