"""
1087 BraceExpansion

You are given a string s representing a list of words. Each letter in the word has one or more options.

If there is one option, the letter is represented as is.
If there is more than one option, then curly braces delimit the options. For example, "{a,b,c}" represents options ["a", "b", "c"].
For example, if s = "a{b,c}", the first character is always 'a', but the second character can be 'b' or 'c'. The original list is ["ab", "ac"].
Return all words that can be formed in this manner, sorted in lexicographical order.

Example 1:

Input: s = "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
Example 2:

Input: s = "abcd"
Output: ["abcd"]
"""
from typing import List


class Solution:

    def expand(self, s: str) -> List[str]:
        # ! result collector
        collect = []
        # ! recursion, construct each word

        def helper(s, word):
            # ! s:string, word, current existed word
            if not s:
                # ! exit condition when s is empty
                collect.append(word)
            else:
                # ! when s is not empty

                if s[0] == "{":
                    # ! if first letter is {, then start to add letters from the next
                    # ! find the index of first } occurance
                    firstcb = s.find("}")
                    for letter in s[1:firstcb].split(","):
                        helper(s[firstcb+1:], word+letter)
                else:
                    helper(s[1:], word+s[0])
        helper(s, "")
        collect.sort()
        return collect
