def subsearch(m, n):
    q = len(m)
    w = len(n)
    j = 0
    for i in range(q-w):
        print(n, m[i:w+i])
        if n == m[i:w+i]:
            return True

s = "cat"
d = "fatfatfatcatfat"
print(subsearch(d,s))
print ("cat" == "cat")
