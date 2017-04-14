def shift(s1, s2, negateLast):
    s1[0] = s2[1]
    s1[1] = s2[2]
    if negateLast:
        s1[2] = not s2[2]
    else:
        s1[2] = s2[2]
    
def outcomes(a):
    n = len(a)
    if n < 3:
        return False
    if n == 3:
        return a[2] == 0 and a[0] == 0
    s000 = [False, False, True]
    s001 = [False, False, False]
    s010 = [False, False, True]
    s011 = [False, False, False]
    s100 = [False, False, False]
    s101 = [False, False, False]
    s110 = [False, False, False]
    s111 = [False, False, False]
    winner = False
    for i in range(3, n):
        s000p = s000[:]
        s001p = s001[:]
        s010p = s010[:]
        s011p = s011[:]
        s100p = s100[:]
        s101p = s101[:]
        s110p = s110[:]
        s111p = s111[:]
        if a[i-2] == 0:
            if a[i-1] == 0:
                if a[i] == 0: #000
                    if a[i-3] == 0:
                        shift(s000, s000, True)
                    else:
                        shift(s000, s100, True)
                    if i==n-1:
                        winner = s000[2]
                else: #001
                    if a[i-3] == 0:
                        shift(s001, s000, False)
                    else:
                        shift(s001, s100, False)
                    if i==n-1:
                        winner = s001[2]
            else:
                if a[i] == 0: #010
                    if a[i-3] == 0:
                        if i==3:
                            s010 = [False, False, False]
                        else:
                            if a[i-4] == 0:
                                shift(s010, s000p, False)
                            else:
                                shift(s010, s100p, False)
                    else:
                        if i==3:
                            s010 = [False, False, True]
                        else:
                            if a[i-4] == 0:
                                shift(s010, s010p, False)
                            else:
                                shift(s010, s110p, True)
                    if i==n-1:
                        winner = s010[2]
                else: #011 
                    if a[i-3] == 0:
                        shift(s011, s001, False)
                    else:
                        shift(s011, s101, False)
                    if i==n-1:
                        winner = s011[2]
        else:
            if a[i-1] == 0:
                if a[i] == 0: #100
                    if a[i-3] == 0:
                        shift(s100, s010, True)
                    else:
                        shift(s100, s110, False)
                    if i==n-1:
                        winner = s100[2]
                else: #101
                    if a[i-3] == 0:
                        shift(s101, s010, False)
                    else:
                        shift(s101, s110, False)
                    if i==n-1:
                        winner = s101[2]
            else:
                if a[i] == 0: #110
                    if a[i-3] == 0:
                        shift(s110, s011, False)
                    else:
                        shift(s110, s111, False)
                    if i==n-1:
                        winner = s110[2]
                else: #111 
                    if a[i-3] == 0:
                        shift(s111, s011, False)
                    if i==n-1:
                        winner = s111[2]
    return winner         

if __name__ == "__main__":
    g = 1
    for a0 in range(g):
        n = 5
        sequence = [0, 1, 0, 0, 0]
        winner = outcomes(sequence)
        if winner == True:
            print("Alice")
        else:
            print("Bob")