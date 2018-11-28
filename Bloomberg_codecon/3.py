data = ["2 3 3","D C B","C A C"]

r, c, k = map( lambda a:int(a),data[0].split())
table = []
for i in range(r):
    table.append(data[i+1].split())
x, y = 0, 0
ans = ""
curr = table[y][x]
ans += curr
for i in range(k):
    cand = [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]
    best = "~"
    b_x, b_y = 0, 0
    for n_x, n_y in cand:
        if -1 < n_x and n_x < c and -1 < n_y and n_y < r:
            new = table[n_y][n_x]
            if curr != new and new < best :
                best = new
                b_x, b_y = n_x, n_y
    curr = best
    x, y = b_x, b_y
    ans += curr

print(ans)
    
