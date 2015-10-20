__author__ = 'Daniel Dides'

"""
Test whether one string is a permutation of another.
Done the "simple and elegant" way (sorted)
and the "more efficient" way (dictionary)
"""

def permutation_sort(a: str, b: str) -> bool:
    return sorted(a) == sorted(b)


def permutation_dict(a: str, b: str) -> bool:
    if len(a) is not len(b):
        return False
    else:
        hash_table_a = {}
        hash_table_b = {}
        for letter in a:
            if letter in hash_table_a:
                hash_table_a[letter] += 1
            else:
                hash_table_a[letter] = 1
        for letter in b:
            if letter in hash_table_b:
                hash_table_b[letter] += 1
            else:
                hash_table_b[letter] = 1
    return hash_table_a == hash_table_b


def main():
    print('1: ', permutation_sort('abc', 'cba'))
    print('2: ', permutation_sort('xyz', 'zyx'))
    print('3: ', permutation_sort('not a permutation', 'abc'))
    print('---')
    print('1: ', permutation_dict('abc', 'cba'))
    print('2: ', permutation_dict('xyz', 'zyx'))
    print('3: ', permutation_dict('not a permutation', 'abc'))


if __name__ == '__main__':
    main()
