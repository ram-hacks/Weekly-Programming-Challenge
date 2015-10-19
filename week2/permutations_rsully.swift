func stringToCharacterCounts(str: String) -> [Character: UInt] {
    var characterCounts = [Character: UInt]()

    for char in str.characters {
        if let c = characterCounts[char] {
            characterCounts[char] = c + 1
        } else {
            characterCounts[char] = 0
        }
    }

    return characterCounts
}

func isPermutation(str1: String, ofString str2: String) -> Bool {
    if str1.characters.count != str2.characters.count {
        return false
    }
    return stringToCharacterCounts(str1) == stringToCharacterCounts(str2)
}

print(isPermutation("abc", ofString: "acb") == true)
print(isPermutation("abc", ofString: "acba") == false)
print(isPermutation("abc", ofString: "ac") == false)

print(isPermutation("123", ofString: "321") == true)
print(isPermutation("111", ofString: "123") == false)

print(isPermutation("", ofString: "") == true)
print(isPermutation(" ", ofString: " ") == true)
print(isPermutation("", ofString: "abc") == false)
print(isPermutation("abc", ofString: "") == false)

print(isPermutation("ABC", ofString: "abc") == false)
