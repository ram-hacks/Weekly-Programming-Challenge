def palindrome_golf(a):
    return a[::-1] == a

def palindrome_itertive(a):
    """ Start at the start and the end, count inwards """
    # TODO make this less crappy
    if len(a) <= 1:
        return True
    else:
        start = 0 
        end = len(a) - 1
        while start != end:
            # print(end)
            # print('start: ', start, ' a: ', a[start])
            # print('end: ', end, ' a: ', a[end])
            if not a[start] == a[end]:
                return False
            else:
                start += 1
                end -= 1
        return True

def palindrome_recursive(a):
    """ OH GOD HERE WE GO AGAIN AND AGAIN AND AGAIN AND AGAIN """
    # Base case
    if len(a) <= 1:
        return True
    else:
        if a[0] == a[len(a)-1]:
            return palindrome_recursive(a[1:-1])
        else:
            return False

def longest_palindrome(a):
    """ 
    Returns the longest contiguous palindrome in a given string. 
    Iteratively go through the string and pass all substrings through
    function to check if they're palindromes. Store the longest. Then
    increase starting character and do it again.

    THIS IS BAD. If the whole string is a palindrome, I take _as long as possible_
    to figure that out. Start big, work smaller.
    """
    # This is some spaghetti if I've ever seen some. In the case where the whole work is
    # a palindrome, we can go ahead and skip. BUT ONLY IN THAT INSTANCE BECAUSE IT'S BAD
    if palindrome_golf(a):
        return a

    # Enter the bad
    max_so_far = ''
    for length in range(1,len(a)-1):
        start = 0
        while start <= len(a) - 1:
            sub = a[start:start+length]
            cur = palindrome_golf(sub)
            if cur is True and len(sub) > len(max_so_far):
                max_so_far = sub
            start += 1

    return max_so_far



       

def main():
    print(palindrome_golf('a'))
    print(palindrome_golf('abc'))
    print(palindrome_golf('abcba'))
    print(palindrome_golf('racecar'))
    print('---')
    print(palindrome_itertive('a'))
    print(palindrome_itertive('abc'))
    print(palindrome_itertive('abcba'))
    print(palindrome_itertive('racecar'))
    print('---')
    print(palindrome_recursive('a'))
    print(palindrome_recursive('abc'))
    print(palindrome_recursive('abcba'))
    print(palindrome_recursive('racecar'))
    print('---')
    print(longest_palindrome('a'))
    print(longest_palindrome('abc'))
    print(longest_palindrome('abcba'))
    print(longest_palindrome('racecar'))
    print(longest_palindrome('abcdddabc'))
    print(longest_palindrome('abcddddabc'))


if __name__ == '__main__':
    main()
