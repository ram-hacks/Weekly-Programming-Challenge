⍝ http://ngn.github.io/apl/web/ to run
⍝ http://tryapl.org/ for reference
⍝ ⍵ is the first argument in a function (I think)
⍝ ⍝ starts a comment

⍝ This is a direct translation of my clojure implementation
sqrt ← { ⍵ * .5 }
φ ← (1 + sqrt 5) ÷ 2
ψ ← (1 - sqrt 5) ÷ 2
fib ← { ⌈ (((φ * ⍵) - (ψ * ⍵)) ÷ (sqrt 5)) }
fIndex ← { 1 + ⌈ ((⍟ ⍵) ÷ (⍟ φ)) }
isFib ← { ⍵ = (fib ∘ fIndex ⍵) }

isFib 54 ⍝ => 0
isFib 55 ⍝ => 1
isFib 102334155 ⍝ => 1
isFib 102334156 ⍝ => 0

⍝ This version build a list of fibonacci numbers then checks if the argument is
⍝ in the list
aFib ← { ⍵ ∊ { a ← ⍵⍴0 ⋄ { ⍵ ≤ 1: a[⍵]←1 ⋄ a[⍵] ← a[⍵ - 1] + a[⍵ - 2] }¨ (⍳⍵) ⋄ a } (fIndex ⍵) }

aFib 54 ⍝ => 0
aFib 55 ⍝ => 1
aFib 102334155 ⍝ => 1
aFib 102334156 ⍝ => 0

⍝ Checks if 1, 2, ... 100, are fibonacci numbers
⍝ isFib¨ (1 + (⍳ 100))
⍝ aFib¨ (1 + (⍳ 100))
