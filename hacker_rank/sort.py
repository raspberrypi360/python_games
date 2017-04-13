def sortable(a, n, startIndex):
    if n < 1 or startIndex>=len(a)-1:
        return True
    if a[startIndex] == startIndex:
        return sortable(a, n-1, startIndex+1)
    if a[startIndex+1] == startIndex:
        if a[startIndex] == startIndex+1:
            return sortable(a, n-2, startIndex+2)
        else:
            return False
    return False

q = 1
for a0 in range(q):
    n = 5
    a = [0, 3, 2, 1, 4]
    sort = sortable(a, n, 0)
    if sort == True:
        print("Yes")
    else:
        print("No")