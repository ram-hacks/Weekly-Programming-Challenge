def permutation(a: str, b: str) -> bool:
    return sorted(a) == sorted(b)


def main():
    print('1: ', permutation('abc', 'cba'))
    print('2: ', permutation('xyz', 'zyx'))
    print('3: ', permutation('not a permutation', 'abc'))


if __name__ == '__main__':
    main()
