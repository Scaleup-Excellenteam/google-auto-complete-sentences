from collections import Counter
import Levenshtein as lev

replaced_letter_error = 5
miss_or_add_letter_error = 10
replaced_error_count = 1
miss_or_add_error_count = 2


class TrieNode:
    def __init__(self, text=''):
        self.text = text
        self.children = dict()
        self.is_end = False
        self.offset = {}


class PrefixTree:
    def __init__(self):
        self.root = TrieNode('')

    def insert(self, filename, sentence, offset):
        current = self.root
        words = sentence.split()
        for i, word in enumerate(words):
            if word not in current.children:
                prefix = ' '.join(words[:i + 1])
                current.children[word] = TrieNode(prefix)
            current = current.children[word]
            current.word = sentence  # Store the sentence in the current node
        current.is_end = True

        if filename in current.offset:
            current.offset[filename].append(offset)
        else:
            current.offset[filename] = [offset]

    def find_sentences_starting_with(self, sentence_prefix):
        """
        Returns a list of all sentences that start with the given sentence prefix,
        along with their offsets.
        """
        matched_sentences = []
        current = self.root
        word_list = sentence_prefix.split()
        score = len(sentence_prefix) * 2

        self.dfs_find(current, word_list, 0, [], matched_sentences, score)
        return matched_sentences

    def dfs_find(self, current, word_list, index, path, matched_sentences, score):
        if index == len(word_list):
            self.collect_words_with_offsets(current, ' '.join(path), matched_sentences, score)
            return

        word = word_list[index]
        for child_word in current.children:
            distance = lev.distance(word, child_word)
            if distance <= 1:
                if distance == 1 and len(word) == len(child_word):
                    score = self.fix_score(word, child_word, score, replaced_letter_error, replaced_error_count)
                else:
                    score = self.fix_score(word, child_word, score, miss_or_add_letter_error, miss_or_add_error_count)

                new_path = path + [child_word]
                self.dfs_find(current.children[child_word], word_list, index + 1, new_path, matched_sentences, score)

    def fix_score(self, word, child_word, score, error, error_count):
        for i in range(len(word)):
            if word[i] != child_word[i]:
                score -= error
                break
            if i > 5:
                continue
            error -= error_count
        return score

    def collect_words_with_offsets(self, node, current_sentence, collected_sentences, score):
        if node.is_end:
            collected_sentences.append((current_sentence, node.offset, score))
        for word, child_node in node.children.items():
            new_sentence = current_sentence + " " + word
            self.collect_words_with_offsets(child_node, new_sentence, collected_sentences, score)

    def get_all_sentences_with_offsets(self):
        collected_sentences = []
        self.collect_words_with_offsets(self.root, '', collected_sentences, 0)
        return collected_sentences
