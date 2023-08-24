import numpy as np
from collections import Counter
from functools import lru_cache


WELCOME_MSG = "****************** WELCOME TO OUR SEARCH SYSTEM ******************"
GET_INPUT = "Enter a sentence (or # to restart, ~ to quit):"
QUIT_MESSAGE = "~"
RESTART_MESSAGE = "#"
MATCHES = "Matches:"
NO_MATCHES = "No matches found."


def display_matches(tree, sentence):
    sentences = tree.get_all_sentences_with_offsets()
    words = sentence.split()

    for sent, offsets in sentences:
        sent_words = sent.split()
        for i in range(len(sent_words) - len(words) + 1):
            sub_sent_words = sent_words[i:i + len(words)]
            sub_sent = ' '.join(sub_sent_words)
            distance = levenshtein_distance(sub_sent, sentence)
            if distance <= 1:
                print(f"Sentence found (Distance {distance}): {sent}, Offsets: {offsets}")


def levenshtein_distance(s1, s2):
    # Calculate the Levenshtein distance between two strings
    m, n = len(s1), len(s2)
    dp = np.zeros((m + 1, n + 1), dtype=int)

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)

    return dp[m][n]


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

        if sentence == RESTART_MESSAGE:
            sentence = ""
            continue

        if sentence.endswith(RESTART_MESSAGE):
            sentence = ""

        display_matches(tree, sentence)
        # matches = display_matches(tree, sentence)
        # if matches:
        #     print(MATCHES)
        #     for match in matches:
        #         print(f"- {match}")
        # else:
        #     print(NO_MATCHES)
