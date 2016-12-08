def find_missing(l):
    return int(((len(l) + 1) * (len(l) + 2)) / 2) - sum(l)


if __name__ == '__main__':
    assert find_missing([7, 8 ,10 ,3 ,6 ,5 ,1 ,2 ,9]) == 4
    assert find_missing([1, 3]) == 2
