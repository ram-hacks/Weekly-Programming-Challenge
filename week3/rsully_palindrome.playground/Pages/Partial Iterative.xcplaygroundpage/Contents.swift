/**
 * Copied from Iterative solution
 */
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

func findPalindrome(str: String) -> String? {
    var longest: String? = nil

    for li in 0...str.characters.count {
        let left = str.characters.startIndex.advancedBy(li)

        for ri in li...str.characters.count {
            let right = str.characters.startIndex.advancedBy(ri)
            let currentRange = Range(start: left, end: right)

            if currentRange.count <= longest?.characters.count {
                // too short
                continue;
            }

            let currentStr = str[Range(start: left, end: right)]
            if isPalindrome(currentStr) {
                longest = currentStr
            }
        }
    }
    return longest
}

findPalindrome("1aba2")     == "aba"
findPalindrome("ababa123")  == "ababa"
findPalindrome("123aba")    == "aba"
findPalindrome("123ababa")  == "ababa"
findPalindrome("123aba")    == "aba"
