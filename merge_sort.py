def MergeSort(list):
    if(len(list) > 1):
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]

        MergeSort(left)
        MergeSort(right)

        a = 0
        b = 0
        c = 0
        print("*********************")
        print(list)
        print("left")
        print(left)
        print("right")
        print(right)
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list[c] = left[a]
                a = a + 1
            else:
                list[c] = right[b]
                b = b + 1
            c = c + 1
        while a < len(left):
            list[c]= left[a]
            a = a + 1
            c = c + 1

        while b < len(right):
            list[c] = right[b]
            b = b + 1
            c = c + 1
        print(list)
        print("*********************")
    return list

list = [44,16,83,7,67,21,34,45,10]
print(list)
MergeSort(list)
print(list)