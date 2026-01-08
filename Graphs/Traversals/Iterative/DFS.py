from collections import deque
class Graph:
    def __init__(self):
        self.adj_list = {}

    def DFS(self,vertex):
        visited = set()
        stack = [vertex]
        while len(stack)>0:
            v = stack.pop()
            if v not in visited:
                print(v)
                visited.add(v)
            for neighbors in self.adj_list[v]:
                if neighbors not in visited:
                    stack.append(neighbors)
                    

    
graph = Graph()
graph.adj_list = {
    "a":["b","c"],
    "b":["a","e"],
    "c":["a","d"],
    "d":["c","e"],
    "e":["b","d"]
}

graph.adj_list = {
    "a": ["b"],
    "b": ["c"],
    "c": ["d"],
    "d": ["b"]  # Cycle back to b
}

graph.DFS("a")
