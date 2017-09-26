#Phidias Mendez
#Date: 9/25/2017
#Description: FizzBuzz Challenge. Any number divisible
#             by 3 will print "RAM". Any number divisible by 5 will
#             print "Hacks". Any number divisible by both will print
#             "RAMHacks".

for index in range(1,51):
    output = ''
    if(index % 3 == 0):
        output += "RAM"
    if(index % 5 == 0):
        output += "Hacks"
    if(index % 3 != 0 and index % 5 != 0):
        output += str(index)
    print(output)
