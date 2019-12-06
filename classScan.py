from getmac import getmac
import os,time
from urllib.request import urlopen

validAddresses = []

class UpdateMacs():
    def __init__(self):
        
        os.system('cls')
        #rangeMin = int(input("\nMinimum value of ip address: "))
        #rangeMax = int(input("\nMaxium value of ip address: "))
        ipPrefix = input("\nFirst three sets of ip address: ")
        
        rangeMin = 0
        rangeMax = 255
        ipPrefix = ipPrefix + "."
        
        self.ipPrefix = ipPrefix

        self.iterThroughIps(rangeMin,rangeMax)


    def saveDict(self):
        with open("ipMacAdds.txt","w") as outfile:
            for item in validAddresses:
                print(item)
                outfile.write(item)
                outfile.write("\n")
        outfile.close()

    def scanForMac(self,last):
        
        


        os.system('cls')
        address = str(self.ipPrefix) + str(last)
        IP = address

        print("\n Scanning IP: ",IP,"\n")
        print(validAddresses)


        macAddress = getmac.get_mac_address(ip=str(address))

        if macAddress:
            addressDict = {
                "IP": IP,
                "MAC": macAddress
            }
            print("Received",IP)
            validAddresses.append(addressDict)
        

    def iterThroughIps(self,rangeMin,rangeMax ):
        for i in range(int(rangeMin),int((rangeMax-1))):
            os.system('cls')
            self.scanForMac(i)
        self.saveDict


class DownloadMacs():
    def __init__(self):
        self.macSanURL = "https://linuxnet.ca/ieee/oui/nmap-mac-prefixes"

        self.downloadSan()


    def downloadSan(self):
        lines = []
        dataFile = urlopen(self.macSanURL)
        lineCount = 0
        for line in dataFile:
            line = line.decode("utf-8")
            line=line.replace("\t",":");line=line.replace("\n","")
            

            
            print(line)
            lineCount = lineCount + 1
            lines.append(line)
        
        with open("macAddreses.txt","w") as outFile:
            for line in lines:
                outFile.write(line)
                outFile.write("\n")

        outFile.close
        print("Downloaded: ",lineCount," lines")





DownloadMacs = DownloadMacs()

time.sleep(3)
os.system('cls')
updateQuest = input("Scan Network? : ")
if "y" in updateQuest:
    update = UpdateMacs()