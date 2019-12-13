from getmac import getmac
import os,time,sys,json,socket,subprocess,ipaddress,signal
from netaddr import *
from ipaddress import ip_network

from urllib.request import urlopen
validAddresses = {}
validAddresses["Devices"] = []

   



class ScanNetwork():
    def __init__(self):
        
        #os.system('cls')
        machineIpAddress = socket.gethostbyname(socket.gethostname())
        print("IP of this machine: ",machineIpAddress)
        rangeMin = int(input("\nMinimum value of ip address: "))
        rangeMax = int(input("\nMaxium value of ip address: "))
        octetCount = int(input("\nOctets to iterate through (default = 1): "))
        ipPrefix = input("\nIP prefix : ")
        self.traceRouteQ = input("\nTrace Routes?: ")
        self.macAddrData = self.loadDict("macAddreses.json")
        ipPrefix = ipPrefix + "."
        self.ipPrefix = ipPrefix
        networkID = self.ipPrefix + "0"
        

        #self.iterThroughIpsBrute(rangeMin,rangeMax)
        if octetCount == 1:
            self.iterThroughIps(rangeMin,rangeMax+1)
        if octetCount == 2:
            self.iterThroughIpsTwo(rangeMin,rangeMax+1)
        if octetCount == 3:
            self.iterThroughIpsThree(rangeMin,rangeMax+1)
        if octetCount == 4:
            self.iterThroughIpsFour(rangeMin,rangeMax+1)

    def traceRoutes(self,ip):
        hopList = []
        result = subprocess.Popen(["tracert","-h","5",ip],stdout=subprocess.PIPE)
        result = result.communicate()[0]
        #print("Resul: ",result)
        resultSplit = result.decode("utf-8").split("\r\n")
        
        for item in resultSplit:
            if "ms" in item:
                hop = item.replace("\r\n","")
                hopList.append(hop)

        #print(resultSplit)
        print(hopList)
        hopCount = len(hopList)
        print(hopCount)
        return hopCount
    def scanForMac(self,last):
        
        
        vend = ""
        data = {}
        hopCount = 1
        data["IP info"] = []
        address = str(self.ipPrefix) + str(last)
        IP = address
        
        
        hostname = IP
        
        if "y" in self.traceRouteQ or "1" in self.traceRouteQ:
            hopCount = self.traceRoutes(IP)
        

        print("\n Scanning IP: ",IP,"\n")
        print(socket.getfqdn(IP))
       
        macAddress = getmac.get_mac_address(ip=str(address))

        if macAddress:
            vendor = self.findVendor(macAddress)
            try:
                hostname,aliasList,lanIP = socket.gethostbyaddr(socket.gethostbyname(IP))
            except:
                hostname = ""
                pass
            
            addressDict = {
                "IP": IP,
                "MAC": macAddress,
                "Vendor":vendor,
                "Hostname":hostname,
                "Hops":hopCount
                
                
            }
            print("Received",IP)
            print(addressDict)
            validAddresses["Devices"].append(addressDict)
            
    def findVendor(self,macAddress):
        vendorID = macAddress.split(":",3)
        vendorID = vendorID[0].upper() + vendorID[1].upper() + vendorID[2].upper()    
        for address in self.macAddrData["Macs"]:
                if address["address"] == vendorID:
                    addr = address["address"]
                    vendor = address["vendor"]
                    return vendor



    def iterThroughIps(self,rangeMin,rangeMax ):
        for i in range(int(rangeMin),int((rangeMax))):
            self.scanForMac(i)
            
        self.saveDict()
    def iterThroughIpsTwo(self,rangeMin,rangeMax ):
        for i in range(int(rangeMin),int((rangeMax))):
            for j in range(int(rangeMin),int((rangeMax))):
                self.scanForMac(str(i)+"."+str(j))
            
            self.saveDict()
    def iterThroughIpsThree(self,rangeMin,rangeMax ):
        for i in range(int(rangeMin),int((rangeMax))):
            for j in range(int(rangeMin),int((rangeMax))):
                for k in range(int(rangeMin),int((rangeMax))):
                    self.scanForMac(str(i)+"."+str(j)+"."+str(k))
            
        self.saveDict()
    def iterThroughIpsFour(self,rangeMin,rangeMax ):
        for i in range(int(rangeMin),int((rangeMax))):
            for j in range(int(rangeMin),int((rangeMax))):
                for k in range(int(rangeMin),int((rangeMax))):
                    for l in range(int(rangeMin),int((rangeMax))):
                        self.scanForMac(str(i)+"."+str(j)+"."+str(k)+"."+str(l))
        self.saveDict()

    def saveDict(self):
        with open("devices.json","w") as outFile:
            json.dump(validAddresses,outFile,indent=4)
        outFile.close()

    def loadDict(self,file):
        with open(file) as json_file:
            data = json.load(json_file)
        return data


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

scan = ScanNetwork()


os.system('cls')
updateMacQuest = input("Update Mac Addresses? : ")
if "y" in updateMacQuest:
    DownloadMacs = DownloadMacs()

time.sleep(.5)
os.system('cls')
updateQuest = input("Scan Network? : ")
if "y" in updateQuest:
    time.sleep(2)
    os.system('cls')
    scan = ScanNetwork()
os.system('cls')