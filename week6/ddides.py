import sys
import time
from threading import Timer

def _load_data(infile):
    """ Load the data from the input file """
    try:
        with open(infile, 'r') as infile:
            data = infile.read().splitlines()
    except FileNotFoundError:
        print('File not found. Please pass a real file.')
        sys.exit(1)

    return data


def sleep_sort(data):
    """ Nobody should ever use this. Ever. """
    sorted_data = []

    def _add_to(x):
        sorted_data.append(x)

    def test_add_to():
        _add_to('aaa')

        print(sorted_data)
    test_add_to()
    for datum in data:
        # print('Sorting ', datum)
        curr = data[0]
        if curr < datum:
            curr = datum

        t = Timer(int(datum), _add_to(datum))
        t.start()

    return sorted_data


def main():
    if len(sys.argv) < 2:
        print('Not enough arguments. Usage: $ python ddides.py inputfile')
    else:
        data = _load_data(sys.argv[1])
        sorted_data = sleep_sort(data)
        print(sorted_data)


if __name__ == '__main__':
    main()

