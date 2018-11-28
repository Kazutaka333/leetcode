data = ["3","6","4","2","1","3","5","1"]
data = "3 6 4 2 1 2 5 1".split()
data = "10 19 1 10 10 10 10 10 10 10 10 10 1 1 1 1 1 1 1 1 1".split()
data = "3 6 4 2 1 3 5 1".split()
booth_n = int(data[0])
group_n = int(data[1])
groups = [0]+[int(data[i+2]) for i in range(group_n)][::-1]
available = [0 for i in range(booth_n)]
counts = [0 for i in range(booth_n)]

assigned = False
curr = groups.pop()
while len(groups) > 0:
    if assigned:
        curr = groups.pop()
    assigned = False
    print(curr)
    for i in range(booth_n):
        if available[i] == 0:
            available[i] += curr
            assigned = True
            if curr != 0:
                counts[i] += 1
            if counts[i]%10 == 0:
                available[i] += 5
            break
    if not assigned:
        available = [max(x-1,0) for x in available]
    print(available)


print(" ".join([str(x) for x in counts]))


