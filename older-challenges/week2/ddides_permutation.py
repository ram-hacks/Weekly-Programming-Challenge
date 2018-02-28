"""
Test whether one string is a permutation of another.
Done the "simple and elegant" way (sorted)
and the "more efficient" way (dictionary)
"""
__author__ = 'Daniel Dides'


import time


class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose
    
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000
        if self.verbose:
            print('Elapsed time: ', self.msecs)

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
    # Small stuff
    print('1: ', permutation_sort('abc', 'cba'))
    print('2: ', permutation_sort('xyz', 'zyx'))
    print('3: ', permutation_sort('not a permutation', 'abc'))
    print('---')
    print('1: ', permutation_dict('abc', 'cba'))
    print('2: ', permutation_dict('xyz', 'zyx'))
    print('3: ', permutation_dict('not a permutation', 'abc'))

    # Much larger stuff
    f = open('random_data_a.txt', 'rb')
    big_data_a = f.readlines()
    f.close()
    f = open('random_data_b.txt', 'rb')
    big_data_b = f.readlines()
    f.close()
    with Timer() as t:
        print ('Sort start.')
        permutation_sort(big_data_a, big_data_b)
    print('Sort finished in %d milliseconds' % t.msecs)
    with Timer() as t:
        print ('Dict start.')
        permutation_dict(big_data_a, big_data_b)
    print('Dict finished in %d milliseconds' % t.msecs)
    

if __name__ == '__main__':
    main()
