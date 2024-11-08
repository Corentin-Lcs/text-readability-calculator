#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import logging
import re

__author__ = 'Corentin L.'
__version__ = '1.0'

def args_parser():
    parser = argparse.ArgumentParser(
        prog='desmetrics',
        description=f'DesMetrics v{__version__} - Calculate the Coleman-Liau Index of a text file.',
        usage='%(prog)s <input_file> [options]'
    )
    # Verbosity level
    parser.add_argument('-v', '--verbose', action='count', default=0, dest='verbosity', help='enable verbose logging')
    # Version information
    parser.add_argument('-V', '--version', action='version', version=f'%(prog)s {__version__}')
    # Input file
    parser.add_argument('input_file', type=str, help='path to the input .txt file')
    return parser.parse_args()

def setup_logging(verbosity: int):
    global logger
    logging.basicConfig(format='%(message)s')
    logger = logging.getLogger()
    if verbosity == 0:
        logger.setLevel(logging.WARNING)
    elif verbosity == 1:
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.DEBUG)

def count_sentences(text: str) -> int:
    return len(re.findall(r'[.!?]', text))

def count_words(text: str) -> int:
    return len(re.findall(r'\b\w+\b', text))

def count_letters(text: str) -> int:
    return len(re.findall(r'[a-zA-Z]', text))

def calculate_coleman_liau_index(letters: int, words: int, sentences: int) -> float:
    L = (letters / words) * 100
    S = (sentences / words) * 100
    return 0.0588 * L - 0.296 * S - 15.8

def process_file(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except Exception as e:
        logger.critical(f'Error reading file {file_path}: {e}')
        exit(1)

def main():
    # Init
    global args
    args = args_parser()
    setup_logging(args.verbosity)
    # Process
    logger.warning(f'DesMetrics v{__version__}')
    text = process_file(args.input_file)
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)
    logger.info(f'Letters: {letters}, Words: {words}, Sentences: {sentences}')
    index = calculate_coleman_liau_index(letters, words, sentences)
    print(f'\n{args.input_file} | Coleman-Liau Index: {index:.2f}')

if __name__ == '__main__':
    main()