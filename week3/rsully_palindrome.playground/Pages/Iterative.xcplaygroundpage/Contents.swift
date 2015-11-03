func isPalindrome(str: String) -> Bool {
    var left = str.startIndex
    var right = str.endIndex

    // Handle empty strings:
    if (left == right) {
        return true
    }
    right = right.predecessor()

    for _ in 0..<str.characters.count {
        if str.characters[left] != str.characters[right] {
            return false
        }

        // Made it to the middle
        if left >= right {
            return true
        }

        left = left.successor()
        right = right.predecessor()
    }
    return false
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

