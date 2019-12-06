from getmac import getmac

validAddresses = []

def scan(firs,las):
    address = firs + las
    IP = address
    macAddress = getmac.get_mac_address(ip=str(address))
    
    if macAddress:
        addressDict = {
            "IP": IP,
            "MAC": macAddress
        }
        print("received",IP)
        validAddresses.append(addressDict)

print("Starting Scan.\nThis will take a while....")
for i in range(1,256):
    scan("192.168.86.",str(i))
print("\nDone!")
print(validAddresses)
# Changing the port used for updating ARP table (UDP packet)
