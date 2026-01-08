class Graph:
    def __init__(self):
        self.adj_list = {}

    def DFS(self,vertex):# in recursive DFS the order is different since we process left vertex first    
        
        def DFSRec(vertex, visited):
            
            # print if not visited 
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)

            # loop over the neighbors
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    DFSRec(neighbor,visited)
            
        visited = set()
        DFSRec(vertex,visited)


            

    
graph = Graph()
graph.adj_list = {
    "a":["b","c"],
    "b":["a","e"],
    "c":["a","d"],
    "d":["c","e"],
    "e":["b","d"]
}

# graph.adj_list = {
#     "a": ["b"],
#     "b": ["c"],
#     "c": ["d"],
#     "d": ["b"]  # Cycle back to b
# }
graph.DFS("a")
