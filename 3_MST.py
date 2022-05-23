#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys 
class Graph():
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]
	def printMST(self, parent):
		for i in range(1, self.V):
			print (parent[i], "-", i, "\t", self.graph[i][parent[i]])
	def minKey(self, key, mstSet):
		min = sys.maxsize
		for v in range(self.V):
			print(v)
			if key[v] < min and mstSet[v] == False:
				min = key[v]
				min_index = v
		return min_index
	def primMST(self):
		key = [sys.maxsize] * self.V
		parent = [None] * self.V # Array to store constructed MST
		key[0] = 0
		mstSet = [False] * self.V
		parent[0] = -1 # First node is always the root of
		for cout in range(self.V):
			u = self.minKey(key, mstSet)
			mstSet[u] = True
			for v in range(self.V):
				if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
						key[v] = self.graph[u][v]
						parent[v] = u
		self.printMST(parent)

print("Enter No of Vertices\n")
n=int(input())
g = Graph(n)
tem=[[0 for i in range(n)] for j in range(n)]
print("Enter No of edges\n")
m=int(input())
print("Enter edges in the form of SRC DEST WEIGHT \n")
for k in range(m):
        abc=input().split(" ")
        abc=[int(i) for i in abc]
        tem[abc[0]][abc[1]]=abc[2]
        tem[abc[1]][abc[0]]=abc[2]
        
    
g.graph =tem 
g.primMST()

#g.graph = [ [0, 2, 0, 6, 0],
# 			[2, 0, 3, 8, 5],
# 			[0, 3, 0, 0, 7],
# 			[6, 8, 0, 0, 9],
# 			[0, 5, 7, 9, 0]]


# In[ ]:




