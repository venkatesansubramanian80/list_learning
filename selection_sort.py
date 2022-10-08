def SelectionSort(list):
    for fill_sort in range(len(list) - 1,0,-1):
        max_index = 0
        for location in range(1,fill_sort + 1):
            if list[location] > list[max_index]:
                max_index = location
        list[fill_sort], list[max_index] = list[max_index], list[fill_sort]
    return list

list = [70,15,25,19,34,44]
list = SelectionSort(list)
print(list)