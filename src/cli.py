from time import time
import logs.log as logger
import parse_data as pd
from src import auto_complete_data as acd

WELCOME_MSG = "****************** WELCOME TO OUR SEARCH SYSTEM ******************"
GET_INPUT = "Enter a sentence (or # to restart, ~ to quit):"
QUIT_MESSAGE = "~"
RESTART_MESSAGE = "#"
MATCHES = "Matches:"
NO_MATCHES = "No matches found."
BEST_MATCHES = 5
SENTENCE = 0
OFFSET_VALUE = 0

def get_nodes(tree, sentence):
    sentence = pd.clean_sentence(sentence)
    sentence = pd.lowercase_and_remove_punctuation(sentence)

    start_time = time()
    nodes_trie = tree.find_sentences_starting_with(sentence)
    finish_time = time()
    response_time = finish_time - start_time
    logger.get_logger().info(f"Time to get response for searching '{sentence}': {response_time}")

    return nodes_trie


def display_matches(tree, sentence):
    nodes_trie = get_nodes(tree, sentence)
    nodes_trie = sorted(nodes_trie, key=lambda x: x[SENTENCE])
    nodes_trie = nodes_trie[:BEST_MATCHES]
    if not nodes_trie:
        print(NO_MATCHES)
        return
    for sentence, offsets_dict, score in nodes_trie:
        filename, offset_list = next(iter(offsets_dict.items()))
        offset_value = offset_list[OFFSET_VALUE]
        result = acd.AutoCompleteData(sentence, filename, offset_value, score)
        print(result)


def run_cli(tree):
    print(WELCOME_MSG)
    sentence = ""
    while True:
        additional_input = input(f"{GET_INPUT} {sentence}")
        sentence += additional_input

        if sentence == "":
            print("Please write a sentence.")
            continue

        if sentence.endswith(QUIT_MESSAGE):
            break

        if sentence.endswith(RESTART_MESSAGE):
            sentence = ""
            continue

        display_matches(tree, sentence)
