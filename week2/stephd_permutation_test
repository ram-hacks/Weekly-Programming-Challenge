a= str(input('Gimme a string!')).lower()
b= str(input('Gimme another string (of the same length)!')).lower()
i=0
h=0
if(len(a) == len(b)):
    print('Yay, they\'re the same length.')
    for i in range(0, len(a)):
        if(a[i] in b):
            print ('Found ' +a[i]+ ' in '+b)
            h+=1
        else:
            print ('Could not find ' +a[i]+ ' in ' + b)
    if(h >= len(a)):
        print(a + ' is a permutation of '+b+'!')
    else:
        print(a + ' is not a permutation of '+b+'!')
else:
    print('Those 2 aren\'t the same length.')
