def p212_752():
    import pymysql
    import os  # 导入os模块，如其名，用以控制系统接口，主要是文件管理相关的接口

    class scoreDB:

        def open(self):  # 定义函数用以连接并读取数据库
            self.connect = connect = pymysql.connect(
                host="10.1.85.172", port=3306, user="root", passwd="123456", db="mydb", charset="utf8")
            self.cursor = self.connect.cursor(pymysql.cursors.DictCursor)
            try:
                sql = """
                        create table score
                        (
                            Num varchar(16) primary key,
                            Name varchar(16),
                            Chinese float,
                            Math float,
                            English float
                        )
                      """
                self.cursor.execute(sql)
            except:
                pass

        def close(self):  # 定义函数用以提交并关闭数据库
            self.connect.commit()
            self.connect.close()

        def show(self):  # 定义函数用以显示数据库及数据库内容
            try:
                self.cursor.execute("select * from score")
                print("%-16s%-16s%-8s%-8s%-8s" %
                      ("学号", "姓名", "语文", "数学", "英语"))
                rows = self.cursor.fetchall()
                for row in rows:
                    print("%-16s%-16s%-8.0f%-8.0f%-8.0f" %
                          (row["Num"], row["Name"], row["Chinese"], row["Math"], row["English"]))
            except Exception as err:
                print(err)

        def __insert(self, Num, Name, Chinese, Math, English):
            try:
                sql = "insert into score values(%s,%s,%s,%s,%s)"
                self.cursor.execute(sql, (Num, Name, Chinese, Math, English))
                print(f"添加了{self.cursor.rowcount}行")
            except Exception as err:
                print(err)

        def __update(self, Num, Name, Chinese, Math, English):
            try:
                sql = "update score set Name=%s,Chinese=%s,Math=%s,English=%s where Num=%s"
                self.cursor.execute(sql, (Name, Chinese, Math, English, Num))
                print(f"更改了{self.cursor.rowcount}行")
            except Exception as err:
                print(err)

        def __delete(self, Num):
            try:
                sql = "delete from score where Num=%s"
                self.cursor.execute(sql, (Num,))
                print(f"删除了{self.cursor.rowcount}行")
            except Exception as err:
                print(err)

        def __loadCheck(self, score):  # 定义函数用以实现从外部导入数据时对数据进行校验
            checked = 0
            try:
                checked = float(score)
                if checked < 0 or checked > 100:
                    checked = 0
            except:
                pass
            return checked

        def __scoreCheck(self, message):  # 定义函数用以校验输入的分数
            while True:
                score = input(message)
                try:
                    score = float(score)
                    if score >= 0 and score <= 100:
                        break
                except Exception as err:
                    print(err)
            return score

        def __infoCheck(self):  # 定义函数用以输入并检查数据正确性
            self.Num = input("学号：").strip()
            self.Name = input("姓名：").strip()
            if self.Num != "" and self.Name != "":
                self.Chinese = self.__scoreCheck("语文：")
                self.Math = self.__scoreCheck("数学：")
                self.English = self.__scoreCheck("英语：")
                self.check = True
                return self.Num, self.Name, self.Chinese, self.Math, self.English
            else:
                print("学号与姓名需填写")
                self.check = False

        def insert(self):  # 定义函数用以向插入函数传入数据
            self.__infoCheck()  # 执行接收数据
            if self.check:
                Num, Name, Chinese, Math, English = self.Num, self.Name, self.Chinese, self.Math, self.English
                self.__insert(Num, Name, Chinese, Math,
                              English)  # 将获得的数据插入至数据库

        def update(self):
            self.__infoCheck()
            if self.check:
                Num, Name, Chinese, Math, English = self.Num, self.Name, self.Chinese, self.Math, self.English
                self.__update(Num, Name, Chinese, Math, English)

        def delete(self):
            Num = input("学号：")
            if Num != "":
                self.__delete(Num)
            else:
                print("学号不能为空")

        def export(self):  # 定义函数用以导出数据
            try:
                file = open("Score.txt", "wt")  # 以wt方式打开文件
                self.cursor.execute("select * from score")  # 选择表内全部内容
                file.write("学号，姓名，语文，数学，英语\n")  # 写入属性名，以半角中文逗号分隔
                rows = self.cursor.fetchall()  # 从指针获得所有数据，为字典型
                for row in rows:  # 遍历写入
                    file.write(
                        f"{row['Num']},{row['Name']},{row['Chinese']},{row['Math']},{row['English']}\n")  # 将每个属性的值写入至每行，以半角英文逗号分隔
                file.close()  # 关闭文件
                print("导出成功")
            except Exception as err:
                print(err)

        def load(self):  # 定义函数用以从文件内加载文件
            try:
                path = input("输入文件名：")  # 输入文件路径
                if os.path.exists(path):  # 在os模块中，对象path有方法exists()用以确认某个文件是否存在
                    file = open(path, "rt")  # 如果存在，则读文本方式打开
                    read = file.readline().strip("\n").split("，")  # 首先读取文本文件第一行，即属性名，并用半角中文逗号进行分隔
                    cList = ["学号", "姓名", "语文", "数学", "英语"]  # 定义属性的准确名称
                    # 如果文件内的属性名与基准属性名能完全匹配
                    if len(read) == 5 and read[0] == cList[0] and read[1] == cList[1] and read[2] == cList[2] and read[3] == cList[3] and read[4] == cList[4]:
                        string = "True"  # 创建一个字符串变量string，用以为接下来的while循环做准备
                        while string != "":  # 当string不为空，即某行有数据时，由于是每回循环检测一次，因此在获得某行后也要对string检测
                            string = file.readline().strip("\n")  # 读某行，并去除分隔符，赋值于string
                            if string != "":  # 接下来如果string不为空的话
                                # 将之保存的半角英文逗号去除，得到一个列表
                                string = string.split(",")
                                if len(string) == 5:  # 如果列表长度为5，并且编号与姓名均不为空，则插入每项至数据库内，否则不插入
                                    Num = string[0].strip()
                                    Name = string[1].strip()
                                    Chinese = self.__loadCheck(string[2])
                                    Math = self.__loadCheck(string[3])
                                    English = self.__loadCheck(string[4])
                                    if Num != "" and Name != "":
                                        self.__insert(
                                            Num, Name, Chinese, Math, English)
                        print("导入成功")  # 如果文件读到结尾，则插入成功
                    else:
                        print("文件内容错误")  # 如果属性名不正确，则文件内容错误
                    file.close()  # 读取成功或未读取，都关闭文件
                else:
                    print(path+"不存在")
            except Exception as err:
                print(err)

        def process(self):  # 定义函数用以实现主程序与组件间调用
            self.open()  # 打开连接
            while True:
                print("1.列出 2.插入3.更改 4.删除 5.导出文件 6.加载文件 7.退出")
                string = input("请输入操作：")
                if string == "1":
                    self.show()
                elif string == "2":
                    self.insert()
                elif string == "3":
                    self.update()
                elif string == "4":
                    self.delete()
                elif string == "5":
                    self.export()
                elif string == "6":
                    self.load()
                elif string == "7":
                    self.close()  # 关闭连接并提交至数据库
                    break

    db = scoreDB()
    db.process()


p212_752()
