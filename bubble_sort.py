def BubbleSort(list):
    lastElementIndex = len(list) - 1
    for passNo in range(lastElementIndex,0,-1):
        print(range(passNo))
        for idx in range(passNo):
            if list[idx] > list[idx+1]:
                list[idx], list[idx+1] = list[idx+1], list[idx]
    return list

print(BubbleSort([25,21,22,24,23,27,26]))