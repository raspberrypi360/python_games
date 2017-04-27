def sortable(a):
    if len(a) == 1 or len(a) == 2:
        return True
    if a[:2] == [0, 1]:
        f1 = True
        f2 = True
    elif a[:2] == [1,0]:
        f1 = False
        f2 = True
    elif a[0] == 0 and a[1] != 1:
        f1 = True
        f2 = False
    else:
        f1 = True
        f2 = False
    for i in range(2, len(a)):
        if f1 == False and f2 == False:
            return False
        if f2 == True:
            if a[i] == i:
                f1 = True
                f2 = True
            else:
                f1 = True
                f2 = False
        else:
            if a[i] != i:
                if a[i-1] == i:
                    if a[i] == i-1:
                        f1 = False
                        f2 = True
                    else:
                        f1 = False
                        F2 = False
                else:
                    f1 = False
                    F2 = False
            else:
                f1 = False
                f2 = False
    if f2 == False:
        return False
    return True



if __name__ == "__main__":
    s = sortable([1, 0, 3, 2], 4)
    print(s)