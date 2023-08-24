import string


def clean_sentence(sentence):
    cleaned_sentence = ' '.join(sentence.split())
    return cleaned_sentence


def lowercase_and_remove_punctuation(sentence):
    lowercase_sentence = sentence.lower()
    translator = str.maketrans('', '', string.punctuation)
    cleaned_sentence = lowercase_sentence.translate(translator)
    return cleaned_sentence


def parse_data(file_path):
    lines = []

    with open(file_path, 'r') as file:
        for line in file:
            cleaned_line = clean_sentence(line.strip())
            cleaned_line = lowercase_and_remove_punctuation(cleaned_line)
            lines.append(cleaned_line)
    return lines