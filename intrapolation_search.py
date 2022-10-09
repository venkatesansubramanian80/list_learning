def IntPolsearch(list, x):
    idx0 = 0
    idxn = (len(list) - 1)
    found = False
    while idx0 <= idxn and x >= list[idx0] and x <= list[idxn]:
        mid = idx0 + int((
                (float(idxn - idx0)
                 /
                 (list[idxn] - list[idx0]))
                *
                (x - list[idx0])
        ))
        if list[mid] == x:
            found = True
            return found
        if list[mid] < x:
            idx0 = mid + 1
    return found

list = [11, 12, 22, 33, 55, 90, 99]
print(IntPolsearch(list, 12))
print(IntPolsearch(list, 91))