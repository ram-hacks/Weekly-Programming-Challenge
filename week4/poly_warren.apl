⍝ Evaluates a polynomial with the most significant power on the left
⍝ APL has a built-in operator for evaluating polynomials! Because, why not?
poly←⊥

⍝ evaluates to 2(3)^3 + 3(3)^2 + 4(3) + 5
3 poly 2 3 4 5

⍝ The ∇ is a reference to the current function (for recursion)
⍝ The ↓ removes elements from the head of the list (returns a new list w/o modifying the original)
⍝   eg 2↓1 2 3 4 5 => 3 4 5
⍝ The ↑ keeps elements from the head of the list
⍝   eg 2↑1 2 3 4 5 => 1 2
⍝ The :⋄ is the ternary conditional operator (?: in C)

⍝ Evaluates a polynomial with the most significant power on the right using Horner's method
horner←{1=⍴⍵:⍵⋄(1↑⍵)+⍺×⍺∇1↓⍵}

⍝ evaluates to 2 + 3(3) + 4(3)^2 + 5(3)^3
3 horner 2 3 4 5
