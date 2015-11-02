package main

import "fmt"

// You can run the code by visiting https://play.golang.org/p/fJGlw-EDX4
// A solution to the longest palindrome problem written in Go, Google's own programming language!

// This could be optimized by not getting substrings and keeping track of indexes instead.

func PartialPalindrome(s string) string {
  // history caches results of calls to Recurse. It avoids performing duplicate computations
  // this technique is called dynamic programming!
	history := make(map[string]bool)
	palindrome := Recurse(s, history)
	fmt.Printf("'%s' --> '%s'\n", s, palindrome)
	return palindrome
}

// result is a named return type
func Recurse(str string, history map[string]bool) (result string) {
	// exists is true if history contains str as a key
	isPalindrome, exists := history[str]
	if exists {
		if isPalindrome {
			result = str
		}
		return
	}

	length := len(str)
	if length < 2 {
		result = str
	} else if str[0] == str[length-1] {
    // then we just need to check if the middle part of the string is a palindrome
		subPalindrome := Recurse(str[1:length-1], history)
		if len(subPalindrome) == length-2 {
			history[str] = true
			result = str
		} else {
			history[str] = false
			result = subPalindrome
		}
	} else {
		left := Recurse(str[0:length-1], history)
		right := Recurse(str[1:length], history)
		if len(left) >= len(right) {
			result = left
		} else {
			result = right
		}
	}
	return
}

func main() {
	PartialPalindrome("aba")
	PartialPalindrome("aaaaaaaaba")
	PartialPalindrome("acbca")
	PartialPalindrome("aba124")
	PartialPalindrome("4010124")
	PartialPalindrome("kayak")
	PartialPalindrome("1234racecar")
	PartialPalindrome("notapalindrome")
	PartialPalindrome("palindrome")
	PartialPalindrome("aaa12321bbb")
	PartialPalindrome("123abcba321")
}
