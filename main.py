import math


def int_to_bit(x):
    arr = []
    for i in range(16):
        arr.append(x >> i & 1)
    arr.reverse()
    return arr


def bin_to_int(list_bits):
    x = 0
    for i in range(len(list_bits)):
        x += list_bits[i] * 2 ** (len(list_bits) - i - 1)
    return x


def check_if_even(num):
    number_of_repeat = int(math.sqrt(len(int_to_bit(num))))
    list_of_bites = int_to_bit(num)
    for i in range(number_of_repeat):
        size_of_returns_list = int(len(list_of_bites) / 2)
        list_of_bites = divide_and_check([], list_of_bites, size_of_returns_list, True)
    return list_of_bites[0]


def divide_and_check(returns_list, list_bit, size_of_returns_list, is_stop):
    left_part = []
    right_part = []
    for i in range(int(len(list_bit) / 2)):
        left_part.append(list_bit[i])
        right_part.append(list_bit[int(len(list_bit) / 2) + i])
    if int(len(left_part)) != 1:
        divide_and_check(returns_list, left_part, size_of_returns_list, False)
    if int(len(right_part)) != 1:
        divide_and_check(returns_list, right_part, size_of_returns_list, False)
    if int(len(right_part)) == 1 and int(len(left_part)) == 1:
        returns_list.append(check(left_part[0], right_part[0]))
    if int(len(returns_list)) == size_of_returns_list and is_stop:
        return returns_list


def check(x, y):
    return 0 if x == y else 1


def get_decode_message(list_of_bits):
    message = []
    for i in range(int(len(list_of_bits) - 1)):
        message.append(list_of_bit[i])
    return message


def is_message_broken(message):
    if message[-1] == check_if_even(bin_to_int(get_decode_message(message))):
        return False
    else:

        return True


number = 732
list_of_bit = int_to_bit(number)
print("number == " + str(number))
print("list_of_data before adding even bit == " + str(list_of_bit))
print("even bit == " + str(check_if_even(number)))
list_of_bit.append(check_if_even(number))
print("final_list == " + str(list_of_bit))
print("decode message == " + str(get_decode_message(list_of_bit)))
print("is message broken == " + str(is_message_broken(list_of_bit)))
