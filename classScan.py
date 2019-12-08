from getmac import getmac
import os,time,sys,json,socket
from urllib.request import urlopen
validAddresses = {}
validAddresses["Devices"] = []
class DecodeDevices():
    def __init__(self):
        print("decoding File")
        self.deviceJsonData = self.loadDict("devices.json")
        self.macAddrData = self.loadDict("macAddreses.json")
        self.getMacVendorSeg()


    def getMacVendorSeg(self):#gets vendor segment and rewrite file
        devs = {}
        devs["Devices"] = []
        
        
        for item in self.deviceJsonData["Devices"]:
            macAddress = item["MAC"]
            ip = item["IP"]
            print("mac addr",macAddress)
            vendorID = macAddress.split(":",3)
            
            vendorID = vendorID[0].upper() + vendorID[1].upper() + vendorID[2].upper()
            
            print(vendorID)
            
            for address in self.macAddrData["Macs"]:
                if address["address"] == vendorID:
                    addr = address["address"]
                    vend = address["vendor"]
                    hostname = socket.gethostbyname_ex(ip)
                  
                    print(hostname)
                              



                    addressDict = {
                        "IP": ip,
                        "MAC": macAddress,
                        "Vendor":vend,
                        "Hostname":hostname
                    }
                
                    devs["Devices"].append(addressDict)

        with open("deviceData.json","w") as outFile:
            json.dump(devs,outFile,indent=4)
        outFile.close()


    def loadDict(self,file):
        with open(file) as json_file:
            data = json.load(json_file)
        return data
    
   



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
        
        with open("devices.json","w") as outFile:
            json.dump(validAddresses,outFile,indent=4)
        outFile.close()

    def scanForMac(self,last):
        
        

        data = {}
        data["IP info"] = []
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
            validAddresses["Devices"].append(addressDict)
            


    def iterThroughIps(self,rangeMin,rangeMax ):
        for i in range(int(rangeMin),int((rangeMax-1))):
            os.system('cls')
            self.scanForMac(i)
        self.saveDict()


class DownloadMacs():
    def __init__(self):
        self.macSanURL = "https://linuxnet.ca/ieee/oui/nmap-mac-prefixes"

        self.downloadSan()


    def downloadSan(self):
        data = {}
        data["Macs"] = []
        dataFile = urlopen(self.macSanURL)
        lineCount = 0
        skipCount = 0 
        for line in dataFile:
            line = line.decode("utf-8")
            line=line.replace("\t",":");line=line.replace("\n","")
            
            print(line)
            try:
                mac,vendor = line.split(":")
            except:
                skipCount = skipCount + 1
                pass

            print(line)
            lineCount = lineCount + 1
            data["Macs"].append({
                "address":mac,
                "vendor":vendor
                })
            #print(lines)
        
        with open("macAddreses.json","w") as outFile:
            json.dump(data,outFile,indent=4)

        outFile.close
        print("Downloaded: ",lineCount," lines")

        with open('macAddreses.json') as json_file:
            data = json.load(json_file)
        for p in data['Macs']:
            print('Address: ' + p['address'])
            print('Vendor: ' + p['vendor'])
            
            print('')
        print("Downloaded: ",lineCount," lines")
        print("skipped: ",skipCount," lines")




#DownloadMacs = DownloadMacs()

#time.sleep(3)
os.system('cls')
updateQuest = input("Scan Network? : ")
if "y" in updateQuest:
    update = UpdateMacs()

DecodeDevices()