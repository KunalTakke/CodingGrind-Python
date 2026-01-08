from collections import deque
class Graph:
    def __init__(self):
        self.adj_list = {}

    def BFS(self,vertex):
        visited = set() # initialize a set 
        visited.add(vertex)
        queue = deque()
        queue.append(vertex) # add first element
        while len(queue)>0:
            v = queue.popleft()
            print(v)
            for neighbors in self.adj_list[v]:
                if neighbors not in visited:
                    visited.add(neighbors)
                    queue.append(neighbors)
        
    



    
graph = Graph()
graph.adj_list = {
    "a":["b","c"],
    "b":["a","e"],
    "c":["a","d"],
    "d":["c","e"],
    "e":["b","d"]
}
graph.BFS("a")
