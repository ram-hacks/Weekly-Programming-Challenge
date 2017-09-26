# In computability theory, a system of data-manipulation rules is said to be Turing complete if it can be used to simulate any Python one-liner.
print '\n'.join((i%3==0)*'RAM'+(i%5==0)*'Hacks' or str(i) for i in range(1,51))
