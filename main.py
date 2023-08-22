import pandas as pd
import string


def clean_sentence(sentence):
    # Clean up sentences by removing duplicate spaces
    cleaned_sentence = ' '.join(sentence.split())
    return cleaned_sentence


def lowercase_and_remove_punctuation(sentence):
    # Convert the sentence to lowercase
    lowercased_sentence = sentence.lower()

    # Remove punctuation using translation table
    translator = str.maketrans('', '', string.punctuation)
    cleaned_sentence = lowercased_sentence.translate(translator)

    return cleaned_sentence


def parse_data(file_path):
    # Read the text file and split into sentences
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Clean up sentences and create a DataFrame
    cleaned_lines = [clean_sentence(line.strip()) for line in lines]
    df = pd.DataFrame({'sentence': cleaned_lines})

    # Apply lowercase and remove punctuation
    df['sentence'] = df['sentence'].apply(lowercase_and_remove_punctuation)

    return df


if __name__ == "__main__":
    file_path = 'textFile.txt'
    parsed_df = parse_data(file_path)
    print(parsed_df)
