"""
937. Reorder Data in Log Files
https://leetcode.com/problems/reorder-data-in-log-files/


You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.

 

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
Example 2:

Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

! python sorted(list, keys,reverse)

! The value of the key parameter should be a function (or other callable) that takes a single argument and returns a key to use for sorting purposes. 
! This technique is fast because the key function is called exactly once for each input record.

"""


def reorderLogFiles(logs):

    def get_key(log):
        # ! if split the indicator and log contents.
        # ! indecator: _id, log contents: rest
        _id, rest = log.split(" ", maxsplit=1)
        # print(_id, rest)
        # ! if rest, the log content is character, then set as (0,rest,_id)
        # ! if rest, the log content is not character, which means they are all numbers
        # ! then set as (1,), as descrobed in question "The digit-logs maintain their relative ordering."
        t = (0, rest, _id) if rest[0].isalpha() else (1, )
        # print(t)
        # print()
        return t
    return sorted(logs, key=get_key)


test = ["dig1 8 1 5 1",
        "dig1 4 1 5 1",
        "dig1 1 1 5 1",
        "let1 art can", "dig2 3 6",
        "let2 own kit dig",
        "let3 art zero"]


b = reorderLogFiles(test)

print(b)