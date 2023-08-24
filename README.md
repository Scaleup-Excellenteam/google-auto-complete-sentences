# Project Name

AutoComplete Search System, a system that provides the best suggestions of your uncompleted search query.

## Algorithms & Structures

- **Pickle Module**: We used the Pickle module to load our data structure once, save it in a folder and then load it when running our auto-complete search program. The purpose of doing so is to lower the time taken to load and parse the data each time running the program, it takes approximately ~ 2 minutes to load the data into a file, and to load the file into our executable program takes around ~ 30 seconds. The module does so by Serializing our data structure from a python object into a byte stream, which we then store in a file, then it deserializes the file into a full-on ready data structure, in other words we used only two functions, pickle.dump() & pickle.load(). 

- **Data Parsing**: read all data found in the archive, and store them in a prefix tree, where the root is the initial word of a sentence going down to the following words. For instance, we have these sentences:
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

In our case, we basically create an instance of our tree, walk through all the .txt files in the archive folder, extract each line and insert it into the tree.

- **CLI**: A user friendly CLI that loops infinetely asking the user to provide input, if a # was provided at the end, the system asks for a new string, if not, the user can complete the previous a sentence. If the user provided a '~' that means he wants to quit and exit the system.

- **Trie (prefix-tree) Data Structure**: As mentioned before, we are using a prefix tree, there are two main classes that we implemented.
First class represents each node in the tree, which consists of :

self.text = text        #  The word of a sentence we want to store in the current node.
self.children = dict()  #  A Dict that holds refernces to the child nodes of the current node. Allows quick access to child nodes using the keys of the dict.
self.is_end = False     #  A boolean variable that indicates if the current words is the last word of a sentence or not.
self.offset = {}        #  Stores the position of a word in a certain .txt file. 

Second class are the functionalities of the prefix tree, the class has 6 methods:

insert(): This method receives a sentence, its file_name and the offset of the sentence in that file. Simply, it loops through the words and insert them into the tree.
          --Runtime Complexity: O(m), where 'm' is the number of words in the sentence.

find_sentences_starting_with(): the method receives a sentence prefix, in other words the user's input. The method returns all the sentences that has the same  prefix   and their offsets
          --Runtime Complexity: O(p), where 'p' is the number of words in the provided prefix.

dfs_find(): The method firstly checks if the current node is the last word of a sentence, which also acts as a termination check, if so merge all matched words to create an original sentence and return it, if not, compute the distance of the current node and the current word we are searching for, meaning, check how much of typo mistakes were made, if the distance is 0 then the word is typed correctly by the user, if the distance is 1, there might be either an extra, replaced or a removed letter between the words. The method Does not accept words with a distance of more than 1, then recursively using DFS algorithm search of the current word.
          --Runtime Complexity: O(b^d), where 'b' is the number of branches of the current node and 'd' is the length of the query.

fix_score(): The method readjusts the score computed if a typo mistake occurred accordingly.
          --Runtime Complexity: O(min(len(word), len(child_word))), in other words the length of the shorter word.

collect_words_with_offsets(): A recursive method, that checks if the current word is the end of a sentence as a termination check, if not the function keeps looping to collect the matched sentence along with its offset and score.
          --Runtime Complexity: O(n), where 'n' is the total number of nodes in the subtree.

get_all_sentences_with_offsets(): This funciton simply returns all selected sentences and their offsets.


- **AutoComplete data structure**: The data structure we chose to use to represent the final result of a search by the user, holds these members:

completed_sentence: str  #  The completed sentence after search.
source_text: str         #  The source file of that completed sentence.
offset: int              #  The positioning of the sentence in that file.
score: int               #  The score of the search found. 


TOTAL RUNTIME COMPLEXITY OF A SINGLE SEARCH: (O n*log(n)).




## Authors:
-Yaakov Haimoff
-Anton Nahahs
-Yehuda Heller
