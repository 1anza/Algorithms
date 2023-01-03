# creating an empty list
anagramList = []
  
# number of elements as input
n, k = map(str,input().split())

# iterate through n
for i in range(0, int(n)):
    word = str(input())
    anagramList.append(word)

# sort list
sortedAnagramList = [''.join(sorted(w)) for w in anagramList]      

# collect frequency of unique words
frequency = {}
total = 0
for w in sortedAnagramList:
    if w in frequency:
        frequency[w] = frequency[w] + 1
    else:
        frequency[w] = 1

# count anagrams
for n in frequency.values():
    if n == 1:
        total += 1

print(total)