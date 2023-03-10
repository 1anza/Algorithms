# -*- coding: utf-8 -*-
"""PS8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kVuW4GFO2cbYfLJwu2VSSmiWb_G34nVw
"""

import heapq

#inputs
nm = list(map(int,input().split()))
n = nm[0]
m = nm[1]

adjList = [[] for x in range(n)]
for i in range(0,m):
  inp = list(map(float,input().split()))
  adjList[int(inp[0])].append((int(inp[1]),inp[2]))
  adjList[int(inp[1])].append((int(inp[0]),inp[2]))

def djikstras(graph, start, end):
  queue = []
  distance = [0 for x in range(n)]
  distance[start] = 1
  heapq.heappush(queue, (-1, start))
    
  # continue while there are items in the queue
  while len(queue):
    distanceToU, u = heapq.heappop(queue)
    distanceToU = -distanceToU
        
    # stop if end is reached
    if(u == end):
      break

    # ignore nodes with distance greater than the current node    
    if(distance[u] > distanceToU):
      continue

    # search through neighbors and calculate distances
    for v, weight in graph[u]:

      # find the distance to the neighboring node
      dist = weight * distance[u]

      # if closer than the current distance, update the distance by adding it to the heap
      if distance[v] < distance[u] * weight:
        distance[v] = dist
        heapq.heappush(queue, (-distance[v], v))

  return distance[end]


print(djikstras(adjList, 0, n-1))