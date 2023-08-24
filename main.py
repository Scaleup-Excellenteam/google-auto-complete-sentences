import pickle
import cli as cli


def main():
    # Load the PrefixTree object from the pickle file
    with open('prefix_tree.pkl', 'rb') as f:
        tree = pickle.load(f)

    # import prefix_tree as pt
    # import parse_data as pd
    #
    # tree = pt.PrefixTree()
    # filename = 'Archive/Matplotlib.txt'
    # lines = pd.parse_data(filename)
    #
    # # initialize the prefix tree
    # offset = 0
    # for line in lines:
    #     tree.insert(filename, line, offset)
    #     offset += len(line) + 1

    cli.run_cli(tree)


if __name__ == "__main__":
    main()
