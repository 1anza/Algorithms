#inputs
nep = list(map(int,input().split()))
n = nep[0]
e = nep[1]
p = nep[2]

houses = []
for i in range(0,n):
    houses.append(tuple(map(float,input().split())))

connected = []
for i in range(0,p):
    connected.append(tuple(map(int,input().split())))

edges = []
for i in range(n):
    for j in range(n):
        edges.append((i, j, ((houses[i][0] - houses[j][0]) ** 2 + (houses[i][1] - houses[j][1]) ** 2)** 0.5))


class FindUnion:
    def __init__(self, n, e):
        self.parent = [x for x in range(n+1)]
        self.size = [0 for x in range(n+1)]
        for i in range(e):
            self.parent[i] = n
        self.size[n] = e

    def find(self, node):
        if self.parent[node] == node:
            return node
        return self.find(self.parent[node])
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return False
     
        if self.size[root1] > self.size[root2]:
            self.parent[root2] = root1
        elif self.size[root1] < self.size[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.size[root1] += 1
                
        return True

union = FindUnion(n,e)

count = 0
for i in range(0,p):
    u, v = connected[i]
    if union.union(u,v):
        count += 1
connect = n - e - count

def kruskals(edges):
    union = FindUnion(n,e)
    edges.sort(key=lambda x: x[2])
    MST = []
    minCost = 0
    numEdge = 0
    for index, tuple in enumerate(edges):
        u, v, w = edges[index]
        if union.union(u, v):
            minCost += w
            numEdge += 1
            MST.append((u, v))
            if numEdge == connect:
                print(minCost)
            

kruskals(edges)
