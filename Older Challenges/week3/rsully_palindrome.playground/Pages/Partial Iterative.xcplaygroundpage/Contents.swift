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

func findPalindrome_old(str: String) -> String? {
    var longest: String? = nil

    for li in 0...str.characters.count {
        let left = str.startIndex.advancedBy(li)

        for ri in li...str.characters.count {
            let right = str.startIndex.advancedBy(ri)
            let currentRange = Range(start: left, end: right)

            if currentRange.count <= longest?.characters.count {
                // too short
                continue;
            }

            let currentStr = str[currentRange]
//            print("\(currentStr)")
            if isPalindrome(currentStr) {
                longest = currentStr
            }
        }
    }
    return longest
}

func findPalindrome(str: String) -> String? {
    for length in (0...str.characters.count).reverse() {
        let offsetMax = str.characters.count - length

        for offset in 0...offsetMax {
            let leftIndex = str.startIndex.advancedBy(offset)
            let rightIndex = str.startIndex.advancedBy(offset + length)
            let currentRange = Range(start: leftIndex, end: rightIndex)

            let currentStr = str[currentRange]
//            print("\(currentStr)")
            if isPalindrome(currentStr) {
                return currentStr
            }
        }
    }
    return nil
}


findPalindrome("1aba2")     == "aba"
findPalindrome("ababa123")  == "ababa"
findPalindrome("123aba")    == "aba"
findPalindrome("123ababa")  == "ababa"
findPalindrome("123aba")    == "aba"
findPalindrome("1aba")      == "aba"
findPalindrome("aba1")      == "aba"
findPalindrome("")          == ""
findPalindrome("a")         == "a"

findPalindrome_old("1aba2")     == "aba"
findPalindrome_old("ababa123")  == "ababa"
findPalindrome_old("123aba")    == "aba"
findPalindrome_old("123ababa")  == "ababa"
findPalindrome_old("123aba")    == "aba"
findPalindrome_old("1aba")      == "aba"
findPalindrome_old("aba1")      == "aba"
findPalindrome_old("")          == ""
findPalindrome_old("a")         == "a"
