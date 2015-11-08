⍝ http://ngn.github.io/apl/web/ to run
⍝ http://tryapl.org/ for reference
⍝ { } are used for functions
⍝ ⍵ is the first argument in a function (I think)
⍝ ← is for assignment
⍝ ⍝ starts a comment
⍝ * is for exponentiation
⍝ ⍟ calculates the natural logarithm
⍝ ⍳ is like the range operator in python, ⍳ 100 gives 0 1 ... 99
⍝ ¨ applies the function to every element of the list (like map in ml)
⍝ ∘ is for function composition
⍝ ⌈ is the ceiling function
⍝ ⍴ is size/reshape operator

⍝ This is a direct translation of my clojure implementation
sqrt ← { ⍵ * .5 }
φ ← (1 + sqrt 5) ÷ 2
ψ ← (1 - sqrt 5) ÷ 2
fib ← { ⌈ ((((φ * ⍵) - (ψ * ⍵)) ÷ (sqrt 5)) - 0.5) }
fIndex ← { 1 + ⌈ (φ ⍟ ⍵) }
isFib ← { ⍵ = (fib ∘ fIndex ⍵) }

isFib 54 ⍝ => 0
isFib 55 ⍝ => 1
isFib 102334155 ⍝ => 1
isFib 102334156 ⍝ => 0

⍝ A more concise implementation of the above
r←5*.5
p←.5×(1 ¯1)+r ⍝ Phi and Phi bar
aFib←{⍵={⌈-/(p∘*⍵+1)÷r}⌈1↑p⍟⍵}

aFib 54 ⍝ => 0
aFib 55 ⍝ => 1
aFib 102334155 ⍝ => 1
aFib 102334156 ⍝ => 0

⍝ Checks the first N numbers for fibonacci numbers
N ← 300
Numbers ← 1 ↓ ⍳ (N + 1)
3 N ⍴ Numbers, (isFib¨ Numbers), (aFib¨ Numbers)
