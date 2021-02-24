#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# script by "HYOUG"

from random import choices, randint
from string import ascii_lowercase, digits


bin_format = lambda bin_value, lenght:  "0" * (lenght - len(str(bin_value)[2:])) + str(bin_value)[2:]   # anonymous function that format the binary values

char_list = [" "] + list(ascii_lowercase) + list(digits)                                                # list of avaible characters
str2bin_dict = {char_list[i] : bin_format(bin(i), 6) for i in range(len(char_list))}                    # convertion dictionary
bin2str_dict = {value: key for (key, value) in str2bin_dict.items()}                                    # idem.


def str2bin(text: list, convertion_dict: dict = str2bin_dict) -> str:
    """Convert text into 'binary' from the str2bin dcitionary"""
    return [convertion_dict[i] for i in text]


def bin2str(binary: list, convertion_dict: dict = bin2str_dict) -> str:
    """Convert 'binary' value into text from the bin2str dictionary or the specified one"""
    output_str = ""
    for value in binary:
        while True:
            if value in convertion_dict.keys():
                output_str += convertion_dict[value]
                break
            else:
                value = int2bin(bin2int(value) - len(list(convertion_dict.keys())))
    return output_str


def bin2int(binary) -> int:
    """Convert a 'binary' value into an integer"""
    if isinstance(binary, list):
        return [sum([int(value[i]) * 2**(len(value) - (i + 1)) for i in range(len(value))]) for value in binary]
    if isinstance(binary, str):
        return sum([int(binary[i]) * 2**(len(binary) - (i + 1)) for i in range(len(binary))])


def int2bin(integer) -> str:
    """Convert an integer into a 'binary' value"""
    if isinstance(integer, list):
        return [bin_format(bin(value), 6) for value in integer]
    if isinstance(integer, int):
        return bin_format(bin(integer), 6)


def stack_bin(bin_target: str, bin_key: str) -> str:
    """'Stack' two binary values in order to get a combined one"""
    bin_output = ""
    for i in range(len(bin_target)):
        if bin_key[i] == "1":
            if bin_target[i] == "1":
                bin_output += "0"
            elif bin_target[i] == "0":
                bin_output += "1"
        else:
            bin_output += bin_target[i]
    return bin_output


def gen_key(char_range: list = char_list.remove(" "), lenght: int = 6) -> str:
    """Generate a random key from the given char. list and given lenght"""
    return "".join(choices(char_range, k=lenght))


def rotate(binary: str) -> str:
    return binary[1:] + binary[0]


def encrypt():
    pass


def decrypt():
    pass


def main():
    target_str = input("Enter the text to crypt : ").lower()
    key_str = gen_key(char_list, randint(1, 10))

    target_bin_list = str2bin(target_str)
    key_bin_list = str2bin(key_str)

    print(f"target          : {target_str}")
    print(f"target bin list : {' '.join(target_bin_list)}")
    print(f"key string      : {key_str}")
    print(f"key bin list    : {' '.join(key_bin_list)}")
    print("encrypting...")

    for i in range(len(target_bin_list) * len(key_bin_list)):
        target_index = i
        key_index = i

        while target_index >= len(target_bin_list):
            target_index -= len(target_bin_list)
        while key_index >= len(key_bin_list):
            key_index -= len(key_bin_list)

        target_bin_list[target_index] = stack_bin(target_bin_list[target_index], key_bin_list[key_index])
            


    print(bin2str(target_bin_list))

            
if __name__ == "__main__":                                                                              # main program
    main()


"""
TODO :
'running' args
decrypting
"""