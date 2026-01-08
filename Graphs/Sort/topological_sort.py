
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            self.adj_list[vertex1].append(vertex2)
            # self.adj_list[vertex2].append(vertex1)
        else:
            if vertex1 not in self.adj_list.keys():
                print(f"{vertex1} not present")
            elif vertex2 not in self.adj_list.keys():
                print(f"{vertex2} not present in graph")
            else:
                print(f"{vertex1} and {vertex2} not present")


    def add_vertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []

    def topological_sort(self,vertex):
        
        def topological_sortUtil(vertex,stack):
            if len(self.adj_list[vertex])>0: #have neighbor
                for neighbor in self.adj_list[vertex]:
                    topological_sortUtil(neighbor)
                   
                stack.append(vertex)
                visited.add(vertex)
            return
            

        visited = set()
        stack = []
        topological_sortUtil(vertex,stack)
        print(stack)
        
        

    
graph = Graph()
# vertex
graph.add_vertex("a")
graph.add_vertex("b")
graph.add_vertex("c")
graph.add_vertex("d")
graph.add_vertex("e")
graph.add_vertex("f")
graph.add_vertex("g")
graph.add_vertex("h")

# edge
graph.add_edge("a","c")
graph.add_edge("c","e")
graph.add_edge("e","h")
graph.add_edge("e","f")
graph.add_edge("f","g")
graph.add_edge("b","d")
graph.add_edge("b","c")
graph.add_edge("d","f")

graph.topological_sort("a")

