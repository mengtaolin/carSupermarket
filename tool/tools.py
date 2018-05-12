# -*- coding:utf-8 -*-

from vo.carVo import CarInfo, CarKindInfo, CarYearInfo, AllCarKindInfo, CarSubKindInfo
import urllib.request
import re
import os


class SpiderTool():
    @staticmethod
    def getHtmlByUrl(url):
        req = urllib.request.Request(url, headers={
            'Connection': 'Keep-Alive',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        })
        oper = urllib.request.urlopen(req)
        data = oper.read()
        html = data.decode('gbk').encode('utf-8')
        return html

    @staticmethod
    def testGetHtml(url):
        req = urllib.request.Request(url, headers={
            'Connection': 'Keep-Alive',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        })
        oper = urllib.request.urlopen(req)
        data = oper.read()
        reg = re.compile(r'position (.*?):')
        html = "";
        try:
            html = data.decode('gb2312').encode('utf-8');
        except UnicodeDecodeError as err:
            errStr = str(err);
            position = int(re.findall(reg, errStr)[0])
            data1 = data[0:position];
            html = html + str(data1.decode('gb2312').encode('utf-8'));
            try:
                tmp = data[position:]
                tmp = tmp.decode('utf-8')
            except UnicodeDecodeError as err:
                position = int(re.findall(reg, errStr)[0])
                tmp1 = tmp[position:];
                html = html + str(tmp[0:position]) + str(tmp1.decode('gb2312').encode('utf-8'));
        print(html)


    @staticmethod
    def loadImg(allCarKindInfo):
        allCarKindInfoList = allCarKindInfo.carKindInfoList;
        basePath = 'D:\\workspace\\carSupermarket\\images';

        for carKindInfo in allCarKindInfoList:
            url = carKindInfo.imageUrl;
            targetPath = basePath + "\\" + carKindInfo.letter;
            isExists = os.path.exists(targetPath)
            if not isExists:
                os.makedirs(targetPath)
            urllib.urlretrieve("http://" + url, targetPath + "\\%s.jpg" %carKindInfo.id)
            # response = requests.get("http://" + url, stream=True)
            # path = os.path.join(targetPath, carKindInfo.id + '.jpg')
            # with open(path, 'wb') as fw:
            #     fw.write(response.content)

    @staticmethod
    def startSpider1():
        # html = SpiderTool.getHtmlByUrl("https://www.autohome.com.cn/grade/carhtml/A.html")
        SpiderTool.testGetHtml("https://car.autohome.com.cn/pic/series/692.html#pvareaid=103448")

    @staticmethod
    def test(html):
        reg = re.compile(r'<li id="(.*?)">.*?<h4>.*?<a href="//.*?">(.*?)</a>.*?</h4>(.*?)</li>', re.S);
        carKindNameList = re.findall(reg, html);
        print(carKindNameList);

    @staticmethod
    def startSpider(allCarKindInfo):
        loadList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U", "V", "W", "X", "Y", "Z"]
        len1 = len(loadList)
        for i in loadList:
            html = SpiderTool.getHtmlByUrl("https://www.autohome.com.cn/grade/carhtml/" + i + ".html")
            SpiderTool.getCarKind(html, i, allCarKindInfo)

    @staticmethod
    def getCarKind(html, letter, allCarKindInfo):

        regAllKind = re.compile(
            r'<dt><a href=".*?"><img width="50" height="50" src="//(.*?)"></a><div><a href=".*?">(.*?)</a></div></dt>')
        regSubHtml = re.compile(r'<dd>(.*?)</dd>', re.S);
        regSubKind = re.compile(r'<div class="h3-tit">(.*?)</div>(.*?)</ul>', re.S);
        regCar = re.compile(r'<li id="(.*?)">.*?<h4>.*?<a href="//.*?">(.*?)</a>.*?</h4>(.*?)</li>', re.S)
        regPrice = re.compile(r'<a class="red" .*?>(.*?)</a>');
        regPublicPraise = re.compile(r'<a href="//(.*?)">口碑</a></div>');
        regPics = re.compile(r'<a id=".*?" href="//(.*?)">图库</a>')
        carKindNameList = re.findall(regAllKind, html)
        subHtmlList = re.findall(regSubHtml, html)

        index = 0;
        for carKindItem in carKindNameList:
            carKindInfo = CarKindInfo();
            carKindInfo.id = letter + "_" + str(index);
            carKindInfo.letter = letter;
            carKindInfo.setDatas(carKindItem)
            allCarKindInfo.addCarKindInfo(letter, carKindInfo);
            subHtml = subHtmlList[index]
            subKindList = re.findall(regSubKind, subHtml);
            subIndex = 0;
            for subItem in subKindList:
                carSubKindInfo = CarSubKindInfo();
                carSubKindInfo.id = carKindInfo.id + "_" + str(subIndex);
                carSubKindInfo.name = subItem[0];
                carList = re.findall(regCar, subItem[1])
                for car in carList:
                    carInfo = CarInfo();
                    carInfo.id = carSubKindInfo.id + "_" + car[0];
                    carInfo.name = car[1];
                    carSubKindInfo.addCarInfo(carInfo=carInfo)
                    detailHtml = car[2];
                    price = re.findall(regPrice, detailHtml);
                    if len(price) == 0:
                        carInfo.priceRange = "暂无报价"
                    else:
                        carInfo.priceRange = price[0];
                    publicPraise = re.findall(regPublicPraise, detailHtml);
                    carInfo.publicPraiseUrl = publicPraise[0];
                    carInfo.imageUrl = re.findall(regPics, detailHtml)[0];
                    SpiderTool.spiderImgsHtml(carInfo);
                    # SpiderTool.spiderPublicPraiseHtml(carInfo)

                carKindInfo.addCarSubKindInfo(carSubKindInfo=carSubKindInfo)
                subIndex = subIndex + 1;

            index = index + 1;

    @staticmethod
    def spiderImgsHtml(carInfo):
        html = SpiderTool.getHtmlByUrl("https://" + carInfo.imageUrl);
        # print html;
        print(html);

    @staticmethod
    def spiderPublicPraiseHtml(carInfo):
        html = SpiderTool.getHtmlByUrl(carInfo.publicPraiseUrl);
        # print html;
        print(html);

    @staticmethod
    def getCarInfo(html):
        pass;

    @staticmethod
    def getCarYear(html):
        pass;
