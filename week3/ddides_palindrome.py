# Part 1
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


if __name__ == '__main__':
    main()
