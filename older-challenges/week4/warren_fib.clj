(import 'java.lang.Math)

; Checks if a number is a fibonacci number in clojure
; Clojure is esoteric enough for me

(def PHI (/ (+ 1 (Math/sqrt 5.0)) 2))
(def PHI_BAR (/ (- 1 (Math/sqrt 5.0)) 2))
(defn ** [x n] (Math/pow x n))

; Calculates the n-th fibonacci number in constant time!
; Who said 340 is never useful?
(defn _fib [n] (/ (- (** PHI n) (** PHI_BAR n)) (Math/sqrt 5.0)))
(defn fib [n] (long (_fib (+ n 1))))

(defn log-phi [x] (/ (Math/log x) (Math/log PHI)))
(defn possible-fib-index [x] (int (+ 1 (log-phi x))))
(defn fib? [n] (== n (fib (possible-fib-index n))))

; (fib? n) will work for "smaller" fibonacci numbers. I tested it
; up to the 40th fibonacci number. At some point, the "possible-fib-index" will
; be too small. The function fib? can be extend to work for higher fib numbers
; by also checking a few values of
;     [possible-fib-index, possible-fib-index + 1, possible-fib-index + 2, ...]
; but this works pretty well.

; (fib? 0) // should be true but it'll make an error due to division by 0, oops
(fib? 1)
(fib? 2)
(fib? 3)
(fib? 4)
(fib? 5)
(fib? 6)
(fib? 7)
(fib? 8)
(fib? 9)
(fib? 13)
(fib? 15)

(fib? 52)
(fib? 53)
(fib? 54)
(fib? 55)
(fib? 56)

(fib? 6764)
(fib? 6765)
(fib? 6766)
(fib? 6767)

(fib? 102334155) ; 40th fibonacci number
(fib? 102334156) ; not the 40th fibonacci number
(fib? 102334154)
(fib? 102253155)
(fib? 123456789)
(fib? 923425253)


; checks if a number is a power of 2
(defn pow2? [n] (== 0 (bit-and n (- n 1))))