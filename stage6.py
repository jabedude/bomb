from os import getenv

user_char = getenv("USER")[0]       # Get first char in username
user_char = ord(user_char)

startchar = ord('a')

while True:
    if (user_char & startchar) % 2 == 0:
        char = (user_char & startchar) // 2
        print("{} {} {}".format(char, chr(startchar), char))
        break
    else:
        startchar += 1
