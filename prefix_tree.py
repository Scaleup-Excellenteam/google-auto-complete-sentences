import string
from collections import Counter


def clean_sentence(sentence):
    cleaned_sentence = ' '.join(sentence.split())
    return cleaned_sentence


def lowercase_and_remove_punctuation(sentence):
    lowercased_sentence = sentence.lower()
    translator = str.maketrans('', '', string.punctuation)
    cleaned_sentence = lowercased_sentence.translate(translator)
    return cleaned_sentence


def parse_data(file_path):
    lines = []

    with open(file_path, 'r') as file:
        for line in file:
            cleaned_line = clean_sentence(line.strip())
            cleaned_line = lowercase_and_remove_punctuation(cleaned_line)
            lines.append(cleaned_line)
    return lines


class TrieNode:
    def __init__(self, text=''):
        self.text = text
        self.children = dict()
        self.is_word = False
        self.offset = {}


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, filename, word, offset):
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i + 1]
                current.children[char] = TrieNode(prefix)
            current = current.children[char]
        current.is_word = True

        if filename in current.offset:
            current.offset[filename].append(offset)
        else:
            current.offset[filename] = [offset]

    def find(self, word):
        """
        Returns the TrieNode representing the given word if it exists
        and None otherwise.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]

        # New code, None returned implicitly if this is False
        if current.is_word:
            return current

    def starts_with(self, prefix):
        """
        Returns a list of all words beginning with the given prefix, or
        an empty list if no words begin with that prefix.
        """
        words = list()
        current = self.root
        for char in prefix:
            if char not in current.children:
                # Could also just return words since it's empty by default
                return list()
            current = current.children[char]

        # Step 2 will go here

    def collect_words_with_offsets(self, node, current_word, collected_words):
        if node.is_word:
            collected_words.append((current_word, node.offset))
        for char, child_node in node.children.items():
            self.collect_words_with_offsets(child_node, current_word + char, collected_words)

    def get_all_words_with_offsets(self):
        collected_words = []
        self.collect_words_with_offsets(self.root, '', collected_words)
        return collected_words


def main():
    tree = PrefixTree()
    filename = 'test.txt'
    # Insert words
    lines = parse_data(filename)

    offset = 0
    for line in lines:
        for word in line.split():
            tree.insert(filename, word, offset)
            offset += len(word) + 1
        offset -= 1

    all_words = tree.get_all_words_with_offsets()
    for word in all_words:
        print(word)


    # # Find words
    # word = tree.find('Provisions'.lower())
    # if word:
    #     x = Counter(word.offset[filename])
    #     print(x)
    #     # print(word.text)
    #     # print(word.offset)
    # else:
    #     print(tree.find('provisions'.lower()))
    #     print('Word not found')



if __name__ == "__main__":
    main()
