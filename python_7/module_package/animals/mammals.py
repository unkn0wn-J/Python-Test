class Dog:
    def __init__(self,name):
        self.name = name

    def info(self):
        return f"Dog 이름: {self.name}"

dog1 = Dog("흰둥이")