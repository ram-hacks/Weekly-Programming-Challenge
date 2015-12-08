num_lines = sum(1 for line in open(input('Please give me a file to sort (file path and name): \n >')))
for i in range (0, num_lines):
    numbers[i]=file.readline()
file.close()
newOrder=[]
for i in range(0, len(numbers)):
    newOrder.append(max(numbers))
    numbers.remove(max(numbers))

for i in range(0, len(newOrder)):
    print(str(newOrder[i])+", ", end="")
