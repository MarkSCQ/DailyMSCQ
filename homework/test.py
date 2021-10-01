
while True:
    inp = input("Hi, how can i help you?")

    if inp == "Bye":
        break
    else:
        word = 0
        index = 0

        words = inp.split()
        index = len(words)
        count = 0
        for word in words:
            for letter in word:
                count += 1
        print(count, words)
