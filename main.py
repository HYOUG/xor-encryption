#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# script by "HYOUG"

from random import choices
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from sys import argv


bin_format = lambda bin_value, lenght:  "0" * (lenght - len(str(bin_value)[2:])) + str(bin_value)[2:]   # anonymous function that format the binary values

char_list = [" "] + list(ascii_lowercase) + list(ascii_uppercase) + list(digits) + list(punctuation)    # list of avaible characters
str2bin_dict = {char_list[i] : bin_format(bin(i), 8) for i in range(len(char_list))}                    # convertion dictionary
bin2str_dict = {value: key for (key, value) in str2bin_dict.items()}                                    # idem.
print(str2bin_dict)


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
    assert isinstance(binary, list) or isinstance(binary, str), f"Unexpected argument type : {type(binary)}.\nExpected argument type : list of str or str"
    if isinstance(binary, list):
        return [sum([int(value[i]) * 2**(len(value) - (i + 1)) for i in range(len(value))]) for value in binary]
    elif isinstance(binary, str):
        return sum([int(binary[i]) * 2**(len(binary) - (i + 1)) for i in range(len(binary))])


def int2bin(integer) -> str:
    """Convert an integer into a 'binary' value"""
    assert isinstance(integer, list) or isinstance(integer, int), f"Unexpected argument type : {type(integer)}.\nExpected argument type : list of int or int "
    if isinstance(integer, list):
        return [bin_format(bin(value), 8) for value in integer]
    elif isinstance(integer, int):
        return bin_format(bin(integer), 8)


def stack_bin(bin_target: str, bin_key: str) -> str:
    """'Stack' two binary values in order to get a combined one"""
    assert isinstance(bin_target, str), f"Unexpected argument type : {type(bin_target)}.\nExpected argument type : str"
    assert isinstance(bin_key, str), f"Unexpected argument type : {type(bin_key)}.\nExpected argument type : str"
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


def gen_key(char_range: list = char_list.remove(" "), lenght: int = 8) -> str:
    """Generate a random key from the given char. list and given lenght"""
    return "".join(choices(char_range, k=lenght))



def encrypt(target, key):                                                                               # encryption function

    target_bin = str2bin(target)
    key_bin = str2bin(key)

    for i in range(len(target_bin) * len(key_bin)):
        target_index = i
        key_index = i

        while target_index >= len(target_bin):
            target_index -= len(target_bin)
        while key_index >= len(key_bin):
            key_index -= len(key_bin)

        target_bin[target_index] = stack_bin(target_bin[target_index], key_bin[key_index])

    return bin2str(target_bin)


def decrypt():                                                                                          # decryption function
    pass


def main():

    usage_text = "Usage : main.py ..."                                                                  # asserts
    assert argv[1] in ["-e", "-d", "-ui"], usage_text
    assert argv[2] in ["-t", "-d"], usage_text

    if argv[1] == "-e":                                                                                 # get the mode from the command line arguments
        mode = "encryption"
    elif argv[1] == "-d":
        mode = "decryption"
    elif argv[1] == "-ui":
        mode = "ui"

    if argv[2] == "-t":                                                                                 # get the target source from the command line arguments
        source = "text"
    elif argv[2] == "-d":
        source = "document"

    if source == "text":                                                                                # get the text-target from the command line arguments
        target = " ".join(argv[3:])[1:-1]
    elif source == "document":
        target = open(argv[3], "r").read()

    if mode == "encryption":                                                                            # run the encryption/decryption
        key = gen_key(char_list, 8)
        print(encrypt(target, key))
    elif mode == "decryption":
        print(decrypt(target, key))
    elif mode == "ui":
        pass
    

            
if __name__ == "__main__":                                                                              # main program
    main()


"""
TODO :
'running' args :
main.py [-e|-d] [-t|-d] [text|fp]
decrypting
edit namings
"""