#!/usr/bin/env python


from gendiff.generate_diff import generate_diff


import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument("-v", "--format", help="set format of output")
    args = parser.parse_args()
    file_path1 = str(args.first_file)
    file_path2 = str(args.second_file)
    print(generate_diff(file_path1, file_path2))


if __name__ == '__main__':
    main()
