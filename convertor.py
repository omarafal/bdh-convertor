import sys
from exceptions import *
from math import floor


def main_convert(from_choice, to_choice, num):

    # if change FROM Decimal
    if from_choice == "Decimal":

        # verify that the number is decimal
        if not verify_decimal(num):
            print("This number is not " + from_choice)
            return null

        # if change TO Decimal
        if to_choice == "Decimal":
            print(num)
            return null

        # if change TO Binary
        elif to_choice == "Binary":
            print(to_binary(num))
            return null

        # if change TO Hexadecimal
        elif to_choice == "Hexadecimal":
            print(to_hexa(num))
            return null

    # if change FROM Binary
    elif from_choice == "Binary":

        # verify that the number entered is binary
        if not verify_binary(num):
            print("This number is not " + from_choice)
            return null

        # turn the number entered into decimal to make it easier to work with
        number = list(num)
        try:
            decimal_number = to_decimal(from_choice, number)

        except NotCorrectInputTypeError:
            print("This number is not " + from_choice)
            return null

        except ValueError:
            print("This number is not " + from_choice)
            return null

        # if change TO Binary
        if to_choice == "Binary":
            print(num)
            return null

        # if change TO Decimal
        elif to_choice == "Decimal":
            print(decimal_number)
            return null

        # if change TO Hexadecimal
        elif to_choice == "Hexadecimal":
            print(to_hexa(decimal_number))
            return null

    # if change FROM Hexadecimal
    elif from_choice == "Hexadecimal":

        # verify that the number entered is hexadecimal
        if not verify_hexa(num):
            print("This number is not " + from_choice)
            return null

        # turn the number entered into decimal to make it easier to work with
        number = list(num)
        try:
            decimal_number = to_decimal(from_choice, number)

        except NotCorrectInputTypeError:
            print("This number is not " + from_choice)
            return null

        except ValueError:
            print("Not a valid format")
            return null

        # if change TO Hexadecimal
        if to_choice == "Hexadecimal":
            print(num)
            return null

        # if change TO Decimal
        elif to_choice == "Decimal":
            print(decimal_number)
            return null

        # if change TO Binary
        elif to_choice == "Binary":
            print(to_binary(decimal_number))
            return null


def to_decimal(from_choice, num):
    """
    :param from_choice: Binary or Hexadecimal
    :param num: number as a list to convert to decimal
    :return: a decimal number
    """

    fraction = ""
    try:
        fraction = num[num.index(".")+1:]  # collects the fraction part of the decimal
        whole = num[:num.index(".")]  # collects the whole number part of the decimal
    except ValueError:
        whole = num

    if from_choice == "Binary":
        if not verify_binary(num):  # if the number is not binary
            raise NotCorrectInputTypeError

        collect_whole = 0  # variable to collect the whole as a number value
        collect_fraction = 0  # variable to collect the fraction as a number value

        if fraction:
            power_fraction = -1
            for i in fraction:
                collect_fraction += int(i) * 2**power_fraction
                power_fraction -= 1

        power_whole = 0
        i = -1
        for j in range(0, len(whole)):
            collect_whole += int(whole[i]) * 2**power_whole
            i -= 1
            power_whole += 1

        final = collect_whole + collect_fraction
        return final  # turn into a return statement

    ################
    elif from_choice == "Hexadecimal":
        if not verify_hexa(num):  # if the number is not Hexadecimal
            raise NotCorrectInputTypeError

    hexadecimals = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "A": "10",
        "B": "11",
        "C": "12",
        "D": "13",
        "E": "14",
        "F": "15",
    }
    collect_whole = 0  # variable to collect the whole as a number value
    collect_fraction = 0  # variable to collect the fraction as a number value

    if fraction:
        power_fraction = -1
        for i in fraction:
            collect_fraction += int(hexadecimals[i.upper()]) * 16**power_fraction
            power_fraction -= 1

    power_whole = 0
    i = -1
    for j in range(0, len(whole)):
        collect_whole += int(hexadecimals[whole[i].upper()]) * 16**power_whole
        i -= 1
        power_whole += 1

    final = collect_whole + collect_fraction
    return final


def to_binary(num):
    """
    :param num: number as a decimal
    :return: number as a binary
    """
    whole = ""
    fraction_list = ""

    try:
        fraction_list = list(str(num))[list(str(num)).index("."):]
        whole_list = list(str(num))[:list(str(num)).index(".")]
    except ValueError:
        whole_list = list(str(num))

    # if there is a fraction
    if fraction_list:

        fraction = ""
        for i in fraction_list:
            fraction += i

        # clear the list to reuse it
        fraction_list = []

        i = 0  # increment to prevent an infinite loop
        while fraction != 0 and i < 32:

            fraction = float(fraction) * 2
            remainder = floor(fraction)
            fraction_list.append(str(remainder))
            fraction -= remainder
            i += 1

    for j in whole_list:
        whole += j

    # clear the list to reuse it
    whole_list = []

    while int(whole) != 0:
        remainder = int(whole) % 2
        whole_list.insert(0, str(remainder))
        whole = (int(whole) - remainder) / 2

    collect = ""  # variable to collect the whole number
    for k in whole_list:
        collect += k

    if fraction_list:
        collect += "."
        for l in fraction_list:
            collect += l

    return collect


def to_hexa(num):
    """
    :param num: number as a decimal
    :return: number as a hexadecimal
    """
    hexadecimals = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "10": "A",
        "11": "B",
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F",
    }
    whole = ""
    fraction_list = ""

    try:
        fraction_list = list(str(num))[list(str(num)).index("."):]
        whole_list = list(str(num))[:list(str(num)).index(".")]
    except ValueError:
        whole_list = list(str(num))

    # if there is a fraction
    if fraction_list:

        fraction = ""
        for i in fraction_list:
            fraction += i

        # clear the list to reuse it
        fraction_list = []

        i = 0  # increment to prevent an infinite loop
        while fraction != 0 and i < 32:
            fraction = float(fraction) * 16
            remainder = floor(fraction)
            fraction_list.append(hexadecimals[str(remainder)])
            fraction -= remainder
            i += 1

    for j in whole_list:
        whole += j

    # clear the list to reuse it
    whole_list = []

    while int(whole) != 0:
        remainder = int(whole) % 16
        whole_list.insert(0, hexadecimals[str(remainder)])
        whole = (int(whole) - remainder) / 16

    collect = ""  # variable to collect the whole number
    for k in whole_list:
        collect += k
    if fraction_list:
        collect += "."
        for l in fraction_list:
            collect += l

    return collect


def verify_decimal(numbers):
    """
    :param numbers: number as a string
    :return: True or False
    """
    valid_numbers = ".0123456789"
    for num in numbers:
        if num not in valid_numbers:
            return False

    return True


def verify_binary(numbers):
    """
    :param numbers: number as a string
    :return: True or False
    """
    if "0" in numbers or "1" in numbers:
        for num in numbers:
            if num != "0" and num != "1" and num != ".":
                return False
        return True


def verify_hexa(numbers):
    """
        :param numbers: number as a string
        :return: True or False
    """
    valid_hexadecimals = '.0123456789ABCDEFabcdef'

    for num in numbers:
        if num not in valid_hexadecimals:
            return False

    return True


from_choice = sys.argv[1]
to_choice = sys.argv[2]
num1 = sys.argv[3]

main_convert(from_choice, to_choice, num1)
