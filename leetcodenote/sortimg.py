while True:
    try:

        s = list(input())
        print("s ", s)
        nums = []
        uppers = []
        lowers = []
        for i in range(len(s)):
            if s[i].isdigit():
                nums.append(s[i])
            if s[i].isupper():
                uppers.append(s[i])
            if s[i].islower():
                lowers.append(s[i])
        nums.sort()
        uppers.sort()
        lowers.sort()
        s = nums+uppers+lowers
        print("".join(s))
    except:
        break
