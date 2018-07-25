Our first problem is to figure out how to turn a large collection of words into a graph. 
What we would like is to have an edge from one word to another if the two words are only different by a single letter. 
If we can create such a graph, then any path from one word to another is a solution to the word ladder puzzle. 
Figure 1 shows a small graph of some words that solve the 
FOOL to SAGE word ladder problem. Notice that the graph is an undirected graph and that the edges are unweighted.
