#!/usr/bin/env python3
from os import getenv
username = getenv("USER")                   # Get the user's username and calculate the length
usernamelen = len(username)
ans = 0

while True:
    ans += 1                                # Starting at zero, loop until the first number is greater than
    length = len(str(ans)) + usernamelen    # the length of the number plus the username length
    if (ans // length // 12) > length:
        break

print(ans)
