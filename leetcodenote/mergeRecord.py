while True:
    try:
        n = int(input())
        data = {}

        for i in range(n):
            record = input().split(" ")
            r1, r2 = int(record[0]), int(record[-1])
            if r1 not in data:
                data[r1] = r2
            else:
                data[r1] += r2
        print(data)

        for key in sorted(data.keys()):
            print(key, data[key])
    except:
        break
