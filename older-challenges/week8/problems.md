Weekly Programming Challenge
============================
March 8, 2016
-------------
### [Making a Coin Fair](codegolf.stackexchange.com)
You are given a string of data consisting of 1s and 0s.
These numbers represent coin flips performed one after the other.
You are told that while a coin flip should produce a 50/50 split,
this coin was flipped unfairly. So while a 1 or 0 might be more or less likely
than the other, 01 and 10 will be equally likely.

Your job is to take the string of data that you are given and check each pair
of numbers for either combination, where 01 = 0 and 10 = 1.
You will then output the new string of data.

To clarify, the string should be imagined to be in blocks of 2 like the
example below.

`0 0, 1 1, 0 0, 1 1, 1 1, 0 1, 0 0`
### Test Cases
`Input --> Output`
`'1110' --> '1'`
`'11000110' --> '01'`
`'1100011' --> '0'`
`'00' --> '' `    
`'1' --> '' `
`'' --> '' `
`'1101001' --> '0' `
``'1011101010' --> '1111'`

### Challenge (code golf)
Try to complete this in as few lines as possible.
