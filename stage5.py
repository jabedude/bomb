from os import getenv
username = getenv("USER")   # Get username
username_vals = [ord(character) for character in username]
input_num = 1000            # Just pick a high number. We will adjust later
master_input = 1000
char1 = ord('~')            # Use tildes because it's the highest printable ascii val (126)
char2 = ord('~')

def math_one(val):
    global input_num
    input_num -= (char1 + val)

def math_two(val):
    global input_num
    input_num -= (val * 2)

def math_three(val):
    global input_num
    input_num -= (val)

def math_four(val):
    global input_num
    input_num += char2 - val

def math_five(val):
    global input_num
    input_num -= (val + char2)

def math_six(val):
    global input_num
    input_num -= (char2)

group_one = [97,101,105,111,117,121,math_one]
group_two = [98,99,100,math_two]
group_three = [102,103,104,math_three]
group_four = [106,107,108,109,110,math_four]
group_five = [112,113,114,115,116,math_five]
group_six = [118,119,120,122,math_six]

master_list = [group_one, group_two, group_three, group_four, group_five, group_six]

for value in username_vals:
    group = [x for x in master_list if value in x]      #find our list
    group[0][-1](value)

ans = master_input - input_num
print("{} {} {}".format(chr(char1), ans, chr(char2)))
