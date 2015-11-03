protocol Reversible {
    var reversed: Self { get }
}

extension String: Reversible {
    var reversed: String {
        return String(characters.reverse())
    }
}


func isPalindrome(str: String) -> Bool {
    return str == str.reversed
}


isPalindrome("") == true
isPalindrome("a") == true
isPalindrome("aa") == true
isPalindrome("aba") == true
isPalindrome("abba") == true
isPalindrome("abcba") == true

isPalindrome("ab") == false
isPalindrome("abc") == false
isPalindrome("abcd") == false

isPalindrome("omgmo") == true
isPalindrome("omgomgomg") == false
isPalindrome("1111") == true

isPalindrome("bla") == false
