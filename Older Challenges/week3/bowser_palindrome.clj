; Week 3:
;
; - Implement iterative and recursive functions to test whether an input
;   string is a palindrome.
; - Implement a function to find the longest palindromic substring in a given input string.
;
(require '[clojure.string :as string])

; compare and reverse...
(defn is_palindrome_reverse [s]
   (= s (string/reverse s))
)

; Somewhat more classic lispy solution: recursive
(defn is_palindrome [s]
  (cond
    (<= (count s) 1) true
    (= (first s) (last s)) (is_palindrome (apply str (rest (drop-last s))))
    :else false
  )
)

; Naive recursive solution: find all substrings and select the longest.
(defn longest_palindrome [s]
  (if (<= (count s) 1)
    s
    (reduce #(if (> (count %1) (count %2)) %1 %2)
      (concat
        (filter is_palindrome (for [x (range 1 (+ (count s) 1))] (apply str (take x s))))
        [(longest_palindrome (apply str (rest s)))]
      )
    )
  )
)

; true, false, true, true, false, true
(def teststrs '("abba", "abca", "aba", "abc", "a"))

; print all palindromes
(doall (map println (filter is_palindrome teststrs)))
(doall (map println (filter is_palindrome_reverse teststrs)))

; Print longest palindromic substrings
(doall (map println (map longest_palindrome ["abc", "baab", "caab", "abcdef12321dedfcaac"])))
