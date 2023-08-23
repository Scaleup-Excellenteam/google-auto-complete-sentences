import pickle
import prefix_tree as pt
import parse_data as pd

def build_and_save_tree():
    tree = pt.PrefixTree()
    filename = 'test.txt'
    lines = pd.parse_data(filename)

    # Initialize the prefix tree
    offset = 0
    for line in lines:
        tree.insert(filename, line, offset)
        offset += len(line) + 1

    # Save the PrefixTree object using pickle
    with open('prefix_tree.pkl', 'wb') as f:
        pickle.dump(tree, f)

if __name__ == "__main__":
    build_and_save_tree()
