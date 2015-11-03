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

       

def main():
    print(palindrome_golf('a'))
    print(palindrome_golf('abc'))
    print(palindrome_golf('abcba'))
    print('---')
    print(palindrome_itertive('a'))
    print(palindrome_itertive('abc'))
    print(palindrome_itertive('abcba'))
    print(palindrome_itertive('racecar'))

if __name__ == '__main__':
    main()
