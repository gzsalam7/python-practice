def main():
    caesarSubst()

def trimWhiteSpace(s):
    s = s.replace(" ","")
    return s


def caesarSubst():
    key = eval(input("Input an integer from 0 to 25: "))
    s = trimWhiteSpace(input("What message do you want to encrypt?: "))
    d = []
    e = []
    letters  = ("abcdefghijklmnopqrstuvwxyz")
    for i in s:
        d.append(ord(i)+ key)
    for i in d:
        i =i + (i - 97)//26
        e.append(chr(i))
    print("".join(e))

main()
        

            
