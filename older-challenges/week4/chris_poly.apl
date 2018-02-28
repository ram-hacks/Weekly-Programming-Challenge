poly←{+/⍵×⍺*¯1+⍳⍴⍵}

⍝ APL evaluates from right to left, and most operations are element-wise
⍝ i.e. 1 1 1 5 5 5 + 1 2 3 4 5 6 
⍝      = 1+1 1+2 1+3 5+4 5+5 5+6 
⍝      = 2 3 4 9 10 11

⍝ This funky A-lookin thing denotes a comment

⍝   ←   : Assignmnet
⍝   {}  : Function
⍝   ⍺   : Left argument to a function
⍝   ⍵   : Right argument to a function
⍝   ⍴   : Gives the shape (the size of a vector/matrix)
⍝   ⍳n  : Gives a vector of the first n cardinal numbers, i.e. ⍳5 => 1 2 3 4 5
⍝   *   : Exponent
⍝   ×   : Multiplication
⍝   +/  : Summation
⍝   ¯   : Negation. Not to be confused with -. Negative five is ¯5, NOT -5

⍝ Example: 2 poly 4 2 7 6 5
⍝   ⍺ = 2, ⍵ = 4 2 7 6 5
⍝     +/⍵ × ⍺ * ¯1 + ⍳⍴⍵
⍝     +/⍵ × ⍺ * ¯1 + ⍳        5
⍝     +/⍵ × ⍺ *               0 1 2 3 4
⍝     +/⍵ ×                   1 2 4 8 16
⍝     +/                      4 4 28 48 80
⍝                             264
