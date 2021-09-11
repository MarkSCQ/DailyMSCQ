from typing import List

class Solution:
    
    def expand(self, s: str) -> List[str]:
        # ! result collector
        collect=[]
        # ! recursion, construct each word
        def helper(s,word):
            # ! s:string, word, current existed word
            if not s:
                # ! exit condition when s is empty
                collect.append(word)
            else:
                # ! when s is not empty

                if s[0]=="{":
                    # ! if first letter is {, then start to add letters from the next
                    # ! find the index of first } occurance
                    firstcb = s.find("}")
                    for letter in s[1:firstcb].split(","): 
                        helper(s[firstcb+1:],word+letter)
                else:
                    helper(s[1:],word+s[0])
        helper(s,"")
        collect.sort()
        return collect