import math


def int_to_bit(x):
    arr = []
    for i in range(16):
        arr.append(x >> i & 1)
    arr.reverse()
    return arr


def check_if_even():
    number_of_repeat = int(math.sqrt(len(int_to_bit(number))))
    list_of_bites = int_to_bit(number)
    for i in range(number_of_repeat):
        size_of_returns_list = int(len(list_of_bites) / 2)
        list_of_bites = divide_and_check([], list_of_bites, size_of_returns_list, True)
    return list_of_bites


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


number = 732
list_of_bits = int_to_bit(number)
print("list_of_data before adding even bit == " + str(list_of_bits))
print("even bit == " + str(check_if_even()[0]))
list_of_bits.append(check_if_even()[0])
print("final_list == " + str(list_of_bits))
