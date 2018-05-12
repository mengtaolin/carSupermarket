# -*- coding:utf-8 -*-


from tool.tools import SpiderTool
from vo.carVo import AllCarKindInfo


class ServerMain():
    def __init__(self):
        self.allCarKindInfo = AllCarKindInfo();

    def startSpider(self):
        # SpiderTool.startSpider(self.allCarKindInfo);
        # SpiderTool.loadImg(self.allCarKindInfo)
        SpiderTool.startSpider1()




if __name__ == "__main__":
    serverMain = ServerMain();
    serverMain.startSpider();




