def InsertionSort(list):
    for i in range(1, len(list)):
        j = i-1
        print("Iteration")
        print(i)
        element_next = list[i]
        while(list[j] > element_next) and (j >= 0):
            list[j+1] = list[j]
            j=j-1
        list[j + 1] = element_next
        print(j+1)
        print("End")
    return list

list = [25,26,22,24,27,23,21]
print(list)
print(InsertionSort(list))