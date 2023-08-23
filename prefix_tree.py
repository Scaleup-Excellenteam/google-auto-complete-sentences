from collections import Counter

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

    def find(self, sentence):
        """
        Returns the TrieNode representing the given sentence if it exists
        and None otherwise.
        """
        current = self.root
        words = sentence.split()
        for word in words:
            if word not in current.children:
                return None
            current = current.children[word]

        # New code, None returned implicitly if this is False
        if current.is_end:
            return current

    def starts_with(self, prefix):
        """
        Returns a list of all sentences beginning with the given prefix, or
        an empty list if no sentences begin with that prefix.
        """
        sentences = list()
        current = self.root
        words = prefix.split()
        for word in words:
            if word not in current.children:
                return list()
            current = current.children[word]

        # New code for step 2
        self.collect_words_with_offsets(current, prefix, sentences)

        return sentences

    def collect_words_with_offsets(self, node, current_sentence, collected_sentences):
        if node.is_end:
            collected_sentences.append((current_sentence, node.offset))
        for word, child_node in node.children.items():
            new_sentence = current_sentence + " " + word
            self.collect_words_with_offsets(child_node, new_sentence, collected_sentences)

    def get_all_sentences_with_offsets(self):
        collected_sentences = []
        self.collect_words_with_offsets(self.root, '', collected_sentences)
        return collected_sentences

