func isPalindrome(str: String) -> Bool {
    let left = str.startIndex
    var right = str.endIndex

    if (left == right) {
        // Handle empty strings
        return true
    }
    right = right.predecessor()
    if (left == right) {
        // Handle 1 char strings
        return true;
    }

    if str.characters[left] != str.characters[right] {
        return false
    }

    return isPalindrome(str[Range(start: left.successor(), end: right)])
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

