import sys


def get_syns(ARGS):
    syn_list = []
    try:
        with open(ARGS.syn, 'r') as f:
            for line in f:
                syn_list.append(line.rstrip('\n').split(' '))
    except IOError as e:
        print('Error in opening file...\n{}'.format(e))
        sys.exit(0)
    return syn_list

def make_syn_dict(syn_list):
    syn_dict = {}
    for subarray in syn_list:
        # every element in the subarray acts as a key, and the assoc. value is the subarray itself (list of words it
        # should be treated equal to)
        for i in subarray:
            syn_dict[i] = subarray
    return syn_dict


def get_file_data(filename):
    try:
        with open(filename, 'r') as f:
            data = f.read().replace('\n', ' ')   # strip newlines
    except IOError as e:
        print('Error in reading file...\n{}'.format(e))
        sys.exit(0)
    data = data.split(' ')     # all words into a list
    return data


def check_plagiarism(file_one_tuple, file_two_tuple, syn_dict: dict, tuple_len):

    # handle if one or the other tuple list was not constructed (in case file lengths are different)
    if len(file_one_tuple) != tuple_len or len(file_two_tuple) != tuple_len:
        return False

    # handle identical lists
    if file_one_tuple == file_two_tuple:
        return True

    # check for synonyms
    for i in range(0, len(file_one_tuple)):
        if file_one_tuple[i] != file_two_tuple[i]:   # words are not identical in same index, check if they are synonyms
            word_syns = syn_dict.get(file_one_tuple[i], None)
            if word_syns is None:                   # no synonyms exist, return False
                return False
            else:
                if file_two_tuple[i] not in word_syns:
                    return False                    # synonyms exist, but word is not a synonym, return False
    # no return false executed means all the words are the same or synonyms exist
    return True

# outputs % of similar tuples
def report(found_count, total_count):
    x = (found_count/total_count)*100
    print('Plagiarism report for this run is {}%'.format(int(x)))
    sys.exit(0)
