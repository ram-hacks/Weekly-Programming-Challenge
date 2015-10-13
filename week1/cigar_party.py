"""
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
"""

def cigar_party(cigars, weekend):
    return (40 < cigars < 60 and weekend is False) or (cigars > 40 and weekend is True)

def main():
    print('1: ', cigar_party(30, False))
    print('2: ', cigar_party(50, False))
    print('3: ', cigar_party(70, True))

if __name__ == '__main__':
    main()
