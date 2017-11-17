#!/usr/bin/env python3
from os import getenv
username = getenv("USER")
length = len(username)
first_letter = ord(username[0])

nums = [first_letter + 1]

for i in range(4):
    nums.append(nums[-1] + (nums[-1] ))

if (nums[-1] % 2 == 0):
    nums[-1] += 1

print(" ".join(str(x) for x in nums))
