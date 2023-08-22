WELCOME_MSG = "****************** WELCOME TO OUR SEARCH SYSTEM ******************"
GET_INPUT = "Enter a sentence (or # to restart, ~ to quit):"
QUIT_MESSAGE = "~"
RESTART_MESSAGE = "#"
MATCHES = "Matches:"
NO_MATCHES = "No matches found."


def display_matches(sentence):
    return ["damn", "this", "is", "working", "well!"]


def run_CLI():
    print(WELCOME_MSG)
    sentence = ""
    while True:
        additional_input = input(f"{GET_INPUT} {sentence}")
        sentence += additional_input

        if sentence.endswith(QUIT_MESSAGE):
            break

        if sentence.endswith(RESTART_MESSAGE):
            sentence = ""

        matches = display_matches(sentence)
        if matches:
            print(MATCHES)
            for match in matches:
                print(f"- {match}")
        else:
            print(NO_MATCHES)


def main():
    run_CLI()


if __name__ == "__main__":
    main()
