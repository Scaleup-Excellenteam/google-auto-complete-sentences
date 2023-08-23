WELCOME_MSG = "****************** WELCOME TO OUR SEARCH SYSTEM ******************"
GET_INPUT = "Enter a sentence (or # to restart, ~ to quit):"
QUIT_MESSAGE = "~"
RESTART_MESSAGE = "#"
MATCHES = "Matches:"
NO_MATCHES = "No matches found."


def display_matches(tree, sentence):
    sentences = tree.find_sentences_starting_with(sentence)
    if not sentences:
        print(NO_MATCHES)
        return
    for sentence, offset in sentences:
        print(f'Sentence found: "{sentence}" , Offsets: {offset}')


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
