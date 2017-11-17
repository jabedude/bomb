from os import getenv
username = getenv("USER")
length = len(username)
first_letter = ord(username[0])

nums = [first_letter + 1]

for i in range(4):
    nums.append(nums[-1] + (nums[-1] ))
    print(nums)

if (nums[-1] % 2 == 0):
    nums[-1] += 1

print(nums)
