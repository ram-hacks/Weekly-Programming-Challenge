i=0
pal = str(input('Pick a string, any string!'))
def palTest(word):
    reverse = word[::-1]
    if word== reverse:
        return True
    else:
        return False
print('easy mode: '+str(palTest(pal)))


def palTestI(word):
    reverse=''
    preverse=''
    for i in range (1, 1 + len(word)):
        reverse = preverse+ word[-i] 
        preverse= reverse
    print('iterative reverse: '+reverse)
    if word== reverse:
        return True
    else:
        return False
print('iterative: '+str(palTestI(pal)))


"""#tried recursive, meh.
def palTestR(word):
    i=1
    reverse=''
    if i ==len(word):
        return 1
    else:
        reverse=reverse+word[-i]
        i+=1
    print(reverse)
palTestR(pal)"""


def palTestP(word): #will figure this one out eventually...
    n=0
    for i in range(0, len(word)):
        wordminus= word[i:] #the rest of the word from where the character i is on to the end of the word 
        if(word[i] in wordminus):  #if you find that letter again in the rest of the word
            partPalEnd= wordminus.index(word[i]) #mark that spot as the end of the partial palindrome
            palLength = partPalEnd + 2  #also keep the length of this partial palindrome
            if ((word[i+i]) == (wordminus[partPalEnd-i])):  #if the letter after the 1st match is the same as the letter 1 before the end of the partial palindrome
                n+=1 #add 1 to the score of partial-palindrome-ness
    if palLength== ((n/2) or ((n/2)-1)):  #if partial-palindrome-ness score = length of potential palindrome (really half, cuz they meet in the middle i think?)
        return ('This is the partial palindrome I came up with: '+ word[i-1:palLength]+'.') # the partial palindrome is 
print(palTestP(pal))

"""partial palindromes psuedo-code:
take 1st letter
check for the same letter throughout the rest of the word,
    if found move back from that spot
        check that spot-1 and start+1 to see if they're equal
            if they are, check spot-2 and start+2 and so on.
    else:
        check the 2nd letter in much the same way."""
