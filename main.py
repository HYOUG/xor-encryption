#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# script by "HYOUG"

from argparse import ArgumentParser


def xorbytes(target:bytes, key:bytes) -> bytes:
    output = []
    index = 0
    for byte in target:
        output.append(byte ^ key[index % (len(key)-1)])
    return bytes(output)


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("fp_target", help="File pointer of the target")
    parser.add_argument("fp_key", help="File pointer of the key")
    args = parser.parse_args()
    
    with open(args.fp_target, "rb") as f:
        target_data = f.read()
    with open(args.fp_key, "rb") as f:
        key_data = f.read()
        
    new_data = xorbytes(target_data, key_data)
    if "." in args.fp_target:
        new_fp = f"{'.'.join(args.fp_target.split('.')[:-1])}_encrypted.{args.fp_target.split('.')[-1]}"
    else:
        new_fp = f"{args.fp_target}_encrypted"
    
    with open(new_fp, "wb") as f:
        f.write(new_data)


if __name__ == "__main__":
    main()