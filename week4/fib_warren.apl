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

⍝ This is a direct translation of my clojure implementation
sqrt ← { ⍵ * .5 }
φ ← (1 + sqrt 5) ÷ 2
ψ ← (1 - sqrt 5) ÷ 2
fib ← { ⌈ ((((φ * ⍵) - (ψ * ⍵)) ÷ (sqrt 5)) - 0.5) }
fIndex ← { 1 + ⌈ ((⍟ ⍵) ÷ (⍟ φ)) }
isFib ← { ⍵ = (fib ∘ fIndex ⍵) }

isFib 54 ⍝ => 0
isFib 55 ⍝ => 1
isFib 102334155 ⍝ => 1
isFib 102334156 ⍝ => 0

⍝ This version build a list of fibonacci numbers then checks if the argument is in the list
⍝ It doesnt work as well as the other version for large numbers
aFib ← { ⍵ ∊ { a ← ⍵⍴0 ⋄ { ⍵ ≤ 1: a[⍵]←1 ⋄ a[⍵] ← a[⍵ - 1] + a[⍵ - 2] }¨ (⍳⍵) ⋄ a } (fIndex ⍵) }

aFib 54 ⍝ => 0
aFib 55 ⍝ => 1
aFib 102334155 ⍝ => 1
aFib 102334156 ⍝ => 0

⍝ Checks if 1, 2, ... 100, are fibonacci numbers
⍝ isFib¨ (1 + (⍳ 100))
⍝ aFib¨ (1 + (⍳ 100))

⍝ Checks the first N numbers for fibonacci numbers
N ← 300
Numbers ← (1 + (⍳ N))
2 N ⍴ Numbers, (isFib¨ Numbers)
