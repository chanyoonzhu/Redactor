#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def redact_names (text):
    text_str = text
    names = []
    # POS tag sentences
    sentences = nltk.sent_tokenize(text_str)
    sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    sentences = [nltk.pos_tag(sentence) for sentence in sentences]
    # find out names and add to names list
    for sentence_tagged in sentences:
        for chunk in nltk.ne_chunk(sentence_tagged):
            print(chunk)
            if type(chunk) == nltk.tree.Tree and chunk.label() == 'PERSON':
                names.append(' '.join([word[0] for word in chunk]))
    # replace names with character
    # TODO
    return text_str

def redact_genders (text):
    text_str = text
    return text_str

def redact_dates (text):
    text_str = text
    return text_str

def redact_addresses (text):
    text_str = text
    return text_str

def redact_phones (text):
    text_str = text
    return text_str

def redact_concept(text, concept):
    text_str = text
    return text_str

def redact(text, flags, concepts):
    content = text
    if "names" in flags:
        # redact names
        content = redact_names(content)
    if "genders" in flags:
        # redact genders
        content = redact_genders(content)
    if "dates" in flags:
        # redact dates
        content = redact_dates(content)
    if "addresses" in flags:
        # redact addresses
        content = redact_addresses(content)
    if "phones" in flags:
        # redact phones
        content = redact_phones(content)
    # redact themes specified in concepts
    if len(concepts) > 0:
        for concept in concepts:
            # redact concept
            redact_concept(content, concept)
    # return redacted string
    return content

def main(files, flags, concepts, output_dir, stats):
    # handle input files
    for file in files:
        # check if file exists
        with open(file, 'r') as f:
            # store file content in string
            raw_content = f.read()
            # redact items specified in flags
            redact(raw_content, flags, concepts)

            # handle output
            # ***TODO*** output not dir
            print(output_dir)

            # handle stats
            print(stats)
    

### parse args ###

class FullPaths(argparse.Action):
    """Expand user- and relative-paths"""
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, os.path.abspath(os.path.expanduser(values)))

def is_dir(dirname):
    """Checks if a path is an actual directory"""
    if not os.path.isdir(dirname):
        msg = "{0} is not a directory".format(dirname)
        raise argparse.ArgumentTypeError(msg)
    else:
        return dirname   
     
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
    parser.add_argument("--output", required=True, help="directory to store redacted files", action=FullPaths, type=is_dir)
    parser.add_argument("--stats", type=argparse.FileType('w'), required=True,
                        help="file storing the summary of redaction process")
    args = parser.parse_args()
    if not args.input and not args.output and not args.stats:
        # missing argument error
        print("missing arguments, use --help for details")
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
        # outputs
        output_dir = args.output
        # stats
        stats_file = args.stats.name
        # call main
        main(files, redaction_flags, concepts, output_dir, stats_file)
