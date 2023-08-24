import pickle
from time import time
import logs.log as logger
import cli as cli

tree_path = 'resources/prefix_tree.pkl'

def main():
    start_time = time()
    # Load the PrefixTree object from the pickle file
    with open(tree_path, 'rb') as f:
        tree = pickle.load(f)

    finish_time = time()
    response_time = finish_time - start_time
    logger.get_logger().info(f"Time to load full tree: {response_time}")
    cli.run_cli(tree)


if __name__ == "__main__":
    main()
