import cli as cli
import prefix_tree as pt
import parse_data as pd

def main():

    tree = pt.PrefixTree()
    filename = 'test.txt'
    lines = pd.parse_data(filename)

    # initialize the prefix tree
    offset = 0
    for line in lines:
        tree.insert(filename, line, offset)
        offset += len(line) + 1

    # all_words = tree.get_all_sentences_with_offsets()
    # for word in all_words:
    #     print(word)
    cli.run_cli(tree)


if __name__ == "__main__":
    main()