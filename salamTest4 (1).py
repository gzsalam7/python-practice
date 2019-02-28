def main():
    caesarSubst()

def trimWhiteSpace(s):
    #replaces spaces with no space
    s = s.replace(" ","")
    return s

def wordCount(s):
    #splits string into a list of words and returns the legnth
    return len(s.split())

def avgWordLength(s):
    s = s.split()
    count = []
    avg = 0
    for i in s:
        #adds the lenght of each word from a list into the list, count
        count.append(len(i))
    for i in count:
        #adds every word length to an average count
        avg = avg + i
    #divides the average coount by the length of the list of words to get the true average
    avg = avg/len(count)
    return(round(avg,3))

def caesarSubst():
    key = eval(input("Input an integer from 0 to 25: "))
    s = input("What message do you want to encrypt?: ")
    print("# of Words = ", wordCount(s))
    print("Average length of words = ", avgWordLength(s))
    s = trimWhiteSpace(s)
    d = []
    e = []
    for i in s:
        #adss the unicode character shifted by the key to empty list d
        d.append(ord(i)+ key)
    #statement checks if unicode values go over the letter values and returns them back to alphabet levels if they do
    for i in d:
        #checks if shifted value goes over z
        if i > 122:
            i = i - 26
        #checks if shifted value goes over Z but is under a
        elif 90 < i < 97:
            i = i - 26
        e.append(chr(i))
    print("".join(e))
#Couldnt do word file
main()


        

            
