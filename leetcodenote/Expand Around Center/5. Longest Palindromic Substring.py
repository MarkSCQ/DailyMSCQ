'''
https://leetcode.com/problems/longest-palindromic-substring/

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"

'''

'''
HOW?

1. Brute Force
    Try every possible pair and finally give out number

2. adapt a DP mind. 

    Each time, we use brute force to search the target substring, we might repeat the same process for many times
    Here is an example
    string a = 'abcdcba'
    String a is a Palindoromic string, the inner contents are also Palindoromic
    a       b       c       d       c       b       a
    |       |       |       |       |       |       |
    |       |       -----------------       |       |
    |       ----------------------------------------|
    -------------------------------------------------

    from this example. 
    cdc is repeated when checking bcdcb, abcdcda using brute force
    bcdcb is repeated when checking abcdcba using brute force

    The core mind, start from the center and extend to head and tail

3. Notice
    two different scenarios
        1. Odd length string   Example: cdc
        2. Even length string   Example: cddc
    
    SOLUTION for two scenarios:
        currentMax = max(odd_SubString_Scenario, even_SubString_Scenario)
            in which: odd_SubString_Scenario considers center i and i
                    even_SubString_Scenario considers center i and i+1
'''


def process(string):
    stringlen = len(string)
    # ! searching the range of palindromic substring
    # ! left and right is the start of searching to left(head) and right(tail)

    def isPa(left, right):
        # ! notice left could be 0; string[left]==string[right] is put as the last condition
        # ! because if the first or second condition fail, it will not go to the third condition
        # ! using this method can avoid array out of boundary error
        while left >= 0 and right < stringlen and string[left] == string[right]:
            left -= 1
            right += 1
        # ! finishing the searching and return the length
        # ! ['a','b','c','c','b','a'] len 6, if left=3,right=3
        # ! it will go through left right
        # !                     2      3
        # !                     1      4
        # !                     0      5
        # !                    -1      6
        # ! then return 6-(-1)-1=6 the final length is 6
        return right-left-1
    res = 0
    start = 0
    for i in range(stringlen):
        curr = max(isPa(i, i), isPa(i, i+1))
        if curr <= res:
            continue
        res = curr
        # ! curr-1, if the length is Even, then need to -1;
        # ! for example (6-1)//2 == (5-1)//2 == 2
        start = i - (curr-1)//2
    return len(string[start:start+res])


while True:
    try:
        string = input()
        process(string)
    except:
        break


# l = int(input())
# s = list(map(int, input().split()))
# k = int(input())
# head = Node()
