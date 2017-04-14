def shift(s, negateLast):
    r = s[:]
    r[0] = s[1]
    r[1] = s[2]
    if negateLast:
        r[2] = not s[2]
    return r
    
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
                        s000 = shift(s000, True)
                    else:
                        s000 = shift(s100, True)
                    if i==n-1:
                        winner = s000[2]
                else: #001
                    if a[i-3] == 0:
                        s001 = shift(s000, False)
                    else:
                        s001 = shift(s100, False)
                    if i==n-1:
                        winner = s001[2]
            else:
                if a[i] == 0: #010
                    if a[i-3] == 0:
                        if i==3:
                            s010 = shift(s000, True)
                        else:
                            if a[i-4] == 0:
                                s010 = shift(s000p, False)
                            else:
                                s010 = shift(s100p, False)
                    else:
                        s010 = shift(s100, True)
                    if i==n-1:
                        winner = s010[2]
                else: #011 
                    if a[i-3] == 0:
                        s011 = shift(s001, False)
                    else:
                        s011 = shift(s101, False)
                    if i==n-1:
                        winner = s011[2]
        else:
            if a[i-1] == 0:
                if a[i] == 0: #100
                    if a[i-3] == 0:
                        s100 = shift(s010, True)
                    else:
                        s100 = shift(s110, False)
                    if i==n-1:
                        winner = s100[2]
                else: #101
                    if a[i-3] == 0:
                        s101 = shift(s010, False)
                    else:
                        s101 = shift(s110, False)
                    if i==n-1:
                        winner = s101[2]
            else:
                if a[i] == 0: #110
                    if a[i-3] == 0:
                        s110 = shift(s011, False)
                    else:
                        s110 = shift(s111, False)
                    if i==n-1:
                        winner = s110[2]
                else: #111 
                    if a[i-3] == 0:
                        s111 = shift(s011, False)
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