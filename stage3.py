#!/usr/bin/env python3
from os import getenv
username = getenv("USER")
usernamelen = len(username)
ans = 0

while True:
    ans += 1
    length = len(str(ans)) + usernamelen
    if (ans // length // 12) > length:
        break

print(ans)
