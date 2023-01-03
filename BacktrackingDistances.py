# receive input from console
n = int(input())
distances = list(map(int, input().split())) 
arr = [0 for x in range(n+1)]
for i in range(1, n+1):
   arr[i] = distances[i-1]

# initialize 2D arrays
iterate = [[0 for x in range(1000+10)] for y in range(n+10)]
finish = [[0 for x in range(1000+10)] for y in range(n+10)]

# locate when end of array is reached
end = 1000000
for i in range(0, n+1):
    for j in range(0, 1001):
        iterate[i][j] = end

# tackle subproblems and iteratively work to the front
iterate[0][0] = 0;
for i in range(1, n+1):
    for j in range(0, 1001):

        if (j - arr[i] >= 0) and (iterate[i-1][j - arr[i]] != end):
            if iterate[i][j] > max(iterate[i-1][j - arr[i]], j):
                iterate[i][j] = max(iterate[i-1][j - arr[i]], j)
                finish[i][j] = j - arr[i]

        if (j + arr[i] <= 1000) and (iterate[i-1][j + arr[i]] != end):
            if iterate[i][j] > max(iterate[i-1][j + arr[i]], j):
                iterate[i][j] = max(iterate[i-1][j + arr[i]], j)
                finish[i][j] = j + arr[i]

# store heights
heights = [0 for x in range(n+2)]
z = 0
def minWall(n, h):
    global z
    global arr

    heights[z] = h
    z += 1

    if n == 0:
        return

    minWall(n-1, finish[n][h])

# if array reaches end print infinity, otherwise find optimal height
infinity = 100000
if iterate[n][0] == end:
    print(infinity)
else:
    minWall(n,0)

# print optimal height
for i in range(1, z):
    if heights[0] < heights[i]:
        heights[0] = heights[i]
print(heights[0])
