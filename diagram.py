import networkx as nx
import matplotlib.pyplot as plt
import json


class Graph():
    def __init__(self,deviceFile):
        self.deviceFile = deviceFile
        self.data = ""
        self.graph = nx.Graph()
        self.devList = []
        self.IPList = []
        self.hostList = []
        self.hopList = []
        self.loadData()
        self.createNodes()



    def loadData(self):
        with open(self.deviceFile) as json_file:
            self.data = json.load(json_file)
        print(self.data)

        for item in self.data["Devices"]:
            self.IPList.append(item["IP"])
            self.hostList.append(item["Hostname"])
            self.hopList.append(item["Hops"])
    
    def createNodes(self):
        for i in range(len(self.devList)):
            self.graph.add_node(i)
            self.graph.add_edge(self.devList[0],i)
        nx.draw_random(self.graph)
        plt.show()





graph = Graph("deviceData.json")