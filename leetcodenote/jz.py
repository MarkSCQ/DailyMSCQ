nums = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}
while True:
    try:
        numstr = input()
        numstr = list(numstr.replace("0x", ""))

        real = 0
        idx = len(numstr)-1
        mi = 0

        while idx >= 0:
            real+=nums[numstr[idx]]*16**mi
            mi+=1
            idx -= 1
    except:
        break
