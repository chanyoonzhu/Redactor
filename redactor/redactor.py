#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

def main(files):
    for f in files:
        print(f)
     
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", action='append', type=argparse.FileType('r'), nargs='+', required=True,
                        help="The files to redact")
    args = parser.parse_args()
    if args.input:
        main(args.input)
