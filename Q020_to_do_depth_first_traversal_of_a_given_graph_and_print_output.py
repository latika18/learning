Question 20
Do a depth first traversal of a given graph, and print the output
Example input:
1 -> 2
1 -> 4
1 -> 5
2 -> 3
3 -> 5
4 -> 2
#consttructor
from collections import defaultdict
import pdb
class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def depth_first_search(self,node):
        visited = [False] * len(self.graph)
        stack = [node]
        visited[node] = True
        while stack:
            
            node = stack.pop()
            print node
            for i in self.graph[node]:
                pdb.set_trace()
                print i
                if not i:
                    break
                
                   
                if visited[i] == False:
                    visited[i] = True
                    stack.append(i)

G = Graph()
G.add_edge(1,2)
G.add_edge(1,4)
G.add_edge(1,5)
G.add_edge(2,3)
G.add_edge(3,5)
G.depth_first_search(1)

