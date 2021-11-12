class pet:
    def __init(self, cate):
        self.cate = cate


class dog(pet):
    def __init(self, name, cate):
        super().__init__(cate)
        self.name = name
        print(f"Name is {self.name}")

    # ! @ classmethod
    @classmethod
    def bark():
        pass
