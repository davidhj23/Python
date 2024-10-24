class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def bark(self):
        print('bark')


class Cat(Mammal):
    def be_annoying(self):
        print('be annoying')


dog = Dog()
dog.walk()
dog.bark()

cat = Cat()
cat.walk()
cat.be_annoying()