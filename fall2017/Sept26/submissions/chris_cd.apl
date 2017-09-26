#! /usr/local/bin/apl --script 
⍝ TO RUN: 
⍝   > paste -s -d ' ' input.txt | ./chris_cd.apl

∇ common x ; a ; b
  →(2≥⍴x)/0            ⍝ Exit when we hit 0 0
  a ← (↑x)↑2↓x         ⍝ Jack's CDs
  b ← (↑1↓x)↑(2+⍴a)↓x  ⍝ Jill's CDs
  +/a∊b                ⍝ Add up shared, output
  common (2+⍴a,b)↓x    ⍝ Recurse
∇

common ⎕

)OFF
