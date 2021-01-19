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

    if int(user_input_number) >= 100:
        if int(user_input_number) < 1000:
            result = True
        else:
            result = False
    else:
        result = False
    return result



def is_duplicated_number(three_digit):

    if len(set(three_digit)) == 3:
        result = False
    else:
        result = True
    return result





def is_validated_number(user_input_number):
    if is_digit(user_input_number) is True:
        if is_between_100_and_999(user_input_number) is True:
            if is_duplicated_number(user_input_number) is False:
                result = True
            else:
                result = False
        else:
            result = False
    else:
        result = False

    return result


def get_not_duplicated_three_digit_number():

    a = "0"
    is_validated_number(a)

    while is_validated_number(a) is not True:
        a = str(get_random_number())
        result = a

    return result


def get_strikes_or_ball(user_input_number, random_number):

    i = 0
    strike = 0
    ball = 0
    user_input_number = user_input_number.strip()
    random_number = random_number.strip()
    while(i < 3):
        j = 0
        while(j < 3):
            if is_validated_number(user_input_number) == False:
                break

            elif (i == j) is True:
                if random_number[i] == user_input_number[j]:
                    strike += 1


            else:
                if random_number[i] == user_input_number[j]:
                    ball += 1

            j += 1
        i += 1
    result = [strike,ball]

    return result



# 'str' object does not support item assignment 문자열/튜플은 = 안된다는거

def is_yes(one_more_input):
    # '''
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자

    if one_more_input.upper() == 'Y':
        result = True

    else:
        if one_more_input.upper() == 'YES':
            result = True
        else:
            result = False

    return result


def is_no(one_more_input):
    if one_more_input.upper() == 'N':
        result = True

    else:
        if one_more_input.upper() == 'NO':
            result = True
        else:
            result = False

    return result


def main():
    print("Play Baseball")

    random_number = str(get_not_duplicated_three_digit_number())

    print("Random Number is : ", random_number)
    user_input = '999'

    while(get_strikes_or_ball(user_input, random_number) != [3, 0]):

        user_input = input("Input guess number : ")

        if user_input != '0':

                if is_validated_number(user_input) is True:
                    get_strikes_or_ball(user_input, random_number)
                    print("Strikes : " +
                    str(get_strikes_or_ball(user_input, random_number)[0]) + " , " +
                    "Balls : " + str(get_strikes_or_ball(user_input, random_number)[1]))
                else:
                    print("Wrong Input, Input again")

        else:
            break

    if user_input is not '0':
        one_more_input = 'Y'
        while(is_no(one_more_input)) is not True:
            one_more_input = input("You win, one more(Y/N) ?")

            if is_yes(one_more_input) is True:
                random_number = str(get_not_duplicated_three_digit_number())

                print("Random Number is : ", random_number)
                user_input = '999'

                while(get_strikes_or_ball(user_input, random_number) != [3, 0]):

                    user_input = input("Input guess number : ")

                    if user_input != '0':

                            if is_validated_number(user_input) is True:
                                get_strikes_or_ball(user_input, random_number)
                                print("Strikes : " +
                                str(get_strikes_or_ball(user_input, random_number)[0]) + " , " +
                                "Balls : " + str(get_strikes_or_ball(user_input, random_number)[1]))===================

if __name__ == "__main__":
    main()