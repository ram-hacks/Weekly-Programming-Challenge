# Part 1
def palindrome_golf(a):
    return a[::-1] == a

def main():
    print(palindrome_golf('a'))
    print(palindrome_golf('abc'))
    print(palindrome_golf('abcba'))

if __name__ == '__main__':
    main()
