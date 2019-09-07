import sys
import argparse
import os
from plagiarizer import *

PLAGIARISM_COUNTER = 0
TOTAL_TUPLE_COUNT = 0


def start():
    # compile list of synonyms in a var
    syn_list = get_syns(ARGS)

    # syn list is a 2-D list of words. All words in a subarray should be treated equally
    syn_dict = make_syn_dict(syn_list)

    # parse all data as a str from both files into global variables that will be sliced every time a tuple is generated
    global FILE_ONE
    FILE_ONE = get_file_data(ARGS.fileone)
    global FILE_TWO
    FILE_TWO = get_file_data(ARGS.filetwo)

    # generate N-tuples sequentially, and pass those tuples into string comparison, and increment TOTAL_TUPLE_COUNT

    while (len(FILE_ONE) >= ARGS.tuple) or (len(FILE_TWO) >= ARGS.tuple):
        file_one_tuple = FILE_ONE[0 : ARGS.tuple]
        FILE_ONE = FILE_ONE[1:]
        print(FILE_ONE)
        file_two_tuple = FILE_TWO[0 : ARGS.tuple]
        FILE_TWO = FILE_TWO[1:]

        # at this stage, we have generated two tuples that we can then compare...
        if check_plagiarism(file_one_tuple, file_two_tuple, syn_dict, ARGS.tuple):
            # if string comparison determines plagiarism, then we add to PLAGIARISM_COUNTER
            global PLAGIARISM_COUNTER
            PLAGIARISM_COUNTER += 1
        # percentage determined by dividing by TOTAL_TUPLE_COUNT
        global TOTAL_TUPLE_COUNT
        TOTAL_TUPLE_COUNT += 1
    report(PLAGIARISM_COUNTER, TOTAL_TUPLE_COUNT)


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
