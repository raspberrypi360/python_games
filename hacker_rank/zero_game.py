def negate(x):
    return not x;

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
    s000p = [False, False, True]
    s001p = [False, False, False]
    s010p = [False, False, True]
    s011p = [False, False, False]
    s100p = [False, False, False]
    s101p = [False, False, False]
    s110p = [False, False, False]
    s111p = [False, False, False]
    winner = False
    for i in range(3, n):
        if a[i-2] == 0:
            if a[i-1] == 0:
                if a[i] == 0: #000
                    s000p = s000[:]
                    if a[i-3] == 0:
                        s000 = list(map(negate, s000))
                    else:
                        s000 = list(map(negate, s100))
                    if i==n-1:
                        winner = s000[2]
                else: #001
                    s001p = s001[:]
                    if a[i-3] == 0:
                        s001 = s000[:]
                    else:
                        s001 = s100[:]
                    if i==n-1:
                        winner = s001[2]
            else:
                if a[i] == 0: #010
                    s010p = s010[:]
                    if a[i-3] == 0:
                        if n==4:
                            return False
                        if a[i-4] == 0:
                            s010 = s000p[:]
                        else:
                            s010 = s100p[:]
                    else:
                        s010 = list(map(negate, s100))
                    if i==n-1:
                        winner = s010[2]
                else: #011 
                    s011p = s011[:]
                    if a[i-3] == 0:
                        s011 = s001[:]
                    else:
                        s011 = s101[:]
                    if i==n-1:
                        winner = s011[2]
        else:
            if a[i-1] == 0:
                if a[i] == 0: #100
                    s100p = s100[:]
                    if a[i-3] == 0:
                        s100 = s010[:]
                    else:
                        s100 = s110[:]
                    if i==n-1:
                        winner = s100[2]
                else: #101
                    s101p = s101[:]
                    if a[i-3] == 0:
                        s101 = s010[:]
                    else:
                        s101 = s110[:]
                    if i==n-1:
                        winner = s101[2]
            else:
                if a[i] == 0: #110
                    s110p = s110[:]
                    if a[i-3] == 0:
                        s110 = s011[:]
                    else:
                        s110 = s111[:]
                    if i==n-1:
                        winner = s110[2]
                else: #111 
                    s111p = s111[:]
                    if a[i-3] == 0:
                        s111 = s011[:]
                    if i==n-1:
                        winner = s111[2]
    return winner         


g = 1
for a0 in range(g):
    n = 5
    sequence = [0, 0, 0, 1, 0]
    winner = outcomes(sequence)
    if winner == True:
        print("Alice")
    else:
        print("Bob")