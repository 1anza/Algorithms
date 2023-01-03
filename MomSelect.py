# number of elements as input
n = input()

# input n elements of IDs
IDs = list(map(int, input().split()))  

# input n elements of skills
skills = list(map(int, input().split()))

# total skill value
sumSkill = sum(skills)

# fairness
fair = sumSkill // 2

# finds median of medians
def MoM(IDs, mid):

    # Split list into blocks of 5
    blocks = [IDs[i : i+5] for i in range(0, len(IDs), 5)]

    # sort each block
    sorted_blocks = [sorted(block) for block in blocks]

    # take the median of each block
    medians = [block[len(block) // 2] for block in sorted_blocks]

    # find the median of all medians
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) // 2]
    else:
        pivot = MoM(len(medians) // 2)

    leftSide = 0
    rightSide = len(IDs) - 1
    i = 0

    # partition the list around the pivot
    while i <= rightSide:
        if IDs[i] == pivot:
            i += 1
        elif IDs[i] < pivot:
            IDs[leftSide], IDs[i] = IDs[i], IDs[leftSide]
            leftSide += 1
            i += 1
        else:
            IDs[rightSide], IDs[i] = IDs[i], IDs[rightSide]
            rightSide -= 1

    # return if match is found, otherwise look at left side or right side
    if mid == leftSide:
        return pivot
    if mid < leftSide:
        return MoM(IDs[0:leftSide], mid)
    else:
        return MoM(IDs[leftSide+1:len(IDs)], mid - leftSide)


referee = MoM(IDs, len(IDs) // 2)
print (referee)