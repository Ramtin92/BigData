#!/usr/bin/python

import sys


def main(argv):
    word_list = []
    first_keys_list = []
    first_keys_dict = {}
    line = sys.stdin.readline()
    for line in sys.stdin:
        first_word, second_word, count = line.split('\t')
        word_list.append((first_word, second_word))
    sorted_by_first_list = sorted(word_list, key=lambda tup: tup[0])

    wordfreq = {}
    for each in sorted_by_first_list:
        pair_word = each[0] + "|" + each[1]
        wordfreq[pair_word] = wordfreq.setdefault(pair_word, 0) + 1
        first_keys_list.append(each[0])

    for each in first_keys_list:
        first_keys_dict[each] = first_keys_dict.setdefault(each, 0) + 1

    for key, value in wordfreq.items():
        first_element_in_key, second_element_in_key = key.split('|')
        print(key + '\t' + str(value / first_keys_dict[first_element_in_key]))



if __name__ == "__main__":
    main(sys.argv)


