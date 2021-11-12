while True:
    try:
        l = input()
        if isinstance(l, int):
            raise ValueError(f"raise Int Error {l}")
        if isinstance(l, str):
            raise ValueError(f"raise Int Error {l}")

    except Exception as ex:
        print(ex)
