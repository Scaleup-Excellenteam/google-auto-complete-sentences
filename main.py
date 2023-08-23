import pickle
import cli as cli


def main():
    # Load the PrefixTree object from the pickle file
    with open('prefix_tree.pkl', 'rb') as f:
        tree = pickle.load(f)

    cli.run_cli(tree)


if __name__ == "__main__":
    main()
