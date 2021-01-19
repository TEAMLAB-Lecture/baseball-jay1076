# -*- coding: utf-8 -*-

import random


def get_random_number():

    return random.randrange(100, 1000)


def is_digit(user_input_number):

    if user_input_number.isdigit() is True:
        result = True
    else:
        result = False

    return result


def is_between_100_and_999(user_input_number):
    user_input_number = int(user_input_number)
    if user_input_number >= 100 and user_input_number < 1000: 
        result = True
    else:
        result = False
    return result


def is_duplicated_number(three_digit):
    three_digit = str(three_digit)
    temp = len(set(three_digit))
    if temp == 3:
        result = False
    else:
        result = True
    # ==================================
    return result


def is_validated_number(user_input_number):
    if is_digit(user_input_number) == True and is_between_100_and_999(user_input_number) == True and is_duplicated_number(user_input_number) == False:
        result = True
    else:
        result = False
    return result


def get_not_duplicated_three_digit_number():
    user_input_number = get_random_number()
    while is_validated_number(user_input_number) == False:
        user_input_number = get_random_number()
    result = user_input_number
    # ==================================
    return result


def get_strikes_or_ball(user_input_number, random_number):
    a = user_input_number
    b = random_number
    st = 0
    ba = 0
    for i in range(0,3):
        for j in range(0,3):
            if a[i] == b[j]:
                if i == j:
                    st = st + 1
                else:
                    ba = ba + 1
    result = [st,ba]
    return result


def is_yes(one_more_input):
    one_more_input = one_more_input.upper()
    if one_more_input == "Y" or one_more_input == "YES":
        result = True
    else:
        result = False
    return result


def is_no(one_more_input):
    one_more_input = one_more_input.upper()
    if one_more_input == "N" or one_more_input == "NO":
        result = True
    else:
        result = False
    return result


def main():
    print("Play Baseball")
    random_number = str(get_not_duplicated_three_digit_number())
    print("Random Number is : ", random_number)
        while 1:
            if ret[0] == 3:
                inp = input("You win, one more(Y/N) ?")
            if is_no(inp) == True:
                flag = False
                break
            elif is_yes(inp) == True:
                flag = True
                random_number = str(get_not_duplicated_three_digit_number())
                print("Random Number is : ", random_number)
                break
            else:
                print("Wrong Input, Input again")
        if flag == False:
            break
    print("Thank you for using this program")
    print("End of the Game")

if __name__ == "__main__":
    main()