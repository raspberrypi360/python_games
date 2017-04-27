import cProfile
import random

def countVotes(l, r, n, v, counter):
    for c in range(n):
        counter[c] = 0
    for i in range(l, r+1):
        counter[v[i]] += 1
    return counter

def countVotes2(l, r, n, v, x):
    v2 = sorted(v[l:r+1])
    count = 1
    id = -1
    for i in range(1, n):
        if v2[i] == v2[i-1]:
            count += 1
        else:
            if count == x:
                id = v2[i-1]
                break
            else:
                count = 0
    if count == x:
        id = v2[i-1]
    return id

def getNominee(counter, x):
    for j in range(len(counter)):
        if counter[j] == x:
            return j
    return -1

def main(t, g, n, v, l, r, x):
    counter = [0]*n
    for i in range(t):
        for j in range(g):
#             votes = countVotes(l, r, n, v, counter)
            nominee = countVotes2(l, r, n, v, x)
#             nominee = getNominee(votes, x)
#             print(nominee)

t = 5
n = 10000
g = n
v = [0]*n
l = 0
r = n-1
x = n
cProfile.run("main(t, g, n, v, l, r, x)")
# main(t, g, n, v, l, r, x)