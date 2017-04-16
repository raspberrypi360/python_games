import math
import cProfile
from _ast import Num

def getArea(r):
    area = 0
    for x in r:
        area += x*x
    return area

def getCombinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    combo = [None]*(n-1)
    combo[0] = sum([pool[i] for i in indices])
    idx = 1
    for p in range(n):
        if p in indices:
            continue
        else:
            combo[idx] = pool[p]
            idx += 1
    yield combo
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        combo = [None]*(n-1)
        combo[0] = sum([pool[i] for i in indices])
        idx = 1
        for p in range(n):
            if p in indices:
                continue
            else:
                combo[idx] = pool[p]
                idx += 1
        yield combo

def combinationParentG(r, k):
    indices = [None]*k
    combos = [None]*k
    combos[0] = getCombinations(r, 2)
    indices[0] = next(combos[0], None)
    for i in range(1, k):
        combos[i] = getCombinations(indices[i-1], 2)
        indices[i] = next(combos[i], None)
    while True:
        for i in reversed(range(k)):
            if indices[i] != None:
                break
        else:
            return
        yield indices[i]
        indices[i] = next(combos[i], None)
        if indices[i] == None:
            for j in reversed(range(i)):
                indices[j] = next(combos[j], None)
                if indices[j] != None:
                    for x in range(j+1, k):
                        combos[x] = getCombinations(indices[x-1], 2)
                        indices[x] = next(combos[x], None)
                    break

def numCombos(r, k):
    length = 0
    for i in combinationParentG(r, k):
        length += 1
    return length

def getSquare(r, k):
    s = 0
    for i in combinationParentG(r, k):
        s += getArea(i)
    return s

def getProduct(r, k):
    n = len(r)
    x2 = 0
    xij = 0;
    for i, s1 in enumerate(r):
        x2 += s1*s1
        for j in range(i+1, n):
            xij += s1*r[j]
    num = n*(n-1)//2
    p2 = num*x2
    pij = 2*xij
    c1 = 1
    nump = 1
    for i in reversed(range(1, k)):
        ni = n-i
        numi = ni*(ni-1)//2
        num *= numi
        p2 *= numi
        nn = ni+1
        numn = nn*(nn-1)//2
        c1 = numi*nump-c1+numn*c1
        pij = 2*xij*c1
        nump *= numi
    s = p2+pij
    return s

def main(k, n, r):
    r.sort()
    s = getProduct(r, k)
    return s*math.pi/num
        
if __name__ == "__main__":
    k = 2
    n = 10
    r = [x+1 for x in range(n)]
    cProfile.run("main(k,n,r)")
#     a = main(k, n, r)
#     print(a)
