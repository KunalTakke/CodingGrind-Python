

class Graph:
    def __init__(self):
        self.gdict={}

    def add_vertex(self,vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = []
            return True
        return False

    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].append(vertex2)
            self.gdict[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self,vertex1,vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            try:
                self.gdict[vertex1].remove(vertex2)
                self.gdict[vertex2].remove(vertex1)
                return True
            except ValueError:
                return False
            

    def remove_vertex(self,vertex):
        if vertex in self.gdict.keys():
            for v in self.gdict[vertex]:
                self.gdict[v].remove(vertex)
            del self.gdict[vertex]
            return True
        return False


        



    
    def print_graph(self):
        for vertex in self.gdict.keys():
            print(vertex,":",self.gdict[vertex])

        




graph=Graph()
graph.add_vertex("a")
graph.add_vertex("b")
graph.add_edge("a","b")
graph.add_vertex("c")
graph.add_edge("a","c")
graph.add_vertex("d")
graph.print_graph()
graph.remove_edge("a","c")
print("Printing after remove edge btw a and c")
graph.print_graph()
print("printing deleting vertex d")
graph.remove_vertex("d")
graph.print_graph()