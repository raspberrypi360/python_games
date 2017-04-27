import itertools

values = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0,0,0,0,0,0,0,"g","g","g","g",1,1,3,5]
winners = 0
combos = 0
for c in itertools.combinations_with_replacement(values, 3):
    combos += 1
    result = 0
    for i in c:
        if i != "g":
            result += i
        else:
            break
    if result > 0 and i != "g":
        winners += 1
print(winners/combos)