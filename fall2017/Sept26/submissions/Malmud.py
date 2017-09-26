#Evan Malmud
#Date: 9/25/2017
#Description: FizzBuzz Challenge. Any number divisible
#             by 3 will print "RAM". Any number divisible by 5 will
#             print "Hacks". Any number divisible by both will print
#             "RAMHacks".

for i in range(1,51):
  if ((i % 3) == 0) & ((i % 5) == 0):
    print("RAMHacks")
  elif (i % 3) == 0:
    print("RAM")
  elif (i % 5) == 0:
    print("Hacks")
  else:
    print(i)