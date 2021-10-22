class Dog:
    def __init__(self):
        self.bark()


"""
 Traceback (most recent call last):
  File ".\testclass.py", line 6, in <module>
    d = Dog()
  File ".\testclass.py", line 3, in __init__
    self.bark()
AttributeError: 'Dog' object has no attribute 'bark'
"""


d = Dog()
