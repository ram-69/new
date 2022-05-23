#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import deque
class Graph:
    def __init__(self,edges,n):
        #self.adjlist=[[] for _ in range(n)]
        self.adjlist=[[0 for i in range(n+1)] for _ in range(n+1)]
        for i in edges:
            self.adjlist[i[0]].append(i[1])
#             self.adjlist[dest].append(src)
            
def BFS(graph,v,discovered):
    q=deque()
    discovered[v]=False
    q.append(v)
    while q:
        v=q.popleft()
        if (v!=0):
            print(v,end=" ")
        for u in graph.adjlist[v]:
            if not discovered[u]:
                discovered[u]=True
                q.append(u)
# edges = [
# # 		(1, 9), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
# # 		(5, 10), (4, 7), (4, 8), (7, 11), (7, 12)
# 		# vertex 0, 13, and 14 are single nodes
# ]

def DFS(graph,v,discovered1):
    list1=[]
    list1.append(v)
    while len(list1)!= 0:
        
        abc=list1.pop()
        if (abc!=0):
            print(abc,end=" ")
        for i in graph.adjlist[abc]:
            if not discovered1[i]:
                discovered1[i]=True
                list1.append(i)
    return None
    
print("Enter Number Of Vertices\n")
n=int(input())

edges=[]
print("Enter Number Of Edges\n")
e=int(input())
for i in range(e):
    abc=input().split(" ")
    abc=[int(i) for i in abc]
    edges.append(abc)

    
discovered=[False]*(n+1)
discovered1=[False]*(n+1)
graph=Graph(edges, n)
for i in range(1,n):
    if not discovered[i]:
        BFS(graph, i, discovered) 
print("\n")
for i in range(1,n):
    if not discovered1[i]:
        DFS(graph, i, discovered1) 


# In[ ]:




