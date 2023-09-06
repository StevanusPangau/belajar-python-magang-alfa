class Computer:
    # Constructor
    def __init__(self, name=''):
        self.name = name

    def __str__(self) -> str:
        print(f"Computer {self.name}")

    def say_hello(self):
        print("i'm computer, called : ", self.name)
