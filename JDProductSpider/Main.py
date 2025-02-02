import re
import requests
import webbrowser
from time import sleep
from getpass import getpass
from threading import Thread
from selenium import webdriver


class MainRequest:

    def view(self):
        while True:
            print("1.重新获取cookies\n2.搜索关键字\n3.打开对应序号的商品页面")
            try:
                num = int(input())
                if num == 1:
                    self.getCoockies()
                if num == 2:
                    self.startRequest()
                if num == 3:
                    self.gotoWebsite()
                else:
                    pass
            except:
                print("在搜索时遇到错误")
    #建立关键词检索
    def startRequest(self):
        self.cookies = self.ReadCookies()
        keyWord = input("请输入关键词：")
        self.maxPage = input("需要爬取的最大页数[100]：")
        self.spiderIntroduction = input("是否爬取商品简介[|yes|no]:")
        self.url = f"https://search.jd.com/Search?keyword={keyWord}"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
        try:
            print("开始请求")
            self.outputString={}
            self.productionList = []
            self.totalProduct=0
            self.wrong=0
            for i in range(int(self.maxPage)):
                self.productionList.append([])
            introduction = False
            if self.maxPage.isdigit():
                self.maxPage = int(self.maxPage)
            else:
                self.maxPage = 100
            if self.spiderIntroduction == "" or self.spiderIntroduction == "yes":
                introduction = True
            for i in range(1, self.maxPage+1):
                num = 30*(i-1)
                Thread(target=self.searchSpider, args=(
                    i, num, introduction)).start()
                if introduction>5:
                    sleep(0.6)
                elif introduction>10:
                    sleep(1.5)
                sleep(0.05)
        except:
            print("在搜索时遇到错误")


    #获取关键词每页的结果
    def searchSpider(self, page, num, introduction):
        url = self.url+f"&page={page}"
        webPage = requests.get(url, cookies=self.cookies,
                               headers=self.headers).text
        listPage=page-1
        self.infoExtract(webPage, num, listPage)
        while 1:
            for i in self.productionList:
                try:
                    if len(i[0])>1:
                        break
                    sleep(0.5)
                except:
                    pass
            break

        allInString=""
        getInfo=self.productionList[listPage]
        if introduction:
            self.batchExtract(getInfo[2],page)
        for i in range(len(getInfo[0])):
            if introduction:
                list = [getInfo[0][i], getInfo[1][i], getInfo[2]
                            [i], getInfo[3][i], getInfo[4][i], self.introductionDict[i+1]]
            else:
                list = [getInfo[0][i], getInfo[1][i], getInfo[2]
                            [i], getInfo[3][i], getInfo[4][i]]
            allInString+=str(list)+"\n"
        self.writeToFile(self.productionList[listPage][0][0],allInString)
            
        
    def writeToFile(self,page,string):
        self.outputString[page]=string
        if len(self.outputString)==int(self.maxPage):
            with open("spider.txt", "at+", encoding="utf-8") as file:
                for i in range(1,int(self.maxPage)+1):
                    file.write(self.outputString[i])
            print("完成！")
            file.close()
    #批量提取商品信息
    def batchExtract(self, urlList,page):
        self.introductionDict = {}
        tick = 30*(page-1)
        for i in urlList:
            tick += 1
            Thread(target=self.getProductInfoExtract,
                   args=(i[0], tick,)).start()
            sleep(0.1)
        while 1:
            completion=len(self.introductionDict)/self.totalProduct*100
            print(" "*100,end="\r")
            print("\033[31m"+"-"*int(completion//5)+"\033[m"+" %-0.3s" % (completion),end="\r")
            if len(self.introductionDict) == self.totalProduct:
                return
            sleep(0.5)
    #提取商品信息
    def getProductInfoExtract(self, url, tag):
        # TODO:分离线程之间的冲突
        webPage = requests.get(url, cookies=self.cookies,
                               headers=self.headers).text
        main = re.findall(
            '<div class="ETab.*?<ul class="parameter2 p-parameter-list">(.*?)<p class="more-par">', webPage, re.S)
        read = re.findall('<li.*?>(.*?)</li>', "".join(main), re.S)
        intrduction = " ".join(read)
        #if intrduction=="":
        #    self.wrong+=1 
        #if self.wrong>=10:
        #    print("无法获取商品信息，请检查cookies")
        for _ in range(20):
            intrductionFilter = re.findall(
                '<[^>]*>', intrduction, re.S)
            if intrductionFilter:
                read = intrduction.replace(
                    intrductionFilter[0], "")
            else:
                break
        self.introductionDict[tag]=read
    #提取商品
    def infoExtract(self, webPage, num, page):
        productList = [[], [], [], [], [], []]
        mainContent = re.findall(
            '<div id="J_goodsList(.*?)<span class="clr"></span>', webPage, re.S)
        allProduct = re.findall('<li.*?>(.*?)</li>',
                                "".join(mainContent), re.S)
        for eachProduct in allProduct:
            num += 1
            productURL = re.findall(
                '<div class="p-img">.*?<a.*?href="(.*?)"', eachProduct, re.S)
            productPicture = re.findall(
                '<div class="p-img">.*?<img.*?data-lazy-img="(.*?)" />', eachProduct, re.S)
            productName = re.findall(
                '<div class="p-name p-name-type-2">.*?<em>(.*?)</em>', eachProduct, re.S)
            productPrice = re.findall(
                '<div class="p-price">.*?<i.*?>(.*?)</i>.*?</strong>', eachProduct, re.S)
            productList.append(num)
            productList[0].append(page+1)
            productList[1].append(num)
            if productURL:
                productURL[0] = "https:"+productURL[0]
                productList[2].append(productURL)
            if productPicture:
                productPicture[0] = "https:"+productPicture[0]
                productList[3].append(productPicture)
            if productName:
                productName = productName[0]
                for _ in range(10):
                    productNameFilter = re.findall(
                        '<[^>]*>', productName, re.S)
                    if productNameFilter:
                        productName = productName.replace(
                            productNameFilter[0], "")
                    else:
                        break
                if "\n" in productName:
                    productName = productName[productName.index("\n")+1:]
                productList[4].append("".join(productName))
            if productPrice:
                productList[5].append(productPrice)
        self.productionList[page]=productList
        self.totalProduct+=len(productList[0])

    def ReadCookies(self):
        try:
            cookies = {}
            with open("cookies.txt", "rt") as file:
                read = file.read()
                read = eval(read)
                file.close()
            if type(read) is list:
                for i in read:
                    cookies[i['name']] = i['value']
                print("Cookies加载完毕")
                return cookies
            else:
                raise ()
        except:
            print("未找到Cookies，即将重新登录")
            self.getCoockies()
            self.ReadCookies()

    def getCoockies(self):
        try:
            webPage = webdriver.Chrome()
            url = "https://passport.jd.com/new/login.aspx"
            webPage.minimize_window()
            webPage.get(url)
            webPage.implicitly_wait(5)
            webPage.find_element(
                "xpath", '//*[@id="loginname"]').send_keys(input("请输入京东账户："))
            webPage.find_element(
                "xpath", '//*[@id="nloginpwd"]').send_keys(getpass("请输入密码："))
            webPage.maximize_window()
            webPage.find_element("xpath", '//*[@id="loginsubmit"]').click()
            webPage.implicitly_wait(10)
            try:
                assert webPage.find_element(
                    "xpath", '//*[@id="J_logo_extend"]/img')
                webPage.minimize_window()
                cookies = webPage.get_cookies()
                return self.writeCookies(cookies)
            except:
                webPage.minimize_window()
                if "认证" in webPage.title:
                    webPage.find_element(
                        "xpath", '//*[@id="app"]/div/div/div/div[2]/button').click()
                    webPage.find_element(
                        "xpath", '/html/body/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div/div/div[1]/button').click()
                    webPage.find_element(
                        "xpath", '/html/body/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/input').send_keys(input("请输入验证码："))
                    webPage.find_element(
                        "xpath", '/html/body/div[2]/div[1]/div[2]/div/div[3]/button').click()
                    sleep(4)
                    cookies = webPage.get_cookies()
                    self.writeCookies(cookies)
        except Exception as err:
            print("在获取cookies时遇到错误", err)

    def writeCookies(self, cookies):
        with open("cookies.txt", "wt+") as file:
            file.write(str(cookies))
        file.close()
        print("已取得cookies！")

    def gotoWebsite(self):
        try:
            num = input("请输入商品序号：")
            length = len(num)
            start = 0
            if length == 3:
                start = int(num[0]+"00")-100
            elif length == 4:
                start = int(num[0]+"000")-200
            elif length == 4:
                start = int(num[0]+"0000")-500
            elif length == 5:
                start = int(num[0]+"00000")-600
            with open("spider.txt", "rt", encoding="utf-8") as file:
                read = file.readlines()
                tick = 0
                while True:
                    try:
                        if start+tick > len(read):
                            print("商品序号超过商品数量")
                            return
                        every = read[start+tick].rstrip("\n")
                        tick += 1
                        each = eval(every)
                        if type(each) == list and len(each) > 1 and each[1] == int(num):
                            print(each)
                            Thread(target=webbrowser.open,
                                   args=(each[2])).start()
                            return
                    except:
                        pass
        except:
            print("读取时遇到错误")
        file.close()


if "__main__" == __name__:
    MainRequest().view()
