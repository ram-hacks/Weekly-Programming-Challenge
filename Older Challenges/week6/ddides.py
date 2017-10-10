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
    """ This is so bad """
    sortedd = []
    def add(x):
        sortedd.append(x)

    init = int(data[0])
    for value in data:
        if int(value) > init:
            init = int(value)
        Timer(int(value), add, value).start()
    time.sleep(init+1)
    
    return sortedd


def main():
    if len(sys.argv) < 2:
        print('Not enough arguments. Usage: $ python ddides.py inputfile')
    else:
        data = _load_data(sys.argv[1])
        print(sleep_sort(data))


if __name__ == '__main__':
    main()

