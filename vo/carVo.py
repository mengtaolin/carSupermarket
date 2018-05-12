# -*- coding:utf-8 -*-


class AllCarKindInfo():
    def __init__(self):
        self.carKindInfoList = [];
        self.carKindInfoDic = {};

    def addCarKindInfo(self, letter, carKindInfo):
        self.carKindInfoList.append(carKindInfo)
        if self.carKindInfoDic.has_key(letter) == False:
            self.carKindInfoDic[letter] = {};
        self.carKindInfoDic[letter][carKindInfo.id] = carKindInfo

    def getCarKindInfoById(self, letter, id):
        if self.carKindInfoDic.has_key(letter) and self.carKindInfoDic[letter].has_key(id):
            return self.carKindInfoDic[letter][id];
        else:
            return


class CarKindInfo():
    def __init__(self):
        self.id = "";
        self.carSubKindInfoList = [];
        self.imageUrl = "";
        self.kindName = "";
        self.letter = "";

    def addCarSubKindInfo(self, carSubKindInfo):
        self.carSubKindInfoList.append(carSubKindInfo);

    def setDatas(self, infoItem):
        self.imageUrl = infoItem[0]
        self.kindName = infoItem[1]
        # print self.kindName
        print(self.kindName)


class CarSubKindInfo():
    carInfoList = []
    def __init__(self):
        self.carInfoList = [];
        self.id = "";
        self.name = "";
        self.imageUrl = "";

    def addCarInfo(self, carInfo):
        self.carInfoList.append(carInfo);

    def getCarInfo(self):
        return self.carInfoList;

    def setDatas(self, datas):
        pass


class CarInfo():
    def __init__(self):
        self.id = "";#存储该车的ID
        self.name = "";#存储该车的名字
        self.imageUrl = "";#存储该车的图片
        self.carYearInfoList = [];
        self.priceRange = "";
        self.picsUrl = "";
        self.publicPraiseUrl = "";

    def addCarYearInfo(self, carYearInfo):
        self.carYearInfoList.append(carYearInfo)

    def getCarYearInfo(self):
        return self.carYearInfoList;

    def setDatas(self, id, name, imageUrl):
        self.id = id;
        self.name = name;
        self.imageUrl = imageUrl



class CarYearInfo():
    def __init__(self):
        self.year = 0;
        self.price = "";
        self.fuelConsumption = 0.0;
        self.fuelConsumptionNum = 0;

    """设置该车年份对应销售类型的汽车数据，以后想加什么就加什么"""
    def setDatas(self,year, price, fuelConsumption, fuelConsumptionNum):
        self.year = year;
        self.price = price;
        self.fuelConsumption = fuelConsumption;
        self.fuelConsumptionNum = fuelConsumptionNum;

