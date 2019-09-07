import sys
import argparse
import os
from plagiarizer import *


def start():
    # compile list of synonyms in a var
    syn_list = get_syns(ARGS)

    # syn list is a 2-D list of words. All words in a subarray should be treated equally
    syn_dict = make_syn_dict(syn_list)

    print(syn_dict)


def get_args():
    parser = argparse.ArgumentParser(description=HELP_MESSAGE)

    # Required switch: Synonym list file name
    parser.add_argument('-s', '--syn', required=True, help='File name for synonym list. Ensure it is in the same\n'
                                                           'directory as this file.')

    # Required switch: Input file one
    parser.add_argument('--fileone', required=True, help='File name of input file one. Ensure it is in the same \n'
                                                         'directory as this file.')

    # Required switch: Input file two
    parser.add_argument('--filetwo', required=True, help='File name of input file two. Ensure it is in the same \n'
                                                         'directory as this file')

    # Optional switch: tuple size
    parser.add_argument('-t', '--tuple', required=False, default=3, type=int, help='Optional tuple size switch. '
                                                                                   'Default is 3.')

    try:
        return parser.parse_args()
    except argparse.ArgumentError as e:
        print('Arguments supplied could not be parsed. Check and run again...\n{}'.format(e))
        sys.exit(0)


# method will check if file(s) supplied can be found in this directory or not
def run_sanities():
    if (not os.path.exists(ARGS.syn)) or (not os.path.exists(ARGS.fileone)) or (not os.path.exists(ARGS.filetwo)):
        print('At least one of the filepaths provided could not be found in the current directory.')
        print('Try running again with files in correct place...')
        sys.exit(0)


if __name__ == '__main__':
    # check for correct number of arguments
    HELP_MESSAGE = 'Please supply as arguments:\n(1) file name with synonym list\n(2) first input file\n' \
                   '(3) second input file\n(4) OPTIONAL - Tuple size, default is 3.'
    if len(sys.argv) != 7:
        print(HELP_MESSAGE)
        sys.exit(0)

    # parse arguments
    ARGS = get_args()

    # sanitize arguments
    run_sanities()

    # trigger start of control flow
    start()
