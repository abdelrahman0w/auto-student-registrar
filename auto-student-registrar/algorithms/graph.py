class di:
    def __init__(self) -> None:
        self.graph = {}
    
    def addNode(self, node) -> None:
        if node not in self.graph:
            self.graph[node] = []

    def addEdge(self, node, value) -> None:
        if node in self.graph:
            self.graph[node].append(value)
    
    def removeEdge(self, node, value) -> None:
        if node in self.graph:
            self.graph[node].remove(value)

    @property
    def getEdges(self) -> list:
        edges = []
        for node in self.graph:
            for neighbour in self.graph[node]:
                edges.append((node, neighbour))
        return edges
    
    def getGraph(self) -> dict:
        return self.graph