Question 20
Do a depth first traversal of a given graph, and print the output
Example input:
1 -> 2
1 -> 4
1 -> 5
2 -> 3
3 -> 5
4 -> 2
from collections import defaultdict

class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def depth_first_search(self,node):
        visited = []
        stack = [node]
       
        while stack:
            
            node = stack.pop()
            if node not in visited:
                print node
                visited.append(node)
            
                for i in self.graph[node]:
                    stack.append(i)
            


G = Graph()
G.add_edge(1,2)
G.add_edge(1,4)
G.add_edge(1,5)
G.add_edge(2,3)
G.add_edge(3,5)
G.depth_first_search(1)
