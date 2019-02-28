def MSD(l, i):

    if len(l) <= 1:
        return l

    aux = []
    buckets = [ [] for x in range(27) ]
    temp = []

    for s in l:
        if i >= len(s):
            aux.append(s)
        else:
            buckets[ord(s[i]) - ord('a')].append(s)

    for b in buckets:
        temp.append(MSD(b, i+1))

    for blist in temp:
        for b in blist:
            aux.append(b)
    return aux

    #return aux + [b for blist in temp for b in blist]

def main():
	L = ['joe', '', 'bob', 'rot', 'rocket', 'rock', 'z', 'mary', 'suzy', 'sue']
	print (L)
	L = MSD(L, 0)
	print (L)

if __name__ == '__main__':
	main()
