from getmac import getmac
import socket


validAddresses = []
def getHostIp():
    hostname = socket.gethostname()
    hostIPAdress = socket.gethostbyname(hostname)
    
    print("\nHost Name: "+hostname)
    print("Host IP: "+hostIPAdress)
    print("\n")
    
    ipList = hostIPAdress.rpartition(".")

    ipPrefix = ipList[0] + "."
    
    return ipPrefix

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
    

print("Starting Scan.\nThis will take a while....")
prefix = getHostIp()
for i in range(1,256):
    scan(prefix,str(i))
print("\nDone!")
print(validAddresses)
# Changing the port used for updating ARP table (UDP packet)
