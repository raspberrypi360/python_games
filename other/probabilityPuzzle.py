import random
x = 1
for i in range(196, 225):
    x *= (i/225)
print(1-x)

def duplicate(l):
    dict = {}
    for i in l:
        if i in dict:
            return True
        dict[i] = 1
    return False

def simulation(max, times, people):
    random.seed()
    dup = 0
    for y in range(times):
        nums = [random.randint(1, max) for j in range(people)]
        if duplicate(nums):
            dup += 1
    return dup/times
print(simulation(225, 1000000, 30))