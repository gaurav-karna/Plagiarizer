import sys


def get_syns(ARGS):
    syn_list = []
    with open(ARGS.syn, 'r') as f:
        for line in f:
            syn_list.append(line.rstrip('\n').split(' '))

    return syn_list

def make_syn_dict(syn_list):
    syn_dict = {}
    for subarray in syn_list:
        # every element in the subarray acts as a key, and the assoc. value is the subarray itself (list of words it
        # should be treated equal to)
        for i in subarray:
            syn_dict[i] = subarray
    return syn_dict
