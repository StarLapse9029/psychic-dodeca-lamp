#!/usr/bin/env python3
# Reminder to chmod +x

import argparse
import base64
import sys

DECODERS = {
        "base16": base64.b16decode,
        "base32": base64.b32decode,
        "base64": base64.b64decode,
        "base85": base64.b85decode,
        }

def main():
    parser = argparse.ArgumentParser(
            description="Decode string in different bases"
            )
    group = parser.add_mutually_exclusive_group(required=True)
    for base in DECODERS:
        group.add_argument(f"--{base}",                        
                           help=f"Decode form {base}",
                           action='store_true')
    parser.add_argument("-i", "--iterations",
                        type=int,
                        default=1,
                        help="Number of iterations")
    parser.add_argument("string", help="String to decode")

    args = parser.parse_args()
    arguments = [i for i, j in args.__dict__.items() if j]
    print(f"Decoding: {arguments[0]}")
    print(f"Iterating: {args.iterations}")
    
    ptr = args.string
    for i in range(args.iterations):
        j = decode(arguments[0], ptr)
        print(f"Iteration {i+1}: {j}")
        ptr = j

def decode(base, string):
    if isinstance(string, str):
        string = string.encode()
    try:
        return DECODERS[base](string)
    except Exception as e:
        print(f"Failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

