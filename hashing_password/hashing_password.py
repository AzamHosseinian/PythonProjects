# -*- coding: utf-8 -*-

"""
A script for hashing a given password using specified hashing algorithms.
"""

import argparse
import hashlib


def parse_arguments():
    """
    Parse command line arguments.
    """
    parser = argparse.ArgumentParser(description='Hash a given password.')
    parser.add_argument('password', help='Input password you want to hash.')
    parser.add_argument('-t', '--type', default='sha256', choices=['sha256', 'sha512', 'md5'],
                        help='The type of hashing algorithm to use.')
    return parser.parse_args()


def hash_password(password: str, hash_type: str) -> str:
    """
    Hash the given password using the specified hashing algorithm.
    """
    try:
        hash_object = getattr(hashlib, hash_type)()
        hash_object.update(password.encode())
        return hash_object.hexdigest()
    except AttributeError:
        raise ValueError(f"Unsupported hash type: {hash_type}")


def main():
    args = parse_arguments()
    password = args.password
    hash_type = args.type

    try:
        hashed_password = hash_password(password, hash_type)
        print(f"< hash-type : {hash_type} >")
        print(hashed_password)
    except ValueError as ve:
        print(f"Error: {ve}")


if __name__ == "__main__":
    main()
