import math
import cProfile

def getProduct(r):
    n = len(r)
    if n==0:
        return 0
    elif n==1:
        return r[0]
    p = 0
    for x1 in r:
        p += x1*x1*((n-1)*n/2-2)
        for x2 in r:
            p += 2*x1*x2
    return p

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
    if k==1:
        yield getProduct(r)
        return
    indices = [None]*(k-1)
    combos = [None]*(k-1)
    combos[0] = getCombinations(r, 2)
    indices[0] = next(combos[0], None)
    for i in range(1, k-1):
        combos[i] = getCombinations(indices[i-1], 2)
        indices[i] = next(combos[i], None)
    while True:
        for i in reversed(range(k-1)):
            if indices[i] != None:
                break
        else:
            return
        yield getProduct(indices[i-1])
        indices[i] = next(combos[i], None)
        if indices[i] == None:
            for j in reversed(range(i)):
                indices[j] = next(combos[j], None)
                if indices[j] != None:
                    for x in range(j+1, k-1):
                        combos[x] = getCombinations(indices[x-1], 2)
                        indices[x] = next(combos[x], None)
                    break

def numCombos(r, k):
    length = 0
    for i in combinationParentG(r, k):
        length += 1
    return length

def main(k, n, r):
    r.sort()
    area = 0
    length = 0
    for i in combinationParentG(r, k):
        area += i
        length += 1
    return (area*math.pi)/length

if __name__ == "__main__":
    k = 2
    n = 100
    r = [x+1 for x in range(n)]
    cProfile.run("main(k,n,r)")
#     a = main(k, n, r)
#     print(a)
