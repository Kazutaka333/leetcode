s = '11110111001101010000000110100100'
maxlen = 0
for i in range(32):
    flipped = s[:i]+"1"+s[i+1:] 
    print(flipped)
    length = 0
    for c in flipped:
        if c == "1":
            length += 1
        else:
            length = 0
        if length > maxlen:
            maxlen = length
print(maxlen)
