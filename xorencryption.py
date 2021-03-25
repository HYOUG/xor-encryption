#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# script by "HYOUG"

from random import choices
from sys import argv
from time import strftime


bin_format = lambda bin_value, lenght:  "0" * (lenght - len(str(bin_value)[2:])) + str(bin_value)[2:]   # anonymous function that format the binary values

char_list = [chr(i) for i in range(128)]                                                                # list of avaible characters
str2bin_dict = {char_list[i] : bin_format(bin(i), 8) for i in range(len(char_list))}                    # convertion dictionary
bin2str_dict = {value: key for (key, value) in str2bin_dict.items()}                                    # //
open("quick_test.txt", "w", encoding="utf-8").write("".join(char_list))


def str2bin(text, convertion_dict: dict = str2bin_dict) -> str:
    """Convert text into 'binary' from the str2bin dcitionary"""
    assert isinstance(text, list) or isinstance(text, str), f"Unexpected argument type : {type(text)}.\nExpected argument type : list of str or str"
    assert isinstance(convertion_dict, dict), f"Unexpected argument type : {type(convertion_dict)}.\nExpected argument type : dict"
    return [convertion_dict[i] for i in text]


def bin2str(binary, convertion_dict: dict = bin2str_dict) -> str:
    """Convert 'binary' value into text from the bin2str dictionary or the specified one"""
    assert isinstance(binary, list) or isinstance(binary, str), f"Unexpected argument type : {type(binary)}.\nExpected argument type : list of str or str"
    if isinstance(binary, list):                                                                        # list case
        output_str = ""
        for value in binary:
            while True:
                if value in convertion_dict.keys():
                    output_str += convertion_dict[value]
                    break
                else:
                    value = int2bin(bin2int(value) - len(list(convertion_dict.keys())))
            return output_str
                    
    elif isinstance(binary, str):                                                                       # string case
        while True:
            if binary in convertion_dict.keys():
                return convertion_dict[binary]
            else:
                value = int2bin(bin2int(value) - len(list(convertion_dict.keys())))


def bin2int(binary) -> int:
    """Convert a 'binary' value into an integer"""
    assert isinstance(binary, list) or isinstance(binary, str), f"Unexpected argument type : {type(binary)}.\nExpected argument type : list of str or str"
    if isinstance(binary, list):                                                                        # list case
        return [sum([int(value[i]) * 2**(len(value) - (i + 1)) for i in range(len(value))]) for value in binary]
    elif isinstance(binary, str):                                                                       # string case
        return sum([int(binary[i]) * 2**(len(binary) - (i + 1)) for i in range(len(binary))])


def int2bin(integer) -> str:
    """Convert an integer into a 'binary' value"""
    assert isinstance(integer, list) or isinstance(integer, int), f"Unexpected argument type : {type(integer)}.\nExpected argument type : list of int or int "
    if isinstance(integer, list):                                                                       # list case
        return [bin_format(bin(value), 8) for value in integer]
    elif isinstance(integer, int):                                                                      # string case
        return bin_format(bin(integer), 8)


def xor_operation(target: str, key: str) -> str:
    """XOR operation on two binaty values"""
    assert isinstance(target, str), f"Unexpected argument type : {type(target)}.\nExpected argument type : str"
    assert isinstance(key, str), f"Unexpected argument type : {type(key)}.\nExpected argument type : str"
    bin_output = ""
    for i in range(len(target)):
        if key[i] == "1":                                                                               # XOR operation
            if target[i] == "1":                                                                        # //
                bin_output += "0"                                                                       # //
            elif target[i] == "0":                                                                      # //
                bin_output += "1"                                                                       # //
        else:                                                                                           # //
            bin_output += target[i]                                                                     # //
    return bin_output


def gen_key(char_list: list = char_list, lenght: int = 8) -> str:
    """Generate a random key from the given char. list and given lenght"""
    assert isinstance(char_list, list), f"Unexpected argument type : {type(char_list)}.\nExpected argument type : list of str"
    assert isinstance(lenght, list), f"Unexpected argument type : {type(lenght)}.\nExpected argument type : int"
    return "".join(choices(char_list, k=lenght))


def multisplit(target: str, split_list: list) -> list:
    """Split a text with multiple characters"""
    assert isinstance(target, str), f"Unexpected argument type : {type(target)}.\nExpected argument type : str"
    assert isinstance(split_list, list), f"Unexpected argument type : {type(split_list)}.\nExpected argument type : list"
    for char in split_list:
        if isinstance(target, str):
            target.split(char)
        else:
            for item in target:
                item.split(char)
    return target


def encrypt(target: str, key: str) -> str:
    """Encrypt the 'text-target' with the given key"""
    formated_key = key * (len(target) // len(key)) +                         \
                   key[0:len(target) - len(key * (len(target) // len(key)))]                            # format the initial key into a new one that is the same size as the target text
    target_bin = str2bin(target)
    key_bin = str2bin(formated_key)
    output = "".join([bin2str(xor_operation(target_bin[i], key_bin[i])) for i in range(len(target_bin))])
    return output


def decrypt(target: str, key: str) -> str:
    """Decrypt the 'text-target' with the given key"""
    return encrypt(target, key)                                                                         # the decryption function is the same as the encryption one


def main():                                                                                             # main function
    if len(argv) == 4:                                                                                  # command line arguments mode
        try:
            mode = argv[1]                                                                              # fetch the command line arguments
            key = argv[2]                                                                               # //
            fp = argv[3]                                                                                # //
            assert mode in ["-e", "-d"], f"Unexpected command line argument : {mode}.\n"    \
                                           "Expected command line argument : '-e' or '-d'"              # check if the command line argument 'mode' is valid
            try:
                text = open(fp, "r", encoding="utf-8").read()                                           # read the content of the target file (utf-8 encoding)
                output = encrypt(text, key)                                                             # encrypt/decrypt the content of the target file
                result = open(f"output_{strftime('%d-%m-%Y_%H.%M.%S')}.txt", "w")                       # new output file
                result.write(output)                                                                    # write the output in the new output file
                result.close()                                                                          # close the new output file
                print(f"The encrypted/decrypted content of {fp} have been successfuly saved " \
                      "in output_{strftime('%d-%m-%Y_%H.%M.%S')}.txt with the following key : {key}")
                
            except FileNotFoundError:                                                                   # error : target file not found
                raise Exception(f"File not found for : {fp}")
            
        except IndexError:                                                                              # error : invalid command line arguments
            raise Exception("Usage : python binencryption.py (key) (file path)")
        
    elif len(argv) == 1:                                                                                # input arguments mode
        target = input("Enter the text to encrypt/decrypt : ")
        key = input("Enter the key :")
        output = encrypt(target, key)
        print(f"output : {output}")
        

if __name__ == "__main__":                                                                              # main program
    main()