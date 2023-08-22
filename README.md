# Project Name

AutoComplete Search System, a system that provides the best suggestions of your uncompleted search query.

## Algorithms & Structures

- **Trie (Prefix-tree) Data Structure**: read all data found in the archive, and store them in a prefix tree, where the root is the initial word of a sentence going down to the following words. For instance, we have these sentences:
-This is a dog
-This is a cat
-This is not a cow
-This guy

the tree would look like:
                This 
                /  \
              is   guy
             / \
            a   not
           / \    \
        cat  dog   a

- **CLI**: a user friendly CLI that loops infinetely asking the user to provide input, if a # was provided at the end, the system asks for a new string, if not, the user can complete the previous a sentence. If the user provided a '~' that means he wants to quit and exit the system.




## Detailed Code Flow

*Start by detailing how you've set up your main data structures. E.g., "We begin by collecting fruit prices from various sources." Then, explain the core logic or algorithm. E.g., "Next, we apply the Example Algorithm to identify price spikes." Conclude with any post-processing or output generation. E.g., "Finally, we visualize the price trends on a graph."*

**Hint**: This section is just a placeholder example of fruit prices. Replace it with a clear and detailed flow of your actual project's logic, algorithms, and processe
