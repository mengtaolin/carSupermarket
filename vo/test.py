# -*- coding:utf-8 -*-

class Demo():

    def __init__(self):
        self.list1 = []

    def addOne(self, str):
        self.list1.append(str)
        print id(self.list1)


if __name__ == "__main__":
    mylist = [];
    for j in range(3):
        demo = Demo();
        for i in range(10):
            demo.addOne("str" + str(i * j))
        mylist.append(demo)
    print mylist;