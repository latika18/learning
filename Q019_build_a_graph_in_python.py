Build a graph in python, given its edge representation.
Example input:
1 -> 2
1 -> 4
1 -> 5
2 -> 3
3 -> 5
4 -> 2

from collections import defaultdict

graph = { '1' : ['2' ,'4','5'],
          '2' : ['3'] ,
          '3' : ['5'] ,
          '4' : ['2']
          }

def generate_edges(graph):
    edges = []

    for node in graph:
        for next_node in graph[node]:
            #if edge exist than append
            edges.append((node,next_node))
    return edges


def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
     
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath:
                    return newpath
        return None


print generate_edges(graph)

print find_path(graph, '1','5')

 
