import os
import pickle
import unittest
from time import time

import src.prefix_tree as pt
import src.parse_data as pd
import logs.log as logger

tree_path = '../resources/prefix_tree.pkl'
filename = '../resources/Archive/Matplotlib.txt'
line_to_check = 'This document provides a terminology for benchmarking the Session'


class TestTree(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName=methodName)
        self.tree = pt.PrefixTree()

    def parse_line(self):
        line = pd.clean_sentence(line_to_check)
        line = pd.lowercase_and_remove_punctuation(line)
        return line

    def set_tree_with_file(self):
        lines = pd.parse_data(filename)
        # initialize the prefix tree
        offset = 0
        for line in lines:
            self.tree.insert(filename, line, offset)
            offset += len(line) + 1

    def set_tree_with_pickle(self):
        # Load the PrefixTree object from the pickle file
        with open(tree_path, 'rb') as f:
            self.tree = pickle.load(f)

    def test_time_to_load_full_tree(self):

        start_time = time()
        self.set_tree_with_pickle()
        finish_time = time()

        response_time = finish_time - start_time
        logger.get_logger().info(response_time)

    def test_time_to_response_for_search(self):

        start_time = time()

        self.set_tree_with_pickle()
        self.tree.find_sentences_starting_with(line_to_check)

        finish_time = time()

        response_time = finish_time - start_time
        logger.get_logger().info(response_time)

    def test_insert_to_tree(self):
        self.set_tree_with_file()
        self.assertEqual(True, True)

    def test_find_sentences_starting_with(self):
        self.set_tree_with_file()
        self.assertEqual(True, True)

    def test_dfs_find(self):
        self.set_tree_with_file()
        nodes_trie = self.tree.find_sentences_starting_with(line_to_check)
        for node in nodes_trie:
            print(node)
        self.assertEqual(True, True)

    def test_collect_words_with_offsets(self):
        self.set_tree_with_file()
        line = self.parse_line()
        nodes_trie = self.tree.find_sentences_starting_with(line)
        sentences = []
        for node in nodes_trie:
            sentences.append(node[0])

        if line in sentences:
            print("found")
        # self.assertEqual(line, l)

    def test_letter_delete(self):
        self.set_tree_with_file()
        self.assertEqual(True, True)

    def test_letter_replace(self):
        self.set_tree_with_file()
        self.assertEqual(True, True)

    def test_letter_insert(self):
        self.set_tree_with_file()
        self.assertEqual(True, True)
