#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

def main(files, flags, concepts, stats):

    # handle input files
    for f in files:
        # check if file exists
        print(f)
    
    # redact items specified in flags
    if "names" in flags:
        # redact names
        print("redact names")
    if "genders" in flags:
        # redact genders
        print("redact genders")
    if "dates" in flags:
        # redact dates
        print("redact dates")
    if "addresses" in flags:
        # redact addresses
        print("redact addresses")
    if "phones" in flags:
        # redact phones
        print("redact phones")
    
    # redact themes specified in concepts
    if len(concepts) > 0:
        for concept in concepts:
            # redact concept
            print(concept)

    # handle stats
    print(stats)
    
     
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", action='append', type=argparse.FileType('r'), nargs='+', required=True,
                        help="The files to redact")
    parser.add_argument("--names", action='store_true', help="redact names")
    parser.add_argument("--genders", action='store_true', help="redact genders")
    parser.add_argument("--dates", action='store_true', help="redact dates")
    parser.add_argument("--addresses", action='store_true', help="redact addresses")
    parser.add_argument("--phones", action='store_true', help="redact phones")
    parser.add_argument("--concept", action='append',
                        help="The theme/keyword to redact")
    parser.add_argument("--stats", type=argparse.FileType('w'), required=True,
                        help="file storing the summary of redaction process")
    args = parser.parse_args()
    if not args.input and not args.stats:
        # missing argument error
        print("missing arguments, use --help for details")
    elif not args.input:
        # no file error
        print("must provide files")
    elif not args.stats:
        # no file error
        print("must use --stats to provide file name to store statistics")
    else:
        # handling arguments
        # input files
        files = []
        for file_objs in args.input:
            for file_obj in file_objs:
                files.append(file_obj.name)

        # redaction flags
        redaction_flags = []
        if args.names:
            redaction_flags.append("names")
        if args.genders:
            redaction_flags.append("genders")
        if args.dates:
            redaction_flags.append("dates")
        if args.addresses:
            redaction_flags.append("addresses")
        if args.phones:
            redaction_flags.append("phones") 
        # concepts
        concepts = []
        if args.concept:
            concepts = args.concept
        # stats
        stats_file = args.stats.name
        # call main
        main(files, redaction_flags, concepts, stats_file)
