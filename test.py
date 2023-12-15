class Ko:
    def method1(self, name):
        print(name)

    def __init__(self, name):
        print(name)
        self.name = name


class Ko2(Ko): pass

class Ko3(Ko2):
    def __new__(cls, *args, **kwargs):
        return 'hello world'

print(Ko('Nikita'), Ko3('Nikita'))