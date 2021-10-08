"""
https://leetcode.com/problems/implement-trie-prefix-tree/

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
"""


class Trie:

    def __init__(self):
        # ! using dictionary to store prefix character
        # ! using # to mark the word is ended
        self.root = {}

    def insert(self, word):
        # ! p is the pointer
        p = self.root
        # ! iterate the word and insert the character
        for i in word:
            if i not in p:
                p[i] = {}
            # ! if the character exists, then update the pointer
            p = p[i]
        # ! if word is finished, then using # to mark the finished state
        p['#'] = True

    def find(self, prefix):
        p = self.root
        # ! iterate the prefix
        for c in prefix:
            # ! if character not existes return None, not found
            if c not in p:
                return None
            p = p[c]
        # ! found, return the new pointer p = { character:{},'#':True }
        return p

    def search(self, word):
        # ! call find, using find prefix to implement the search
        node = self.find(word)
        # ! if we find the word return True, else return False
        return node is not None and '#' in node

    def startsWith(self, prefix):
        # ! using find to implement this functionality
        return self.find(prefix) is not None
