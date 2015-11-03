func isPalindrome(💬: String) -> Bool {
    let 👈 = 💬.startIndex
    var 👉 = 💬.endIndex

    if (👈 == 👉) {
        // Handle empty strings
        return true
    }
    👉 = 👉.predecessor()
    if (👈 == 👉) {
        // Handle 1 char strings
        return true;
    }

    if 💬.characters[👈] != 💬.characters[👉] {
        return false
    }

    return isPalindrome(💬[Range(start: 👈.successor(), end: 👉)])
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

isPalindrome("💬") == true
isPalindrome("💬💬") == true
isPalindrome("💬a💬") == true
isPalindrome("👈👉") == false
