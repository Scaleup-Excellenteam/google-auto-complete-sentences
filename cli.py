import parse_data as pd
import auto_complete_data as acd

WELCOME_MSG = "****************** WELCOME TO OUR SEARCH SYSTEM ******************"
GET_INPUT = "Enter a sentence (or # to restart, ~ to quit):"
QUIT_MESSAGE = "~"
RESTART_MESSAGE = "#"
MATCHES = "Matches:"
NO_MATCHES = "No matches found."

def get_sentences(tree, sentence):
    sentence = pd.clean_sentence(sentence)
    sentence = pd.lowercase_and_remove_punctuation(sentence)
    sentences = tree.find_sentences_starting_with(sentence)
    return sentences


def display_matches(tree, sentence):
    sentences = get_sentences(tree, sentence)
    sentences = sorted(sentences, key=lambda x: len(x[0]))
    sentences = sentences[:5]
    if not sentences:
        print(NO_MATCHES)
        return
    for sentence, offsets_dict in sentences:
        filename, offset_list = next(iter(offsets_dict.items()))
        offset_value = offset_list[0]
        result = acd.AutoCompleteData(sentence, filename, offset_value, 0)
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
