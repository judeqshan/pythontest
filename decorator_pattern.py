
#encoding=utf-8
__author__ = 'kevinlu1010@qq.com'

from abc import ABCMeta, abstractmethod


class Person():
    def __init__(self, name):
        self.name = name

    def decorator(self, component):
        self.component = component

    def show(self):
        print('%s开始穿衣' % self.name)
        self.component.show()


class Finery():
    def __init__(self):
        self.component = None

    def decorator(self, component):
        self.component = component

    __metaclass__ = ABCMeta

    @abstractmethod
    def show(self):
        if self.component:
            self.component.show()


class TShirt(Finery):
    def show(self):
        Finery.show(self)
        print("t_shirt")


class Trouser(Finery):
    def show(self):
        Finery.show(self)
        print("paints")


class Shoe(Finery):
    def show(self):
        Finery.show(self)
        print("shoe")


class Tie(Finery):
    def show(self):
        Finery.show(self)
        print("tie")


if __name__ == '__main__':
    person = Person('kevin')
    tshirt = TShirt()
    trouser = Trouser()
    shoe = Shoe()
    tie = Tie()

    trouser.decorator(tshirt)
    shoe.decorator(trouser)
    tie.decorator(shoe)
    person.decorator(tie)
    person.show()