#!/usr/bin/env python

def missing_num(nums):
    return list(filter(lambda x: x not in nums, range(1, max(nums)+1))).pop(0)

if __name__ == '__main__':
    assert missing_num([7,8,10,3,6,5,1,2,9]) == 4
    assert missing_num([1,3]) == 2

