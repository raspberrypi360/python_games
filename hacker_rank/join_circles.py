import math
import itertools

def getArea(r):
    area = 0
    for i in r:
        for x in i:
            if type(x) == int:
                area += math.pi * x**2
            else:
                radius = 0
                stack = [x]
                while len(stack) != 0:
                    y = stack.pop()
                    for z in y:
                        if type(z) == int:
                            radius += z
                        else:
                            stack.append(z)
                area += math.pi * radius**2
    return area/len(r)

def getCombinations(n, r):
    combo = []
    for i in itertools.combinations(n, r):
        n2 = n[:]
        c = list(i)
        for x in c:
            n2.remove(x)
        n2.append(c)
        combo.append(n2)
    return combo

if __name__ == "__main__":
    k = 2
    n = 100
    r = [i for i in range(100)]
    r.sort()
    newR = getCombinations(r, 2)
    for i in range(1, k):
        results = []
        for x in newR:
            s = getCombinations(x, 2)
            for y in s:
                results.append(y)
        newR = results
    area = getArea(newR)
    print(area)
