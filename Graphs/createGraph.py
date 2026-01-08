class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
        else:
            if vertex1 not in self.adj_list.keys():
                print(f"{vertex1} not present")
            elif vertex2 not in self.adj_list.keys():
                print(f"{vertex2} not present in graph")
            else:
                print(f"{vertex1} and {vertex2} not present")
    
    def remove_edge(self,vertex1,vertex2):
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            self.adj_list[vertex1].remove(vertex2)
            self.adj_list[vertex2].remove(vertex1)
        else:
            print("either of the vertexes does not exists")

    def remove_vertex(self,vertex):
        del self.adj_list[vertex]
        
        for ls in self.adj_list.values():
            if vertex in ls:
                ls.remove(vertex)
        

        


    def add_vertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
        
    def print_graph(self):
        for k,v in self.adj_list.items():
            print(f"{k} : {v}",end="\n")
        

graph = Graph()

graph.add_vertex("a")
graph.add_vertex("b")
graph.add_vertex("c")

graph.add_edge("a","b")
graph.add_edge("a","c")
graph.add_edge("b","c")
graph.print_graph()

print("remove vertex")
graph.remove_vertex("c")
graph.print_graph()
