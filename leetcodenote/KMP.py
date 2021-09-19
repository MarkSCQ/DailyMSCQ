"""
String pattern searching.


next array, pattern string. dentoes the longest common prefix and suffix of string[0:i]. The longest common prefix and suffix.
"""


def strStr(haystack, needle):
    n, h = len(needle), len(haystack)

    i, j, nxt = 1, 0, [-1]+[0]*n

    # ! constructing next array
    # ! the next array is doing a calculation of largest common string of prefix and suffix
    while i < n:
        # ! needle[i]==needle[j], j is used for prefix, i is used to search the common string
        # ! if needle[i]==needle[j], this means we have at least one character common string
        if j == -1 or needle[i] == needle[j]:
            # ! since needle[i]==needle[j], we expect the next i and j still meets this requirements
            i += 1
            j += 1
            # ! j is considered as current max prefix length
            nxt[i] = j
        else:
            # ! if needle[i]!=needle[j] or j!=-1
            # ! needle[i]!=needle[j] means fail to acquire the common string
            # ! this step has two function.
            # ! 1 initilization when not equal to -1
            # ! 2 when needle[i]!=needle[j], mismatch, then set j as the previous state
            j = nxt[j]
    i = 0
    j = 0

    print(nxt)

    # ! searching
    while i < h and j < n:
        # ! check if matching
        if j == -1 or haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            # ! if not match, starting from the previous next array value
            j = nxt[j]
    return i-j if j == n else -1


# def buildNext(pattern):
#     next = []

#     next.append(0)

#     x = 1
#     now = 0
#     while x < len(pattern):
#         if pattern[now] == pattern[x]:
#             now += 1
#             x += 1
#             next.append(now)
#         elif now:
#             now = next[now-1]
#             print("now ", now)
#         else:
#             next.append(0)
#             x += 1

#     return next


# def kSearch(text, pattern):
#     tar = 0
#     pos = 0

#     while tar<len(text) :
#         if text[tar]==pattern[pos]:
#             tar+=1
#             pos+=1
#         elif pos:
#             pos=next[pos-1]
#         else:
#             tar+=1
#         if pos==len()

haystack = "ABABDABACDABABCABAB"

needle = "ABABCABAB"


strStr(haystack, needle)
