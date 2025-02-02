#此项目遵循MIT协议，任何自然人均可无需经过许可地对此项目进行无限的复制、改动、分发

def p5_122():
    import math
    num = float(input("输入一个数"))
    if num >= 0:
        num = math.sqrt(num)  # 对于对象num，使用方法math.sqrt
        print("平方根是：", num)
    else:
        print("复数不能开平方")
    print("The End")


# p5_122()


def p10_131():
    intager = 12
    print("|% d |" % intager)   # 对于变量intager，做整数转换
    # 对于变量intager，做整数转换，对于参数内正整数，向intager左侧输出指定占位数量减去传入的intager字符数量，占位符数量为2
    print("|% 4d |" % intager)
    # 对于变量intager，做整数转换，对于参数内负整数，向intager右侧输出指定占位数量减去传入的intager字符数量，占位符数量为2
    print("|% -4d |" % intager)
    # 对于变量intager，做整数转换，对于参数内的特殊数0，占位符为阿拉伯数字0，向intager左侧输出指定占位数量减去传入的intager字符数量，数量为2
    print("|% 04d |" % intager)
    # 对于变量intager，做整数转换，对于参数内的特殊参数-0，向intager右侧输出指定占位数量减去传入的intager字符数量，占位符数量为2
    print("|% -04d |" % intager)
    intager = 12345                 # 当传入字符大于指定占位数量时，不作占位处理
    print("|% d |" % intager)       # 对于变量intager，做整数转换
    # 对于变量intager，做整数转换，对于参数内正整数，向intager左侧输出指定占位数量减去传入的intager字符数量，因为占位符数量小于0，因此占位符数量为0
    print("|% 4d |" % intager)
    # 对于变量intager，做整数转换，对于参数内负整数，向intager右侧输出指定占位数量减去传入的intager字符数量，因为占位符数量小于0，因此占位符数量为0
    print("|% -4d |" % intager)
    # 对于变量intager，做整数转换，对于参数内的特殊数0，占位符为阿拉伯数字0，向intager左侧输出指定占位数量减去传入的intager字符数量，因为占位符数量小于0，因此占位符数量为0
    print("|% 04d |" % intager)
    # 对于变量intager，做整数转换，对于参数内的特殊参数-0，向intager右侧输出指定占位数量减去传入的intager字符数量，因为占位符数量小于0，因此占位符数量为0
    print("|% -04d |" % intager)


# p10_131()


def p11_132():
    year = 2015
    month = 2
    day = 1
    hour = 8
    minute = 12
    second = 0
    print("Time: % 04d-%02d-%02d %02d:%02d:%02d" %
          (year, month, day, hour, minute, second))  # 使用%对各个传入变量做分隔，并使用各参数为输出占位赋零


# p11_132()


def p11_133():
    string = 12.57432           # 传入浮点字符串
    print("|% f|" % string)     # 对于浮点字符串string,做浮点转换
    # 对于浮点字符串string,做浮点转换，对于参数符号"."的左位定义为包括占位符的总字符长度，是8，为8位，如总字符长度不足8位则向左填充占位符；右位定义小数长度，为1位
    print("|% 8.1f|" % string)
    # 对于浮点字符串string,做浮点转换，对于参数符号"."的左位定义为包括占位符的总字符长度，是8，为8位，如总字符长度不足8位则向左填充占位符；右位定义小数长度，为2位
    print("|% 8.2f|" % string)
    # 对于浮点字符串string,做浮点转换，对于参数符号"."的左位定义为包括占位符的总字符长度，是-8，为8位，如总字符长度不足8位则向右填充占位符；右位定义小数长度，为1位
    print("|% -8.1f|" % string)
    # 对于浮点字符串string,做浮点转换，对于参数符号"."的左位定义为包括占位符的总字符长度，是-8，为8位，如总字符长度不足8位则向右填充占位符；右位定义小数长度，为0位
    print("|% -8.0f|" % string)


# p11_133()


def p12_134():
    string = "ab"               # 传入string
    print("|% s |" % string)    # 对于字符串string，直接做字符串输出
    # 对于字符串string，传入参数8，定义为包括占位符的总字符长度，是8，为8位，如总字符长度不足8位则向左填充占位符；
    print("|% 8s |" % string)
    # 对于字符串string，传入参数-8，定义为包括占位符的总字符长度，是8，为8位，如总字符长度不足8位则向右填充占位符；
    print("|% -8s |" % string)


# p12_134()


def p16_exercise():
    p16_1_length, p16_1_width = input("输入一个矩形的长与宽，用半角英文分隔").split(",")
    p16_1_acreage = int(p16_1_length) * int(p16_1_width)
    print("矩形的面积为：", p16_1_acreage)

    # 使用24:00:00的秒数形式减去传入数值，得出距离午夜的秒数
    p16_2_InputSecond = 86400 - int(input("请输入秒数："))
    # 将上方得出的秒值除以60得出的余数，作为60秒以内的确切秒数使用，e.g:18325 % 60 = 25
    p16_2_Second = p16_2_InputSecond % 60
    # 用距离午夜的秒数将上方得出的确切秒数减去，并将结果除以60，得出总分钟数，通过求余得出确切的分钟数，e.g:（18325 - 25） / 60 = 305  305 % 60 = 5
    p16_2_Minute = (p16_2_InputSecond - p16_2_Second) / 60 % 60
    # 用距离午夜的秒数将上方得出的确切秒数减去，并将结果除以60，得出总分钟数，通过除以60并直接截取商的非小数位数字来计算，e.g:（18325 - 25） / 60 = 305 -> 305 / 60 = 5.083... -> 305 // 60 = 5
    p16_2_Hour = (p16_2_InputSecond - p16_2_Second) / 60 // 60
    print("%02d:%02d:%02d" % (p16_2_Hour, p16_2_Minute, p16_2_Second))  # 对结果做0占位


# p16_exercise()


def p19_211():
    Input = int(input("Enter:"))
    if Input % 2 == 0:  # 如果传入的整数能被2整除，则为偶数
        print("Even")
    else:                          # 否则为奇数
        print("Odd")


# p19_211()


def p19_212():
    Input = int(input("Enter:"))
    if Input > 0:  # 如果传入的整数大于0
        print(Input)  # 则直接输出正数
    else:                          # 否则为负数
        print(-Input)  # 则直接对传入整数做反处理


# p19_212()


def p19_213():
    a, b = float(input("a=")), float(input("b="))
    if a > b:  # 如果a大于b
        c = a  # 把a赋值给c
    else:
        c = b  # 否则把b赋值给c
    print(c)


# p19_213()


def p21_221():
    Mark = float(input("输入成绩："))
    if Mark < 0 or Mark > 100:  # 如果输入大于100或输入小于0，则不是一个有效的分数范围
        print("错误的成绩")
    elif Mark >= 90:
        print("A")
    elif Mark >= 80:
        print("B")
    elif Mark >= 70:
        print("C")
    elif Mark >= 60:
        print("D")
    else:
        print("E")


# p21_221()


def p22_222():
    DayInWeek = int(input("week="))
    if DayInWeek == 0:  # 如果输入为0，对变量Output赋值“星期天”
        Output = "星期天"
    elif DayInWeek == 1:  # 否则如果输入为1，......
        Output = "星期一"
    elif DayInWeek == 2:
        Output = "星期二"
    elif DayInWeek == 3:
        Output = "星期三"
    elif DayInWeek == 4:
        Output = "星期四"
    elif DayInWeek == 5:
        Output = "星期五"
    elif DayInWeek == 6:
        Output = "星期六"
    else:  # 如果传入参数皆不为以上数值，对变量Output赋值“星期天”
        Output = "未知"
    print(Output)  # 输出变量Output所具有的值


# p22_222()


def p23_223():
    import math
    print("输入一元二次方程的a,b,c")
    a, b, c = float(
        input("a=")), float(input("b=")), float(input("c="))  # 分别对传入的数值赋予给变量
    if a != 0:  # 如果a不等于0
        delta = b * b - 4 * a * c  # 则计算一元二次方程的delta
        if delta > 0:  # 如果delta的值大于0
            delta = math.sqrt(delta)  # 对delta使用math.sqrt方法求平方根
            solve1 = (-b + delta) / 2 * a  # 计算-b加上delta
            solve2 = (-b - delta) / 2 * a  # 计算-b减去delta
            print("x1 = ", solve1, ",x2 = ", solve2)  # 分别输出x1与x2
        elif delta == 0:  # 如果delta为0
            print("x1,x2 = ", -b / 2 * a)  # 输出x1与x2相同的结果
        else:  # 如果delta既不大于0，也不等于0
            print("输入无实数解")  # 则没有实数解
    else:  # 如果a为0
        print("并非一元二次方程")  # 则不是一元二次方程


# p23_223()


def p24_231():
    Tick = 0  # 初始化计数变量为0
    while Tick < 3:  # 当计数变量小于三时，执行以下循环
        Tick = + 1  # 计数变量加1
    print("Last", Tick)  # 仅输出在循环体外变量的最终值


# p24_231()


def p25_232():
    Tick = 0  # 初始化计数变量为0
    while Tick < 4:  # 当计数变量小于4时，执行循环
        print(Tick)  # 于循环体内输出计数变量的值


# p25_232()


def p25_233():
    Target = int(input("计算:从1加到"))  # 输入目标数值
    Tick = 0  # 初始化计数变量为0
    StartFrom = 0  # 初始化累积器变量
    while Tick <= Target:  # 当计数变量小于或等于输入的目标值时，执行以下操作
        StartFrom = StartFrom + Tick  # 将计数变量加入到累积器中
        Tick = Tick + 1  # 计数变量加1
    print(StartFrom)  # 输出累积器变量的值


# p25_233()


def p25_234():
    tick = 0  # 初始化计数变量为0
    startFrom = 0  # 初始化分数变量
    while tick < 5:  # 当计数变量小于5时，执行以下动作
        score = float(input(f"第{tick+1}个成绩:"))  # 获取每个分数
        startFrom = startFrom + score  # 将获取到的分数加入分数变量
        tick = tick + 1  # 计数器加1
    print(f"平均分为：{startFrom/5}")  # 计算并输出平均分


# p25_234()


def p25_235():
    intager = int(input("输入正整数："))  # 赋值于整数变量
    string = ""  # 初始化字符串为空字符串
    while intager != 0:  # 如果整数变量中的数值不为空，即不为0，执行以下循环
        singleNumber = intager % 10  # 将传入的整数变量除以10，得到余数，也就是整数变量中的尾部的一位数
        string = string + str(singleNumber)  # 将数字以字符串形式栈放入至字符串变量
        intager = intager // 10  # 将整数变量除以10，并获取其非小数的确切整数值，也就是去除尾部的一位数
    print(string)


# p25_235()


def p26_233():
    divisor, dividen = int(input("被除数：")), int(input("除数："))
    tick = 0  # 初始化计数器
    intager = str(divisor//dividen)  # 对输入的被除数与除数进行基本除法，并取确切非小数部分
    remaind = divisor % dividen  # 计算得出是否包含余数
    if remaind != 0:    # 如果包含余数，则商必有小数，进入小数处理
        offset = int(input("精确度偏移："))  # 如果侦测到是有小数的被除数与除数，提供输入精确度
        result = intager + "."  # 将上方确切整数作为结果的整数部分，并加上小数点以分隔后续小数
        while remaind != 0 and tick < offset:  # 当包含小数以及计数器小于设定值时，执行以下循环
            remaind = 10 * remaind  # 先将余数乘10，方便后续计算
            # 将余数与除数相除，得出确切整数部分，并将其添加在结果后方
            result = result + str(remaind//dividen)
            remaind = remaind % dividen  # 将余数与除数相除，如果余数已被除尽，则即使计数器未达到设定值也退出
            tick = tick + 1  # 计数器加1
        print(f"{divisor}/{dividen}={result}")  # 专用于输出小数商
    else:  # 如果被除数除以除数不包含余数
        print(f"{divisor}/{dividen}={divisor/dividen}")  # 专用于输出整数商


# p26_233()


def p29_241():
    intager = int(input("输入一个正整数，判断是否为质数:"))  # 质数：只能被1与自身整除的数
    minPrime = 2  # 定义最小质数
    while minPrime < intager:  # 当定义数值小于传入数值时，执行以下循环
        if intager % minPrime == 0:  # 如果整数除以定义数值的余数为0
            break  # 跳出循环，即当传入数值为偶数时跳出循环
        minPrime = minPrime + 1  # 否则将定义数值加1，即此条代码仅在传入数值为奇数时执行
    if minPrime == intager:  # 跳出循环后，当定义数值等于传入整数时
        print(f"{intager} 是质数")
    else:  # 否则
        print(f"{intager} 不是质数 ")


# p29_241()


def p29_242():
    intA, intB = int(input("输入两个正整数，找出两数的最小公倍数\nA=")), int(
        input("B="))  # 最小公倍数：能被任意两个数同时整除的最小的数
    if intA > intB:  # 如果传入数值A大于传入数值B，即最小公倍数永不小于输入数值中的最大的一个数
        intC = intA  # 则向计算数值赋予输入的最大值A
    else:
        intC = intB  # 否则如果B大于A，则向计算数值赋予最大值B
    multiply = intA * intB  # 将两数相乘
    while intC <= multiply:  # 当计算数值小于两数相除的积时,即最小公倍数永不大于两数相乘的积
        if intC % intA == 0 and intC % intB == 0:  # 一旦计算数值可以被输入数值皆整除时，即为最小公倍数
            break  # 跳出循环
        intC = intC + 1  # 因为计算数值永远大于等于输入数值中最大的数，因此将计算数值加1
    print(intC)  # 输出计算数值，即最小公倍数


# p29_242()


def p30_243():
    intA, intB = int(input("输入两个正整数，找出两数的最大公约数\nA=")), int(
        input("B="))  # 最大公约数：能把两个数同时整除的最大的数
    if intA > intB:  # 如果传入数值A大于传入数值B，即最大公约数永不大于输入数值中最小的一个数
        intC = intB  # 则向计算数值赋予输入的最小值B
    else:
        intC = intA  # 否则如果B大于A，则向计算数值赋予最小值A
    while intC >= 1:  # 当计算数值大于等于1时，即最大公约数永不小于1
        if intA % intC == 0 and intB % intC == 0:  # 一旦输入的数均能用计算数值整除时，即为最大公约数
            break  # 跳出循环
        intC = intC - 1  # 因为计算数值永远小于等于输入数值中最小的数，因此将计算数值减1
    print(intC)  # 输出计算数值，即最大公约数


# p30_243()


def p34_254():
    number, count = 0, 0  # 初始化输入判断
    while number <= 0 or number >= 10:  # 当传入数值超过1-9的范围时，循环执行以下代码
        number = int(input("计算a+aa+aaa...,请输入1-9之间的数\na="))
    while count <= 0:  # 当需计算次数未定义时，循环执行以下代码
        count = int(input("最终a的数量n="))
    total, tick = 0, 0  # 初始化累加器与计数器
    for loop in range(count):  # 循环次数是需计算的次数加1
        tick = 10 * tick + number  # 将计数器乘10再加a的值，即将a的数值栈推入进计数器
        total = total + tick  # 将计数器每次输出的值传入累加器
        if loop < count - 1:  # 输出功能的实现：当循环次数小于计算次数时，减1则为了给输出结果留空
            print(tick, end="+")  # 如果循环次数未达到指定计算次数
        else:
            print(tick, end="=")  # 如果循环次数达到设定值，则输出
    print(total)  # 输出总结果


# p34_254()


def p37_264():
    money = 10
    beer, cap, bottle, total = money // 2, 0, 0, 0  # 初始化钱，啤酒数......
    while beer > 0:  # 当还有啤酒时
        cap = cap + beer  # 总瓶盖数等于之前的瓶盖数加这次的啤酒数
        bottle = bottle + beer  # 总空瓶数等于之前的空瓶数加这次的啤酒数
        total = total + beer  # 总啤酒数等于之前的啤酒数加这次的啤酒数
        print(f"这次喝了{beer}瓶酒，总共喝了{total}瓶酒")
        beer = 0  # 初始化啤酒数，即已喝完
        print(f"喝完后有{beer}瓶啤酒，{cap}个盖子，{bottle}个空瓶")
        # 换物功能的实现：
        if cap >= 4:  # 当有4个以上的瓶子时
            # 用总盖子数减去将盖子换完后的剩下的盖子，得出可换的盖子数，将总盖子数除以4后取确切整数值，得出可换多少啤酒
            print(f"用{cap - cap % 4}个盖子换{cap // 4}瓶酒")
            beer = beer + bottle // 4  # 将换得的啤酒加入总啤酒数
            cap = cap % 4  # 瓶盖数等于换完酒后余下的瓶盖
        if bottle >= 2:  # 如果有2个以上的空瓶时
            # 用总空瓶数减去将空瓶换完后的剩下的空瓶，得出可换的空瓶数，将总空瓶数除以2后取确切整数值，得出可换多少啤酒
            print(f"用{bottle - bottle % 2}个空瓶换{bottle // 2}瓶啤酒")
            beer = beer + bottle // 2  # 将换得的啤酒加入总啤酒数
            bottle = bottle % 2  # 空瓶数等于换完酒后余下的空瓶
        print(f"换后拥有{beer}瓶啤酒，还剩{cap}个盖子，{bottle}个空瓶\n")  # 用于循环体内展示
    print(f"总共喝了{total}瓶酒，剩下{cap}个盖和{bottle}个空瓶")  # 用于循环结束后的展示


# p37_264()


def p39_271():
    print("九九乘法表")
    for FirMultiplier in range(1, 10):  # 被乘数的范围：1-9
        # 乘数的范围：从1开始，结束为从2到9递增，每次递增数为1，即范围为1-2,1-3，1-4...1-9
        for SecMultiplier in range(1, FirMultiplier + 1):
            print(
                f"{FirMultiplier} * {SecMultiplier} = {FirMultiplier * SecMultiplier}", " ", end="")  # 每个式子用空格隔开，并保持不换行
        print()  # 上一行执行完成后，换行


# p39_271()


def p40_272():
    tick = 0  # 初始化输出功能的计数器
    for divisor in range(2, 101):  # 给被除数赋值范围2-100
        judgement = True  # 初始化判断变量
        for dividen in range(2, divisor):  # 除数的定义范围为大于1并小于被除数的整数
            if divisor % dividen == 0:  # 在一个区间为从2开始，结束的范围是从2-100，每次递增量为1的循环中作为除数，被除数是2-100；如果有一个数能被除自己之外的数整除
                judgement = False  # 则将判断变量改为False
                break  # 直接中断计算，开始计算下一个被除数
                # 如果在2-100中，一旦有一个数只能被自己整除，而不能被其他比自己小的数整除，则不进入上述条件判断定义的语句
        # 输出功能/得到结果的实现，隶属于被除数的循环
        if judgement:  # 如果探测到判断变量为True，即有一个数能被自己整除，并且不能被其他数整除，因此，只要某个数为质数，则执行以下输出
            print("% 5d" % divisor, end=" ")  # 获取当前的被除数，即某个质数
            tick += 1  # 用于控制输出格式的计数器，为总共输出的数值计数
            if tick % 5 == 0:  # 如果一排有五个数值，即只要计数器每次为5的倍数就执行以下语句
                print()  # 换行


# p40_272()


def p40_273():
    for first in range(1, 4):  # 第一个数的范围是1-3
        for second in range(1, 4):  # 第二个数的范围是1-3
            for third in range(1, 4):  # 第三个数的范围是1-3
                # 不输出有多于2个的相同数值，即让输出的一行数中所有数都为不相同的数，即如果一行中有两个或两个以上的数相同，则不进行输出
                if first != second and second != third and first != third:
                    print(first, second, third)


# p40_273()


def p43_274():
    condition1 = 1  # 初始化条件1
    while condition1 <= 3:  # 当条件1小于等于3时，进入第一层循环
        condition2 = 1  # 初始化条件2
        print("进入循环")
        while condition2 <= 3:  # 当条件2小于等于3时，进入第二层循环
            print(condition1, condition2)  # 输出此时的条件1和条件2
            if condition2 % 2 == 0:  # 如果条件2为偶数
                break  # 则跳出第二层循环
            condition2 = condition2 + 1  # 否则为条件2的数值加1
        print("退出循环")
        condition1 = condition1 + 1  # 完成第二层循环后，为第一层循环的条件1的数值加1


# p43_274()


def p44_274():
    for row in range(4):  # 控制行数
        for length in range(2 * row + 1):  # 控制长度，每增加一行，长度就增加2
            print("*", end="")  # 直接在尾部追加输出结果
        print()  # 每输出完一行就换一次行


# p44_274()


def p45_275():  # 一个任意整数和一组数字，如果这个任意整数可以被这组数字里的任意一个数给整除，并且这组数字相乘可以得到这个任意整数，那么，这组数字则为把整数质因数分解后的结果
    intager = int(input("输入一个整数"))
    judgement = True  # 初始化判断变量
    print(intager, end="")
    tick = 2  # 初始化计数器为2，因为质数为可以被1和自己整除，为防止之后被1给整除而导致陷入循环，因此不包含1；作为结果，此变量为最小因数的抽象
    while tick <= intager:  # 当计数器小于整数时，执行以下循环
        while intager % tick == 0:  # 如果整除与最小因数能够整除，即计数器的数值为整数的最小因数（不包括1），则进入下方输出
            if judgement:  # 如果判断条件为正
                print("=", tick, end="")  # 则输出“=”符号与第一次计算结果，
                # 将判断条件改为否，也就是说，由于if条件收到的判断变量为非正，因此在第一次输出此条件后，之后的输出都由else的代码决定；之所以会输出一次，是因为在循环体外前已定义了判断条件为正
                judgement = False
            else:  # 如果判断条件非正
                print("*", tick, end="")  # 第一次计算结果之后的结果都由此程序输出
            intager = intager // tick  # 为了之后的计算，将整数除以计数器数值，并取纯整数，也就是将所有最小因数相乘后可以得到整数的功能实现
        tick = tick + 1  # 如果整数无法与计数器整除时，那么计数器的数值并非为最小因数，由于每次得出结果不可能小于前一个结果，因此每当无法进入第二层循环体时，计数器会将每个大于前一个的数值均尝试一遍


# p45_275()


def p46_281():
    import math
    try:  # try下指定可能会出错的代码
        print(math.sqrt(float(input("计算一个数的平方根："))))
    except Exception as err:  # except指定需要检测的例外情况，Exception为所有可能造成出错的例外情况，并将错误结果赋值至err变量中
        print(err)  # 只有当错误发生时，才输出err变量中的报错
    print("End")  # 使用了try/except的python程序在遇到错误时会继续运行


# p46_281()


def p48_282():
    print("开始")
    try:  # 首先开始执行try指定的语句块
        print("除0计算")
        devideZero = 1 / 0  # 除0错误
        print("计算结束")  # 当错误发生时，错误之后的代码不会继续执行
    except Exception as err:  # except语句将错误进行捕捉，并指定检测所有错误，然后将错误传入变量
        print(err)  # 输出错误信息
    print("终止")


# p48_282()


def p49_283():
    print("开始")
    try:
        print("在try语句中")
        # 人为定义一个非程序性的错误，由于是在try语句块内，错误会转到except处理，如果在try语句外，则直接中止程序运行;指定类型为“例外”的错误，并设置错误消息为“一个错误”
        raise Exception("一个错误")
        print("结束try")  # 中断执行
    except Exception as err:  # 侦测到错误，并将错误消息传入至err变量中
        print(err)  # 输出err
    print("终止")


# p49_283()


def p49_284():
    import math
    while True:  # 永久循环，在计算完毕前一直循环
        try:
            intager = int(input("计算一个数的平方根："))
            if intager <= 0:  # 如果整数小于0
                raise Exception("输入为负数")  # 手动抛出一个“例外”错误，并传出信息，中止if之后的执行
            print(math.sqrt(intager))  # 输出结果
            print("完成")
            break  # 计算完后退出循环体
        except Exception as err:  # 处理并输出错误
            print("输入错误", err)


# p49_284()


def p50_285():
    import math
    while True:  # while语句用以控制判断输入是否符合规则，否则重新输入
        try:
            intager = int(input("计算一个数的平方根："))
            if intager <= 0:  # 如果整数小于0
                raise Exception()  # 手动抛出一个“例外”错误，并不附加任何信息
            break  # 如果未抛出错误，则退出判断语句块
        except:  # 不探测指定错误，而是一旦出错，就返回下列输出
            print("请输入正整数")
    print(math.sqrt(intager))  # 判断完输入是否正确后，开始计算，位于判断之后
    print("完成")


# p50_285()


def p51_286():
    try:
        name, gender, age = input("姓名："), input("性别："), float(input("年龄："))
        if name.strip() == "":  # 如果姓名为空或者仅有空格，则抛出错误，strip函数用以去除掉字符串前后的空格，因此也可以防止用空格代替空姓名而通过的现象产生
            raise Exception("无效的姓名")
        elif gender != "男" and gender != "女":  # 否则如果性别非两性，则抛出错误
            raise Exception("无效的性别")
        elif age < 18 or age > 30:  # 否则如果年龄小于18或大于30，也抛出错误
            raise Exception("无效的年龄")
        print(name, gender, age)
    except Exception as err:  # 捕捉并输出错误
        print(err)


# p51_286()


def p52_291():  # 哥德巴赫猜想：任何一个6及以上的偶数均可由两个素数相加得到，即不小于6的偶数=素数1+素数2
    while True:  # 验证输入是否正确
        even = int(input("验证哥德巴赫猜想,输入一个大于等于6的偶数:"))
        if even % 2 == 0 and even >= 6:  # 如果输入为大于等于6的偶数
            break  # 则跳出循环，否则重新输入
    maxprime = even // 2  # 因为偶数=素数1+素数2，所以假定最大的素数为偶数除以2
    intager1 = 2  # 定义整数1为最小素数2
    while intager1 <= maxprime:  # 当整数1小于最大素数时
        isprime = True  # 初始化用以判断是否为素数的变量
        # 以下for代码块判断整数1是否为素数，定义计算素数的变量judgePrime，judgePrime的范围是大于1，且不大于整数1的每个整数值
        for judgePrime in range(2, intager1):
            if intager1 % judgePrime == 0:  # 如果整数1能够被小于自己的数整除或能被2整除
                isprime = False  # 那么整数1不是素数
                break  # 退出判断整数1是否为素数的循环
        if isprime:  # 如果整数1为素数，即整数1不能被自己或1以外的数整除
            intager2 = even - intager1  # 那么由偶数=素数1+素数2可以得知，整数2=偶数-整数1
            for judgePrime in range(2, intager2):  # 为了判断整数2为素数的准确性，因此也要进行判断是否为素数
                if intager2 % judgePrime == 0:  # 如果整数2不是素数
                    isprime = False  # 设置判断是素数的变量为否
                    break  # 退出判断代码块
            if isprime:  # 如果两个整数均通过了判断是素数的测试
                print(f"{even}={intager1}+{intager2}")  # 输出结果
        intager1 = intager1 + 1  # 如果整数1不是素数，那么直接跳过判断整数2的代码块，将整数1加1后继续循环运行，实际上优化了运行速度
    print("完成")  # 一旦第一个整数大于偶数除以2，即整数1大于假定的最大素数，将直接退出while循环体，因此第一个整数永远不会大于输入数值的一半


# p52_291()


def p54_exercise():

    def exercise1():
        while True:
            try:
                a, b, c = float(input("计算一元二次方程,a=")), float(
                    input("b=")), float(input("c="))
                if a == 0:
                    raise ValueError("a必须不等于0")
                break
            except Exception as err:
                print(err)
        delta = b * b - 4 * a * c
        if delta > 0:
            print(f"x1={(-b + delta) / 2 * a},x2={(-b - delta) / 2 * a}")
        elif delta == 0:
            print(f"x1=x2={(-b - delta) / 2 * a}")
        else:
            print("方程无实数解")

    exercise1()

    def exercise2():
        from math import sqrt
        a, b, c = float(input("计算三角形面积,第一条边=")), float(
            input("第二条边=")), float(input("第三条边="))
        if a + b > c and b + c > a and c + a > b:
            p = (a + b + c) / 2
            area = sqrt(p * (p - a) * (p - b) * (p - c))
            print(f"三角形的面积是{area}")
        else:
            print("无法构成三角形")

    exercise2()

    def exercise3():
        string = str(input("输入一个字符，判断是否为小写字母："))
        print("输入为小写字母") if string.islower(
        ) and string.isalpha() else print("输入为除小写字母外的其他字符")

    exercise3()

    def exercise4():
        print(input("输入一串字符,判断有多少个0:").count("0"))

    exercise4()

    def exercise5():
        a, b = int(input("输入两个整数判断谁最大，第一个")), int(input("输入第二个整数"))
        print(f"{a}为最大的数")if a > b else print(f"{b}为最大的数")

    exercise5()

    def exercise6():
        print(str(input("将小写字母转换为大写字母：")).upper())

    exercise6()

    def exercise7():
        year = int(input("输入一个年份，判断是否为闰年"))
        print("是闰年") if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else print(
            "不是闰年")

    exercise7()

    def exercise8():
        a, b = float(input("输入两个数按从大到小排序大，第一个")), float(input("输入第二个数"))
        print(f"{a}>{b}")if a > b else print(f"{b}>{a}")

    exercise8()

    def exercise9():
        a, b, c = int(input("输入三个整数找出最小的数，第一个")), int(
            input("第二个")), int(input("第三个"))
        if a < b and a < c:
            print(f"{a}最小")
        elif b < a and b < c:
            print(f"{b}最小")
        else:
            print(f"{c}最小")

    exercise9()

    def exercise10():
        profit = float(input("输入利润，单位按万元计："))
        if profit <= 10:
            bonus = profit * 0.12
        elif profit > 10 and profit < 20:
            bonus = 10 * 0.12 + (profit - 10) * 0.085
        elif profit >= 20 and profit <= 40:
            bonus = 10 * 0.12 + 10 * 0.085 + (profit - 20) * 0.06
        elif profit >= 40 and profit <= 60:
            bonus = 10 * 0.12 + 10 * 0.085 + 20 * 0.06 + (profit - 40) * 0.04
        elif profit >= 60 and profit <= 100:
            bonus = 10 * 0.12 + 10 * 0.085 + 20 * \
                0.06 + 20 * 0.04 + (profit - 60) * 0.025
        else:
            bonus = 10 * 0.12 + 10 * 0.085 + 20 * 0.06 + \
                20 * 0.04 + 40 * 0.025 + (profit - 100) * 0.01
        print(f"发放的奖金量为{bonus}万元")

    exercise10()

    def exercise11():  # 圆面积计算公式：(x-a)^2+(y-b)^2=r^2,其中(a,b)为圆心坐标，r为半径
        x, y = float(input("查找在哪个圆上x=")), float(
            input("y="))  # x,y定义距离圆心(a,b)的任意点，半径已给出，因此r^2为1
        if (x-2)*(x-2) + (y-2)*(y-2) <= 1:  # 也就是说，如果将任意点带入方程后得出的结果不大于1，那么这个点距圆心围出的圆的面积永远不大于1，即这个任意点只能在圆的内部
            print("该坐标在第一个圆上")
        elif (x+2)*(x+2) + (y-2)*(y-2) <= 1:  # 由于四个圆相互分离，因此不会有任意点出现在多个圆的情况发送
            print("该坐标在第二个圆上")
        elif (x+2)*(x+2) + (y+2)*(y+2) <= 1:  # 因此这四个公式中，一旦有一个公式的结果小于0，另外三个公式则会大于0
            print("该坐标在第三个圆上")
        elif (x-2)*(x-2) + (y+2)*(y+2) <= 1:
            print("该坐标在第四个圆上")
        else:  # 例外情况，即点均不在四个圆上，在这种情况下，以上四个公式的计算结果均大于1
            print("该坐标不在任何圆内")

    exercise11()


# p54_exercise()


def p56_313():

    def fun(x):  # 定义函数fun()，并为函数定义需要传入的参数x，x变量的数值仅在函数fun()内可用
        print(x)  # 输出x的值
        if x < 0:  # 如果x小于0
            return  # 退出函数fun()，在此并不传出任何值，但在其他用例可以是传出某个值，也可以是表达式：return ……
        print(x * x)  # 一旦return执行，之后的代码均不会执行，与break有异曲同工之处

    y = -2  # 在函数fun()的外部定义变量y等于-2
    fun(y)  # 向函数fun()传入y的值，即让fun()的内部变量x等于外部变量y


# p56_313()


def p58_313_2():

    def isPrime(intager):  # 定义isPrime函数用以判断一个整数是否为质数
        print("开始计算")
        for judgement in range(2, intager):
            print(judgement)
            if intager % judgement == 0:  # 如果不为质数
                return 0  # 则传出0
        print("计算完成")
        return 1  # 如果为质数，则传出1，传出的值也可以是其他布尔值，包括True、False

    print(f"return {isPrime(9)}")  # 向函数isPrime传入数值9，并输出运行后从函数内传出的数值0或1


# p58_313_2()


def p58_313_3():  # 没有返回值的函数

    def Sayhello():
        print("Hello,everyone!")

    Sayhello()  # 直接输出函数内定义了需要输出的内容

    def fun(x):
        if x < 0:
            return  # 直接中断程序运行
        print(x)

    fun(-5)


# p58_313_3()


def p58_311():

    def max(a, b):  # 定义函数max，需要传入两个数值
        c = a  # 假定a大于b，因此结果等于a
        if b > a:  # 如果b大于a
            c = b  # 则结果等于b
        return c  # 传出结果
    print(max(2, 4))  # 输出结果


# p58_311()


def p59_312():

    def max(a, b):  # 定义函数max，需要传入两个数值
        maxValue = a  # 假定a大于b，因此结果等于a
        if b > a:  # 如果b大于a
            maxValue = b  # 则结果等于b
        return maxValue  # 传出结果

    # 定义需要调用max函数的代码
    a, b, c = float(input("输入三个数，查找最大值,a=")), float(
        input("b=")), float(input("c="))
    firstmax = max(a, b)  # 首先传入a,b到max()函数，然后传出a,b中最大的值，并赋值到变量firstmax
    # 将c与在a,b中最大的值进行比较，即将c与firstmax传入max()函数中，并最终传出最大数值至secondmax变量中
    secondmax = max(c, firstmax)
    print("max=", secondmax)  # 输出最大值


# p59_312()


def p60_314():

    def greatestCommonDivisor(a, b):  # 如果传入数值A大于传入数值B，即
        minValue = a
        if b < a:
            minValue = b
        # 为可能的最大公约数创建范围，从传入的最小数值开始，并以1为变化值向下递减，并且不小于等于0
        for divisor in range(minValue, 0, -1):
            if a % divisor == 0 and b % divisor == 0:  # 如果某个公约数能够将两个整数整除，由于for是从大到小递减，因此第一次得出的结果即为最大公倍数
                return divisor  # 返回divisor在计算停止时所含有的变量

    def leastCommonMultiple(a, b):
        maxValue = a
        if b > a:
            maxValue = b
        multiply = a * b
        # 为可能的最小公倍数创建范围，从传入的最大数值开始，而且不大于两数相乘的积
        for dividen in range(maxValue, multiply + 1):
            if dividen % a == 0 and dividen % b == 0:  # 如果某个公倍数能够被两个整数整除，由于for是从小到大递增，因此第一次得出的结果即为最小公倍数
                return dividen  # 返回dividen在计算停止时所含有的变量

    # 用以调用两个函数的语句
    a, b = int(input("输入两个数，获取它们的最大公倍数与最小公约数,a=")), int(input("b="))
    print(f"最大公约数{greatestCommonDivisor(a,b)}")
    print(f"最小公倍数{leastCommonMultiple(a,b)}")


# p60_314()


def p62_321():

    def sumTo(intager):  # 定义sumTo函数用以计算(1+2+……+intager)的和，函数内的变量tick,loop,intager均为内部变量
        tick = 0  # 初始化累加器
        # 创建循环，从0到intager+1，即从包括0开始到intager这个值结束，可代换为range(0,intager+1,1)
        for loop in range(intager + 1):
            tick = tick + loop  # 将每次循环出的结果加到累加器内
        return tick  # 传出累加器的数值

    m = 10
    print(sumTo(m))  # 将m传入sumTo函数，并输出累加器传出的数值


# p62_321()


def p62_322():

    def fun(x, y):
        print(f"Inside Func:{x,y}")
        x, y = 1, 2  # 在函数内部定义x和y分别为1和2

    x, y = 100, 200  # 在函数外部定义x和y分别为100和200
    fun(x, y)  # 由于函数内部并无任何传出变量，而且
    print(x, y)


# p62_322()


def fun_323_1(x_323_1):  # 单层函数

    global y_323_1  # 声明变量y为主程序的全局变量
    y_323_1 = 0  # 定义程序全局变量y的值为0
    x_323_1 = 0  # 定义函数内变量x的值为0


x_323_1, y_323_1 = 1, 2  # 在主程序定义函数x和y
# fun_323_1(x_323_1)  # 将x的值传入函数内，由于在函数内同时修改的也是外部的值，因此，从函数内输出的变量仅有y的数值
# print(x_323_1, y_323_1)#输出x和y，结果，程序全局变量y的数值被fun函数影响，所以在函数外部的y值会变为0


def p63_323_2():  # 嵌套函数情况下的全局变量

    def fun(x):
        global y_323_2  # 声明变量y为主程序的全局变量
        y_323_2 = 0  # 设置y的值为0
        x = 0

    # 对于一个已声明全局变量的内部函数，即使该内部函数为一个主函数的嵌套，该内部函数的全局变量也不会影响到位于主函数的其他的语句，因此如果需要让内部函数的全局变量应用到主函数，需要在主函数体内声明使用主程序的全局变量
    global y_323_2
    x, y_323_2 = 1, 2  # 在宿主函数体定义
    fun(x)  # 运行函数，由于x这个变量并未被fun函数作为全局变量传入函数，而因为fun函数主动声明自己的y变量与全局变量相等，因此y变量内的值会被永久改变
    print(x, y_323_2)  # 输出x,y


# p63_323_2()


def p63_324():

    def A(x):  # 定义函数块A，需要传入一个参数
        global y  # 将函数内的变量y等于外部变量y
        x, y = 0, 0  # 设置x,y为0

    def B(x):  # 定义函数块B，需要传入一个参数
        global y  # 将函数内的变量y等于外部变量y
        x, y = 0, 10  # 设置x,y为0

    global y
    x, y = 1, 2  # 初始化x,y的值分别为1和2
    A(x)  # 运行函数A，此时y已经被函数A更改为0
    B(x)  # 运行函数B，此时y已经被函数B更改为10
    print(x, y)  # 输出x和y


# p63_324()


def p64_324():

    def input_324():  # 定义输入函数
        global province, city  # 定义全局变量province,city
        province, city = input("省份："), input("城市：")

    def output_324():  # 定义输出函数
        print(f"省份：{province} 城市：{city}")

    global province, city
    province, city = "", ""  # 将变量初始化

    input_324()  # 执行输入
    output_324()  # 执行输出


# p64_324()


def p66_331():

    def innerSum(intager):  # 定义用以计算公式内部的加法
        tick = 0  # 初始化累加器
        for loop in range(1, intager + 1):
            tick = tick + loop  # 从1加到传入的数值
        return tick  # 返回累加器的数值给需要调用这个函数的语句

    def totalSum(intager):  # 定义用以将个部分的和相加
        tick = 0  # 初始化累加器
        for loop in range(1, intager+1):
            tick = tick + innerSum(loop)  # 将将从innerSum函数得到的数据块累加
        return tick  # 返回累加器的数值给需要调用这个函数的语句

    print("计算结果", totalSum(int(input("计算从1+(1+2)+...+(1+2+...+n),n="))))


# p66_331()


def p67_332():

    def isPrime(intager):  # 定义用以判断是否为质数的函数
        for loop in range(2, intager):  # 循环开始，不大于传入数值
            if intager % loop == 0:  # 如果输入能被一个数整除
                return 0  # 那么这个数不是质数，返回0
        return 1  # 否则返回1

    intager = int(input("输入一个数，找出它的质因数"))
    for loop in range(2, intager + 1):  # 循环开始，不包括1，包括输入数值，用以判断某个数是否为输入数值的因数
        # 如果一个数为输入数值的因数，并且是质数；由于在isPrime定义了传出的是0或1，因此如果传出的是0，则为False，1或以上为True
        if intager % loop == 0 and isPrime(loop):
            print(loop)  # 输出数值


# p67_332()


def p67_333():

    def isPrime(intager):  # 用以判断是否为质数
        for loop in range(2, intager):
            if intager % loop == 0:
                return 0
        return 1

    print("将100以及以下的偶数用以验证哥德巴赫猜想")
    for number in range(6, 101, 2):  # 大于等于6，小于12，每次增加2的循环
        # 定义整数1不包含最小质数，最大数值不超过可传入的最大数值，每次增加2
        for intager1 in range(3, number + 1, 2):
            intager2 = number - intager1  # 则整数2等于输入数值减去整数1
            if isPrime(intager1) and isPrime(intager2):  # 如果整数1和整数2都是质数
                print(f"{number} = {intager1} + {intager2}")  # 输出这条式子
                break  # 每个偶数只需输出一次，并且第一个整数永远为符合的最小质数


# p67_333()


def p69_341():

    def fun(a, b=1, c=2):  # 定义一个具有默认参数的函数，并且必须有一个参数传入才能执行
        print(a, b, c)  # 输出a,b,c的值

    fun(0)  # 向fun函数传入0
    fun(1, 2)  # 向fun函数传入1,2，默认将数值顺序对齐，并且在传入指定数值后，fun函数的默认参数将会被传入的数值替代
    fun(1, 2, 3)  # 向fun函数传入1,2，3，所有数值均被替换，且默认参数被传入数值替代


# p69_341()


def p69_342():

    def fun(a, b=1, c=2):  # 定义一个具有默认参数的函数，并且必须有一个参数a传入才能执行
        print(a, b, c)

    # 向fun函数传入0,4,2，在没有特别指定变量a的位置时，首位必须指定一个值用以变量a，可以是变量或字符串，而b,c的值可以在指定后任意放置
    fun(0, c=4, b=2)
    # 在只想要更改位于第三位的默认变量c的情况下，可以指定要更改的变量c，即函数内第三位的值，并且不影响其他值，当然，在没有特别指定变量a的位置时，首位必须指定一个值用以变量a
    fun(0, c=4)
    fun(b=2, a=1, c=4)  # 在指定了必要变量a的位置下，各数值的顺序变动不受限制，并且更改的值均为指定的变量
    fun(a=0, c=4, b=2)
    fun(c=1, b=3, a=2)


# p69_342()


def p70_343():

    def fun(a, b=1, c=2):  # 标准定义：a为位置参数，b,c为键值参数；位置参数必须在键值参数的前位
        print(a, b, c)
    # 以下为错误函数格式的示例
    # fun(a=0,1,c=2) ->  不符合规范的调用，在不指定位置参数的特殊位置的情况下，位置参数必须在键值参数的前方

    # def fun(a=0, b, c=0):  ->  错误的定义，位置参数必须在键值参数的前位
        print(a, b, c)

    fun(0)  # 也就是说，调用函数所要传入的参数要么是全部顺序指定
    fun(0, 1)
    fun(a=1, b=2, c=3)  # 要么全部直接指定
    fun(0, 1, c=3)  # 要么混合指定，位置参数必须位于键值参数的前位


def p71_344():
    help(print)  # 使用help语句获取指定语句的帮助文档
    # 默认的：sep--各个值用空格分隔；end--以\n结尾，即换行；file--将输出重定向到(sys.stdout)默认为控制台的标准输出；flush--是否将存入缓冲区中待输出的内容直接输出到某处，开启可防止输出内容在内存中时断电丢失
    print(1, 2)
    print(1, 2, sep='-')  # 输出指定数值，并用"-"分隔
    print("line")
    print("line", end='*')  # 将默认的结尾换行替换成"*"结尾，因此下一行也会接上此行输出
    print("end")


# p71_344()


def p72_351():

    def fun():
        print("开始")
        n = 1 / 0  # 除0错误
        print("结束")

    try:
        fun()  # 即使是函数内的错误，错误也会向上传递到开始调用的主函数
    except Exception as err:
        print(err)


# p72_351()


def p72_352():

    def fun():
        print("开始")
        try:
            n = 1 / 0
            print("结束")
        except:  # 函数内的错误捕捉器，捕捉所有错误
            print("函数内部错误")

    try:
        fun()
    except Exception as err:  # 在错误被捕捉后，将会停止传递，因此外层函数无法捕获错误，所以如果内外代码块中均没有错误捕捉器，错误会一直向外传播，结果，程序中止
        print(err)


# p72_352()


def p73_353():

    def A():  # 定义一个除0错误
        print("A开始")
        n = 1 / 0
        print("A结束")

    def B():  # B调用A
        print("B开始")
        A()
        print("B结束")

    try:
        B()  # 调用B
        print("结束")  # 在主程序中，由于调用B的过程中发生错误，因此主程序的语句也不会再向下执行
    except Exception as err:  # 由于错误向外传播，在主程序中捕获到错误
        print(err)
    print("终止")


# p73_353()


def p74_354():

    def A():  # 除以0
        print("A开始")
        n = 1 / 0
        print("A结束")

    def B():
        print("B开始")
        try:
            A()
        except Exception as err:  # 位于B函数的错误捕捉器
            print("由B函数捕捉", err)
        print("B结束")

    try:
        B()
        print("完成")
    except Exception as err:  # 位于主程序的错误捕捉器，在错误被捕捉后，将会停止传递，因此外层函数无法捕获错误
        print("由主程序捕捉", err)
    print("终止")


# p74_354()


def p75_355():

    def A():
        print("A开始")
        n = 1 / 0
        print("A结束")

    def B():
        print("B开始")
        A()
        print("B结束")

    B()  # 由于程序及函数内没有任何错误捕捉器，错误会一直向外传播，结果，程序中止
    print("终止")


# p75_355()


def p75_353():

    def timeConvert():
        hour = int(input("输入时分秒，转换为hh:mm:ss;时:"))
        if hour < 0 or hour > 23:  # 如果小时的输入不符合规范
            raise Exception("错误小时数")  # 抛出错误
        minute = int(input("分:"))
        if minute < 0 or minute > 59:  # 如果小时的输入不符合规范
            raise Exception("错误的分钟数")  # 抛出错误
        second = int(input("秒:"))
        if second < 0 or second > 59:  # 如果小时的输入不符合规范
            raise Exception("错误的秒数")  # 抛出错误
        print("%02d:%02d:%02d" % (hour, minute, second))

    try:
        timeConvert()
    except Exception as err:  # 捕捉被抛出的错误
        print(err)  # 输出错误


# p75_353()


def p77_361():
    import myModule  # 从同一文件夹下的其他python文件引入函数；直接引入myModule里的所有函数
    from myModule import myMax, myMin  # 从名为myModule的python文件引入myMax函数和myMin函数
    # 指定从myModule调用myMax函数和myMin函数
    print(myModule.myMin(1, 2), myModule.myMax(1, 2))
    print(myMin(1, 2), myMax(1, 2))  # 在经过from...import...语句后，直接调用函数


# p77_361()


def p78_362():
    # 从主程序所在位置旁边的文件夹Mine里将myModule文件内的myMin函数和myMax函数引入
    from Mine.myModule import myMin, myMax
    print(myMin(1, 2), myMax(1, 2))


# p78_362()


def p78_364():
    import sys  # 导入用以与解释器交互的模块，即与python引擎交互的模块，
    path = sys.path  # 将现在正在使用的python解释器的数值赋值到path变量，此时path的数值类型为列表
    print(path)
    for i in path:  # 因为path为列表，因此此处的for起到的是遍历列表的效果
        print(i)


# p78_364()


def p80_372():
    '''
    def dayInYear(year, month, day):#定义某月某日距离一年的第一天已经过去了多少天，以下均用if则是为了将天数累加
        totalDay = day #如果为1月，那么距离某年的开始就为日的日期
        if month >= 2:#如果月份为2或以上，在原来的基础上加31，假设现在的月份为2，即1月的天数加上2月现在的过去的天数，结果，过去了31+day天
            totalDay += 31#在原来的基础加上31
        if month >= 3:
            totalDay += 29 if isLeapYear(year) else 28#计算闰年
        if month >= 4:
            totalDay += 31
        if month >= 5:
            totalDay += 30
        if month >= 6:
            totalDay += 31
        if month >= 7:
            totalDay += 30
        if month >= 8:
            totalDay += 31
        if month >= 9:
            totalDay += 31
        if month >= 10:
            totalDay += 30
        if month >= 11:
            totalDay += 31
        if month >= 12:
            totalDay += 30
        return totalDay#已经废弃的原版垃圾代码，起因是这坨东西太大挡着我了，下面写了个极简版
    '''
    def isLeapYear(year):  # 用以判断是否为闰年的函数
        # 当为闰年时，会返回True,否则，返回False；闰年：可被400整除，如果为非整百年，则可被4整除
        return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

    def dayPerMonth(year, month):  # 用以计算在一年中某月有多少天
        dayInMonth = 30  # 一般情况下为30天
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:  # 如果传入的月份为1,3,5,7,8,10,12，则为31天
            dayInMonth = 31
        elif month == 2:  # 如果为2月
            # 快捷语句写法，如果isLeapYear为True，则day为29，否则为28
            dayInMonth = 29 if isLeapYear(year) else 28
        return dayInMonth  # 返回dayInMonth变量的值

    def dayInYear(year, month, day):  # 用以计算某月某日距离某年的第一天已经过去了多少天
        totalDay = day  # 将传入的天数设为基础天，并将totalDay作为累加器
        for perMonth in range(1, month):  # 由于已设置基础天，将变量perMonth的范围从1开始到小于传入的月份
            # 将年和月传入dayPerMonth，用以计算某个月有几天，并将算出的天累加
            totalDay += dayPerMonth(year, perMonth)
        return totalDay  # 计算完后返回总天数

    def weekOfDay(year, month):  # 用以计算每月的开始是星期几
        #(公元元年开始至某年过了的年数) + (神秘的闰年计算公式)
        DuringSinceFirstYear = (year-1) + (year-1)//400 + (year-1)//4 - (year-1)//100 \
            + dayInYear(year, month, 1)  # + 距离指定年月的年始过去了多久
        # 由于公元元年1月1日为星期一，因此除以7得到的余数为0则是星期天，1则是星期一...
        return DuringSinceFirstYear % 7

    def output(year, month):  # 用以调用和输出各项的结果
        weekADay = weekOfDay(year, month)  # 得到每月的开始是星期几
        dayInMonth = dayPerMonth(year, month)  # 得到每个月有几天
        print("% -6s% -6s% -6s% -6s% -6s% -6s% -6s" %
              ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"))  # 输出顶栏星期一至星期日，并且每项输出均保持在6个字符，右侧输出空格用以对齐
        for w in range(weekADay):  # 用以给每月开始之日所属的星期留空，范围为从0到不大于输入数值
            print("% -6s" % " ", end="")  # 每个数值的输出均保持在6个字符，右侧输出空格用以对齐
        for day in range(1, dayInMonth + 1):  # 用以输出每个月的日期，范围为从1到不大于某月的最大日
            # 输出day变量，每个数值的输出均保持在6个字符，右侧输出空格用以对齐，将默认换行符替换为空，即不换行
            print("% -6d" % day, end="")
            weekADay = weekADay + 1  # 每当完成一次输出，星期数加1
            if weekADay % 7 == 0:  # 如果输出的下一个数值为7的倍数，即输出的日期为星期日
                print()  # 换行以输出下一周的日期
    # 最终调用
    year = int(input("year:"))
    for month in range(1, 13):
        print()
        print("--------------", year, "年", month, "月---------------")
        output(year, month)
        print()
    # 调用的层次结构：input -> output(for) -> weekOfDay -> dayInYear -> dayPerMonth(for) -> isLeapYear; input -> dayPerMonth -> isLeapYear;


# p80_372()


def p84_exercise():

    # def exercise1():   低能题，无解

    def exercise2():

        def jumpCount(max):
            number = -1
            for loop in range(0, max):
                number = number + 2
            return number

        total = 0
        for tick in range(1, 100):
            if jumpCount(tick) > 100:
                return total
            total = total + 1 / jumpCount(tick)

    exercise2()

    def exercise3():
        upper, lower = 0, 0
        string = str(input("输入一串字符，判断有多少个大写或小写字母"))
        for everyChar in string:
            if everyChar.isupper():
                upper += 1
            elif everyChar.islower():
                lower += 1
        print(f"有{upper}个大写字母, {lower}个小写字母.")

    exercise3()

    def exercise4():

        # 定义用以计算斐波拉契数列的函数；斐波拉契数列：在一个数列中。某个数的值为为前面两个数值之和，即在斐波拉契数列1,2,3,5...中，3由1+2得出，5由2+3得出
        def Fibonacci(sequence):
            firstNum, secondNum = 0, 1  # 首先定义前2个和前1个为最开始的两位数
            for queue in range(sequence):  # 创建一个for循环，用以计算第sequence个斐波拉契数列的数为多少
                total = firstNum + secondNum  # 将第一个数与第二个数相加，得到第三个数
                firstNum = secondNum  # 为了下一次循环的计算，由于创建了第三个数，因此定义了第一个数的firstNum变量往后进一位，也就是secondNum所处的数值
                secondNum = total  # 在firstNum完成了对secondNum的缓存后，secondNum也往后进位，也就是total的变量
            return secondNum  # 在完成循环后，返回secondNum，也就是total的值

        total = 0
        for i in range(2, 22):  # 由于2/1的为斐波拉契数列的第二个，因此从2开始循环，21之后结束
            cal = Fibonacci(i) / Fibonacci(i-1)  # 获取斐波拉契数列的某位为多少
            total = total + cal  # 累加
        print(f"计算结果为{total}")

    exercise4()

    def exercise5():
        score, tick, total = 0, 0, 0
        while True:
            if tick == 0:
                score = float(input("计算学生的平均分，输入错误的分数以结束:"))
            else:
                score = float(input(f"第{tick+1}个学生"))
            if score < 0 or score > 100:
                break
            tick += 1
            total += score

        print(f"平均分为{total / tick}")

    exercise5()

    def exercise6():
        def accurateDivide(dividen, divisor, accurate):
            remaind = dividen % divisor
            if remaind != 0:
                afterDecimal = "."
                tick = 0
                while remaind != 0 and tick < accurate:  # 当包含小数以及计数器小于设定值时，执行以下循环
                    # 将余数与除数相除，得出确切整数部分，并将其添加在结果后方
                    afterDecimal += str(10 * remaind // divisor)
                    remaind = remaind * 10 % divisor
                    tick += 1  # 计数器加1
                print(f"{dividen}/{divisor}={dividen//divisor}{afterDecimal}")
            else:
                print(f"{dividen}/{divisor}={dividen/divisor}")

        print("输入整数的被除数和除数，计算它们的精确值")
        accurateDivide(int(input("被除数：")), int(input("除数")), int(input("精确度")))

    exercise6()

    def exercise7_solution1():  # 方法1：for循环，直到找到符合条件的值
        total = 0
        while True:
            total += 1
            least = total
            tick = 0
            for day10 in range(10):
                tick += 1
                least = (least / 2) - 1
            if least == 1 and tick == 10:
                print(f"总共有{total}个桃子")
                break

    exercise7_solution1()

    def exercise7_solution2():  # 方法2：逆推得出结果
        least = 1
        for i in range(10):
            least = (least + 1) * 2
        print(f"总共有{least}个桃子")

    exercise7_solution2()

    def exercise8():
        tick, total = 0, 0
        while tick < 20:
            tick += 1
            firstNum, secondNum = 0, 1
            for queue in range(tick):
                firstNum, secondNum = secondNum, firstNum + secondNum
            total += secondNum
        print(total)

    exercise8()

    def exercise9():

        for every in range(1000):
            tick, total = 1, 0
            string = str(every) + "="
            while tick < every:
                if every % tick == 0:
                    string += str(tick) if tick == 1 else "+" + str(tick)
                    total += tick
                tick += 1
                if total == every:
                    print(string)
                    break

    exercise9()

    def exercise10():
        numbers1 = []  # 创建一个列表1
        for tick in range(500, 1500):  # 得出在500-1000可能的人数
            if tick % 7 == 3 and tick % 5 == 2 and tick % 3 == 1:
                numbers1.append(tick)  # 将可能的人数加入列表1
        # 创建一个列表2，得到的数为被1000减去的绝对值，即越小越接近1000
        numbers2 = [abs(1000 - every) for every in numbers1]
        # numbers2.index(min(number2))求出在列表2最小的数的索引，即最接近1000的数的索引，由于列表1和列表2的顺序对应，因此得到索引为3后，将其传入前部numbers1[]，得到位于同一索引的原始数值，即最接近1000的数，并输出
        print(numbers1[numbers2.index(min(numbers2))])

    exercise10()

    def exercise11():
        tick = 0
        while True:
            hua, mon = 12, 32
            tick += 1
            hua += tick
            mon += tick
            if hua * 2 == mon:
                print(tick, "年后他的岁数是他母亲的一半")
                break

    exercise11()

    def exercise12():
        for loop1 in "x", "y", "z":  # 用以定义a可能与谁打
            for loop2 in "x", "y", "z":  # 用以定义b可能与谁打
                for loop3 in "x", "y", "z":  # 用以定义c可能与谁打
                    if loop1 != loop2 != loop3 and loop1 != loop3:  # 用以过滤掉相同的结果，即a,b,c不可能与同一个人打
                        if loop1 != "x" and loop3 != "x" and loop3 != "z":  # 用以过滤掉特别的人选
                            print(f"a与{loop1}, b与{loop2}, c与{loop3}")  # 输出最终结果

    exercise12()

    def exercise13():
        earth, tick = 60, 0
        while True:
            if earth >= 80:
                print(f"{tick}年后地球达到80亿人")
                break
            earth *= 1 + 0.015
            tick += 1

    exercise13()

    def exercise14():
        height, tick, total = 80, 0, 80
        while tick < 10:
            height /= 2
            total += height * 2
            tick += 1

        print(f"{total},{height}", tick)

    exercise14()

# p84_exercise()


def p88_412_1():
    print(len("abc"))  # 每个中文、字母、空格等字符的长度均为1
    print(len("你好abc"))
    print(len("你好 abc"))


# p88_412_1()


def p88_412_2():
    string = "你好 abc"
    count = len(string)  # 计算字符串的字符数
    for i in range(count):  # 以字符串数量为目标，建立用于遍历每个字符的循环
        # 将每个字符作为单独的输出，[]内数值为索引号，即0为第一个字符，1为第二个字符，由于i随循环增大，因此起到遍历的效果
        print(string[i])


# p88_412_2()


def p89_412_3():
    string = "Hi,你好"
    count = len(string)
    for i in range(count):  # 遍历字符串
        # ord即ordinal序数，用以返回一个字符的序数；也就是说，每个字符都有自己的序号，如字符H在Unicode顺序中排第72位
        print(string[i], ord(string[i]))

    string1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 以下输出Aa-Zz，0-9的Unicode编码
    string2 = "abcdefghijklmnopqrstuvwxyz"
    string3 = "0123456789"
    for i in range(len(string1)):
        print(string1[i], "---", ord(string1[i]),
              string2[i], "---", ord(string2[i]))
    for i in range(len(string3)):
        print(string3[i], "---", ord(string3[i]))


# p89_412_3()


def p90_412_4():  # 将Unicode码转换为字符，使用chr函数
    a = chr(25105)
    b = chr(20204)
    c = chr(119)
    d = chr(101)
    print(a, b, c, d)


# p90_412_4()


def p90_412_5():  # 比较两个字符串的Unicode编码大小，a<b为-1,a>b为1,a=b为0

    def compare(string1, string2):  # 需要传入两个字符串进入函数
        length1 = len(string1)  # 得出字符串1的长度
        length2 = len(string2)  # 得出字符串2的长度
        if length1 < length2:  # 为了防止比较时位数多的一串无法与位数小的一串比较，即如果字符串1的长度小于字符串2
            minString = length1  # 将最小位数变量设为字符串1的长度
        else:  # 如果字符串2的长度小于或等于字符串1
            minString = length2  # 将最小位数变量设为字符串2的长度
        # 进入比较for循环；在Python中，大于、小于等比较符可以直接用以比较字符的Unicode大小，而不需要再次将字符转换为Unicode后比较；此for循环每次加1，是由于在字符串位数一样的情况下，开头最大的即为最大的字符串
        for i in range(minString):
            if string1[i] > string2[i]:  # 如果字符串1中某位的Unicode值大于字符串2中同一位的Unicode值，如xyz，abc中的x和a
                return 1  # 返回1给调用的函数，并中止函数
            elif string1[i] < string2[i]:  # 如果字符串1中某位的Unicode值小于字符串2中同一位的Unicode值，如abc，xyz中的a和x
                return -1  # 返回1给调用的函数，并中止函数
        # 如果直到for循环结束后仍未得出结果，即两个字符串的前部分均为相同，如abc,abc123；则开始比较位数，位数最大的即为最大
        if length1 == length2:  # 如果字符串1的长度等于字符串2，如abc,abc
            return 0  # 则返回0给调用的函数，并中止函数
        elif length1 > length2:  # 如果字符串1的长度等于字符串2，如abc123,abc
            return 1  # 则返回1给调用的函数，并中止函数
        else:  # 一旦非以上必然结果，即字符串1的长度小于字符串2，如abc,abc123
            return -1  # 则返回-1给调用的函数，并中止函数

    print(compare("abc123", "abc1234"))


# p90_412_5()


def p91_411():
    string = input("输入一串字符，计算它的大写字母数=")
    count = 0  # 初始化计数器
    for i in range(len(string)):  # 遍历字符串
        # 如果某个字符大于等于A或小于等于B，即某个字符的Unicode值为65-90，为大写字母所处的Unicode值区间时
        if string[i] >= "A" and string[i] <= "Z":
            count += 1  # 计数器加1
    print("大写字母的个数为", count)


# p91_411()


def p91_412():
    string = input("输入一串字符，计算它的大写、小写、数字有多少个=")
    upper, lower, digit = 0, 0, 0
    for i in range(len(string)):
        if string[i] >= "A" and string[i] <= "Z":  # 如果某个字符的Unicode值为65-90，为大写字母的Unicode区间时
            upper += 1  # 计数器加1
        # 如果某个字符的Unicode值为97-122，为小写字母的Unicode区间时
        elif string[i] >= "a" and string[i] <= "z":
            lower += 1  # 计数器加1
        if string[i] >= "0" and string[i] <= "9":  # 如果某个字符的Unicode值为48-57，为阿拉伯数字的Unicode区间时
            digit += 1  # 计数器加1
    print(f"大写字母{upper}个，小写字母{lower}个，数字{digit}个")


# p91_412()


def p92_413():  # 以下示例演示了如何使用相同的结构得出不同的结果

    def reverse(string):  # 定义字符串反转
        outString = ""  # 定义outString变量为字符串变量
        for i in range(len(string)-1, -1, -1):  # 建立递减循环，从字符串从0开始计算的长度到0，向下每次递减1
            # 每次向输出变量添加一个字符，即将原字符串从后往前遍历，并依次附加至outString变量
            outString = outString+string[i]
        return outString  # 处理后返回结果

    def noReverse(string):  # 定义纯字符串遍历
        outString = ""
        for i in range(0, len(string)):  # 建立递增循环，从0到字符串的长度，每次递增1
            # 每次向输出变量添加一个字符，即将原字符串遍历，并依次附加至outString变量，也就是说，将字符串拆分，缝合后得到与原字符串一致的字符串
            outString = outString+string[i]
        return outString  # 返回结果

    print(reverse("reverse"))
    print(noReverse("reverse"))


# p92_413()


def p92_414():

    def spaceTrim(string):  # 定义用以修剪左右空格的函数
        outPut = ""  # 定义用以输出的变量为字符串
        tick = 0  # 设置计数器的值为0
        stringLength = len(string) - 1  # 确定字符串的函数长度
        # 当计数器的值小于等于字符串长度以及位于计数器指定位置的某字符为空格时，即前位有空格时，计数器+1，由于采用计数器来确定某指定位置的字符值，因此每次计数器+1，字符位置会转到下一个字符，如果不为空格，则终止加算
        while tick <= stringLength and string[tick] == " ":
            tick += 1
        # 当计数器的值小于等于字符串长度以及位于字符串长度的值的字符为空格时，即当最后的字符为空格时，最终字符串长度-1，由于采用字符串长度方式来确定最后一个值，在字符串长度-1后，倒数第二个空格会成为最后一位的空格，直到最后的字符不为空格
        while tick <= stringLength and string[stringLength] == " ":
            stringLength -= 1
        # 建立循环，从先前确定的计数器值到结尾的最终数值，也就是说，最后遍历得出的字符串为前部与后部均不含空格的字符串
        for i in range(tick, stringLength + 1):
            outPut += string[i]  # 将遍历后的结果附加进outPut变量内
        return outPut

    string = input("输入一个左右具有空格的字符串：")
    print(f"{string}的长度是{len(string)}")
    string = spaceTrim(string)
    print(f"修剪后是{string}，长度是{len(string)}")


# p92_414()


def p93_412_6():
    string = "P"  # 定义字符串为大写P
    # 使用Unicode数值偏移来将小写转为大写，字符A为65，字符P为80，字符a为97，字符p为112，由于字符A与字符a的相隔32位的距离，因此P与p也相隔32位
    # a-A的Unicode值32，再加上字符P的Unicode值80，得出112即p的Unicode值，再通过chr函数将Unicode值转为字符
    lower = chr(ord("a") - ord("A") + ord(string))
    print(lower)


# p93_412_6()


def p93_415():

    def transLowerToUpper(string):  # 定义将小写全部转为大写
        outPut = ""
        for i in range(len(string)):  # 为字符串创建遍历
            if string[i] >= "a" and string[i] <= "z":  # 如果字符在a-z之间，即字符为小写
                # 将字符进行Unicode计算，得出某小写字母转换为大写字母的Unicode码，并将Unicode解码至字符
                outPut += chr(ord("A") - ord("a") + ord(string[i]))
            else:
                outPut += string[i]  # 如果不为小写，则直接将该字符加入结果，而不作改变
        return outPut

    def transUpperToLower(string):  # 定义将大写全部转为小写
        outPut = ""
        for i in range(len(string)):  # 为字符串创建遍历
            if string[i] >= "A" and string[i] <= "Z":  # 如果字符在A-Z之间，即字符为大写
                # 将字符进行Unicode计算，得出某大写字母转换为小写字母的Unicode码，并将Unicode解码至字符
                outPut += chr(ord("a") - ord("A") + ord(string[i]))
            else:
                outPut += string[i]  # 如果不为大写，则直接将该字符加入结果，而不作改变
        return outPut

    string = input("请输入一串具有字母的字符串：")
    print(f"将输入全部转为大写，{transLowerToUpper(string)}")
    print(f"将输入全部转为小写，{transUpperToLower(string)}")


# p93_415()


def p94_416():

    # 子串：字符串其中任意一段连续字符，如"apple"的字串可以是"appl","app","pl","e",""(空)...
    def subString(string, start, length):
        stringLength = len(string)  # 定义原字符串长度
        outPut = ""
        tick = start  # 将子串的计数器设为原字符串中指定位置
        # 当子串的计数器小于子串结尾(子串开始的位置加上子串长度)，以及计数器小于原字符串长度时
        while tick < start + length and tick < stringLength:
            outPut += string[tick]  # 将原字符串的第某位开始附加至outPut变量，子串截止长度由while循环控制
            tick += 1  # 遍历时每次向后一位
        return outPut  # 返回子串的值

    string = "abcdefghijk"
    print(subString(string, 4, 2))  # 字符串从0开始的第二个，即c，长度为4
    print(subString(string, 2, 24))  # 字符串从0开始的第二个，即c，长度为24，也就是字符串的全部


# p94_416()


def p95_413_1():  # 判断是否为对称型字符串，反转法

    def reverse(string):  # 定义用以反转的函数
        outPut = ""
        for i in range(len(string)-1, -1, -1):  # 从后往前遍历
            outPut += string[i]  # 并将遍历的字符合并为字符串
        return outPut  # 返回反转后的字符串

    def isSymmetry(string):  # 定义用以判断是否为对称型的函数
        reversed = reverse(string)  # 将字符串反转
        if string == reversed:  # 如果原字符串等于反转后的字符串，例如原字符串为"abccba","abcba"
            return 1  # 则返回1，即为对称型
        else:
            return 0  # 否则返回1，为非对称型

    string = input("输入一个字符串，判断是否为对称型字符串：")
    if isSymmetry(string):
        print("对称")
    else:
        print("不对称")


# p95_413_1()


def p95_413_2():  # 判断是否为对称型字符串，同时遍历法

    def isSymmetry(string):  # 定义用以判断是否为对称型的函数，方法为两侧同时向中心靠拢，比较两侧开始第某位数值是否相同
        tick = 0  # 左侧计数器置0
        stringLength = len(string) - 1  # 右侧计数器为字符串的函数长度
        while tick <= stringLength:  # 当左侧计数器大于右侧计数器时停止，即当左侧的字符串位置超过右侧的字符串位置时停止遍历，如"abcba",左侧"abc",右侧"abc"，"abccba",左侧"abcc",右侧"abcc"
            if string[tick] != string[stringLength]:  # 如果两侧开始的第某位数值不相等
                return 0  # 那么这个字符串不为对称型字符串，返回0
            tick += 1  # 左侧每次+1，即每次循环时向中心靠拢1格
            stringLength -= 1  # 右侧每次-1，即每次循环时向中心靠拢1格
        return 1  # 如果中途未因字符不同停止，那么返回1，即为对称型字符串

    string = input("输入一个字符串，判断是否为对称型字符串：")
    if isSymmetry(string):
        print("对称")
    else:
        print("不对称")


# p95_413_2()


# 对于字符串变量string，有string[start:end:step]，即子串的开始，结尾，每隔几个字符才输出一个字符，并引出索引的概念，即第一个字符的索引号为0，第二个为1......
def p96_422():
    string = "abcdefghijk"  # 一共11个字符，索引号最大为10
    print("string----", string)
    # 开始的索引号为0，结尾的索引号为2，即选择字符串中索引号包括0的小于2的索引号所替代的字符，也就是0,1，即a,b
    print("string[0:2]----", string[0:2])
    print("string[:2]----", string[:2])  # 如果不指定开始，则选定索引号为2之前的所有字符
    print("string[2:]----", string[2:])  # 如果不指定结尾，则选定索引号为2之后的所有字符
    print("string[2:6]----", string[2:6])  # 选定索引号为从2到6之间的所有字符
    print("string[:]----", string[:])  # 不指定任何，相当于直接输出string
    # 使用半角冒号占位，仅指定步数，即每隔几个字符输出一次字符，不指定时默认为1，因此2则相当于每次隔2-1个字符输出一次
    print("string[::2]----", string[::2])
    print("string[0:7:2]----", string[0:7:2])  # 从开头开始，到索引号为6之间的所有字符，每次输出间隔1个字符
    print("string[8:14]----", string[8:14])  # 选定索引号8-14之间的字符，超过部分则略过，仅输出有效部分
    # 选定索引号1-5之间的字符"bcde"，每次间隔1个字符，即仅输出"bd"
    print("string[1:5:2]----", string[1:5:2])
    # 选定索引号1-4之间的字符"bcd"，每次间隔1个字符，即仅输出"bd"
    print("string[1:4:2]----", string[1:4:2])


# p96_422()


def p96_422_1():  # 对于字符串变量string，有string[start:end:step]，其中三个变量均可为负
    string = "abcdefghijk"  # 一共11个字符，索引号最大为10，反向索引号最大为-10
    print("string----", string)

    # 当使用负数索引时，一个字符可以有两个索引号，-1为字符串最后一位，即k，-2为j，由于索引默认为从左往右，因此得出的结果相当于string[0:9]
    print("string[0:-2]----", string[0:-2])

    # 如果不指定开始，则选定索引号为-2之前的所有字符，等同于string[:9]
    print("string[:-2]----", string[:-2])

    # 如果不指定结尾，则选定索引号为-2之后的所有字符，等同于string[9:]
    print("string[-2:]----", string[-2:])

    # 选定索引号为从-2到6之间的所有字符，等同于string[9:6]，由于步长默认为正，因此不会有任何输出；(详见倒数四行代码的解释)
    print("string[-2:6]----", string[-2:6])

    print("string[:]----", string[:])  # 不指定任何，相当于直接输出string

    # 使用半角冒号占位，即当选定的子串为字符串本身时，步数可以为正或负，如果步数为负值，则输出反转，并且间隔输出的方向均相反，因此从k开始，向左间隔输出
    print("string[::-2]----", string[::-2])

    # 对于开始为字符串的左侧，而结尾为字符串的右侧的子串，步长不能为负，否则无内容输出
    print("string[7:-1:-1]----", string[7:-1:-1])

    # 对于开始为字符串的右侧，而结尾为字符串的左侧的，步长不能为正，否则无内容输出
    print("string[8:0:-1]----", string[8:0:-1])

    # 对于开始为字符串的右侧，而结尾为字符串的左侧的，步长为负，并且每次间隔1个字符
    print("string[5:1:-2]----", string[5:1:-2])

    # 对于开始为字符串的右侧，而结尾为字符串的左侧的，步长为负，并且每次间隔1个字符
    print("string[4:1:-2]----", string[4:1:-2])


# p96_422_1()


def p98_422_2():
    string = "Python(version4.5) is easy"  # 创建一个具有英文大小写字符的字符串
    # 对字符串使用lower()方法，即将原字符串中所有的大写字符转为小写，而其他字符则不作处理，并将对字符串处理过后的结果输出
    print(string.lower())
    # 对字符串使用upper()方法，即将原字符串中所有的小写字符转为大写，而其他字符则不作处理，并将对字符串处理过后的结果输出
    print(string.upper())
    print(string)  # 输出原本字符串


# p98_422_2()


def p98_422_3():
    string = "12abcabcab"  # 字符串的最大索引为9，对于搜索字符串ab，匹配的索引号有2,5,8
    # 对原字符串使用find()方法，即向字符串搜索某个或某串字符，如果有多个结果，则输出位于原字符串最左侧的结果的索引号；也就是从左往右查找，一旦出现一串与搜索内容匹配的字符串，则输出在原字符串中那个字符串第一个字符的位置
    ab = string.find("ab")  # 如ab，在原字符串中索引号为2
    abd = string.find("abd")  # 如果搜索无结果，即字符串中没有要搜索的那个字符，则返回-1
    print(ab, abd)  # 对string进行操作后的结果均已赋值于这两个变量，输出它们


# p98_422_3()


def p99_422_4():  # rfind中，r为right的意思，即从右往左开始查找
    string = "12abcabcab"  # 字符串的最大索引为9，对于搜索字符串ab，匹配的索引号有2,5,8
    ab = string.rfind("ab")  # 从右往左开始查找，如果有多个结果，则输出位于最右侧的结果的索引号，即8
    abd = string.rfind("abd")  # 与find()一样，如果搜索无结果，则返回-1
    print(ab, abd)


# p99_422_4()


def p99_422_5():  # index()与find()函数的实现功能相同，但在index中，一旦搜索的字符串不存在，则直接中止程序，并抛出“未找到指定子串”的错误
    string = "12abcabcab"
    ab = string.index("ab")
    abd = string.index("abd")
    print(ab, abd)


# p99_422_5()


def p99_422_6():
    string = "12abcabcab"
    ab = string.startswith("12a")  # startswith()方法用以判断原字符串是否以某字符串开始
    abd = string.endswith("ab")  # endswith()方法用以判断原字符串是否以某字符串结尾
    print(ab, abd)  # 执行方法后的结果为布尔值True或False

    def myStartsWith(string, wantFind):  # 自制startswith函数
        stringIndex = string.find(wantFind)  # 首先得出某字符串在原字符串最左侧的索引
        if stringIndex == 0:  # 如果索引为0，即搜索结果为字符串的开头
            return True
        else:  # 向调用的代码传出结果
            return False

    def myEndsWith(string, wantFind):  # 自制endswith函数
        stringIndex = string.rfind(wantFind)  # 首先得出某字符串在原字符串最右侧的索引
        # 必须确保索引不为负，即原字符串存在搜索结果，且搜索结果的位置与公式计算相同，即rfind的结果等于原字符串长度减去搜索字符串的长度
        if stringIndex >= 0 and stringIndex == len(string) - len(wantFind):
            return True
        else:  # 向调用的代码传出结果
            return False

    # 函数与方法的使用方式不同，方法可以在一个变量后加“.”使用，方法也相当于这个被加“.”的变量的自有属性，如：variable.myfunction()
    # 而函数则需要手动传入变量，如：myfunction(variable)

    ab1 = myStartsWith(string, "12a")
    abd1 = myEndsWith(string, "ab")
    print(ab1, abd1)


# p99_422_6()


def p100_422_7():  # 在lstrip,rstrip,strip中，l意为left，r意为right，strip意为去除、剥离
    string = "   ab x yz "
    lstrip = string.lstrip()  # 剥离左侧的空字符
    rstrip = string.rstrip()  # 剥离右侧的空字符
    strip = string.strip()  # 剥离两侧的空字符
    print(lstrip, len(lstrip))
    print(rstrip, len(rstrip))
    print(strip, len(strip))
    print(string, len(string))


# p100_422_7()


def p101_422_8():  # split意为分离、分裂
    string = "I am learning Python"
    # 对于split()方法，括号内默认将传入字符串值作为分隔符，相当于.split(sep="")，并将被分开的字符串组成一个列表
    split = string.split(" ")
    print(split)

    # 将ear作为分隔符，分为"I am l"和"ning Python"，即把"learning"中的"ear"去除后，将两个原本并不连续的字符串分开
    split2 = string.split("ear")
    print(split2)

    # 由于字符串首为ab，如将ab作为分隔的依据，结果出会现一个空字符串，因为分隔实际上是将分隔符左侧进行提取，而字符串首部ab左侧无任何字符，因此方法只能输出一个空字符串，好处是可用于判断字符串首是否包含了分隔符
    string2 = "abcabcabc"
    split3 = string2.split("ab")
    print(split3)


# p101_422_8()


def p102_421():

    def myLower(string):
        outPut = ""
        for i in range(len(string)):  # 为字符串创建遍历
            if string[i] >= "A" and string[i] <= "Z":  # 如果字符在A-Z之间，即字符为大写
                # 将字符进行Unicode计算，得出某大写字母转换为小写字母的Unicode码，并将Unicode解码至字符
                outPut += chr(ord("a") - ord("A") + ord(string[i]))
            else:
                outPut += string[i]  # 如果不为大写，则直接将该字符加入结果，而不作改变
        return outPut

    # 比较方法与函数间相同的功能实现
    string = "aABEbwWFEW"
    a = string.lower()
    b = myLower(string)
    print(a)
    print(b)


# p102_421()


def p102_422():

    def myStrip(string):
        outPut = ""  # 定义用以输出的变量为字符串
        tick = 0  # 设置计数器的值为0
        stringLength = len(string) - 1  # 确定字符串的函数长度
        # 当计数器的值小于等于字符串长度以及位于计数器指定位置的某字符为空格时，即前位有空格时，计数器+1，由于采用计数器来确定某指定位置的字符值，因此每次计数器+1，字符位置会转到下一个字符，如果不为空格，则终止加算
        while tick <= stringLength and string[tick] == " ":
            tick += 1
        # 当计数器的值小于等于字符串长度以及位于字符串长度的值的字符为空格时，即当最后的字符为空格时，最终字符串长度-1，由于采用字符串长度方式来确定最后一个值，在字符串长度-1后，倒数第二个空格会成为最后一位的空格，直到最后的字符不为空格
        while tick <= stringLength and string[stringLength] == " ":
            stringLength -= 1
        # 建立循环，从先前确定的计数器值到结尾的最终数值，也就是说，最后遍历得出的字符串为前部与后部均不含空格的字符串
        for i in range(tick, stringLength + 1):
            outPut += string[i]  # 将遍历后的结果附加进outPut变量内
        return outPut

    # 比较方法与函数间相同的功能实现
    string = " a b    "
    a = string.strip()
    b = myStrip(string)
    print(a, len(a))
    print(b, len(b))


# p102_422()


def p103_423():

    def mySplit(string, sep):
        sepNum = string.find(sep)  # 先行寻找位于最左侧的分隔符的索引
        list = []  # 创建列表
        while sepNum >= 0:  # 当分隔符在字符串中存在时，即find()的结果不为-1时
            splitPart = string[0:sepNum]  # 将获取首位分隔符左侧的内容
            list.append(splitPart)  # 并加入至列表中
            string = string[sepNum+len(sep):]  # 将字符串进行修剪，即将已附加至列表的字符串部分和分隔符去除
            # 在修剪过后的字符串中查找下一个分隔符的索引号；当字符串中无分隔符时，find()返回-1至sepNum中，退出循环
            sepNum = string.find(sep)
        list.append(string)  # 一旦字符串内的分隔符均已处理完毕，如果最后的分隔符右方仍有字符，则将右侧剩余的字符加入列表
        return list

    # 比较方法与函数间相同的功能实现
    string = "abcababcab"
    a = string.split("a")
    b = mySplit(string, "a")
    print(a, b)


# p103_423()


def p104_423():

    def myFind(string, wantFind):
        stringLength = len(string)  # 确认字符串的长度
        findLength = len(wantFind)  # 确认要查找的关键字的长度
        if stringLength < findLength:  # 如果关键字的长度比字符串还长
            return -1  # 直接返回无效值-1
        tickIndex = 0  # 初始化用以对齐的字符串索引号
        # 第一层while实现查找关键字在原字符串的索引号
        while tickIndex <= stringLength - findLength:  # 如果字符串索引大于原字符串长度减去关键字长度，即如果剩余索引的数量小于关键字长度也仍未有结果，结束while循环
            tickAlign = 0  # 初始化对齐计数器
            while tickAlign < findLength:  # 实现原字符串的某部分与关键字一一比对，如果即使对齐计数器大于等于索引长度也仍未有结果，结束第二层while循环
                # 如果对齐后某个字符与关键字内的不同，有可能是匹配完毕，也有可能是对齐不正确；通过tickIndex实现原字符串与关键字的对齐，通过tickAlign实现原字符串与关键字的进位相同
                if string[tickIndex + tickAlign] != wantFind[tickAlign]:
                    break  # 退出while，检测关键字是否比对成功
                tickAlign += 1  # 否则将对齐后的字符串与关键字向右进位继续比较
            if tickAlign == findLength:  # 如果比对成功的长度等于关键字长度
                return tickIndex  # 返回关键字在原字符串的索引
            tickIndex += 1  # 如果第二层while无结果，将对齐索引往右进一位
        return -1  # 返回无效值-1

    # 比较方法与函数间相同的功能实现
    string = "ababcabcd12ab"
    print(myFind(string, "abc"), string.find("abc"))
    print(myFind(string, "ad"), string.find("ad"))


# p104_423()


def p105_432_1():
    list = ["a", "b", "c", "d"]
    print(list)
    print(type(list))  # type()函数用于列出一个变量的类型，变量list的类型为列表


# p105_432_1()


def p105_432_2():  # 与字符串类似，列表也能使用索引，用以定位列表中的每个字符串
    # 数字和布尔值等内置常量可无需加引号，一般地，如果一串字符未被引号括起，则被视为一个变量
    list1 = ["physics", "chemistry", 1997, 2000]
    list2 = [1, 2, 3, 4, 5, 6, 7]
    print("list1[0]:", list1[0])  # 输出列表中的第一个项的值
    print("list2[1:5]:", list2[1:5])  # 输出列表中第二个到第五个项的值，按列表方式编排


# p105_432_2()


def p106_432_3():
    list = ["physics", "chemistry", 1997, 2000]
    print("在list索引号为2的位置上的值是：")
    print(list[2])
    list[2] = 2001  # 可直接更改某个项的值，即在确定某个值后，直接使用“=”以进行更改
    print("在list索引号为2的位置上的新值是：")
    print(list[2])


# p106_432_3()


def p106_432_4():
    list = ["physics", "chemistry", 1997, 2000, 2017]
    print(list)
    del list[2]  # del可用于删除某个变量或变量内的项
    print("在删掉索引2的值后的列表")
    print(list)


# p106_432_4()


def p107_432_5():
    list1 = ["a", "b"]
    list2 = ["c", "a"]
    list3 = list1 + list2  # 可通过加法符号运算将两个列表合并
    print(list3)


# p107_432_5()


def p107_431():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print(list[0:2])
    print(list[:2])
    print(list[2:])
    print(list[2:-1])
    print(list[:])
    print(list[::2])
    print(list[0:7:2])
    print(list[7:0:-2])
    print(list[8:14])


# p107_431()


def p108_432():  # 与字符串相同，列表也能经过裁切获得子列表，以及对于step的正负理解均相同，用例list[start:end:step]
    list = ["a0", "a1", "a2", "a3", "a4", "a5",
            "a6", "a7", "a8", "a9"]  # 列表内有10个字符串，最大索引号为9
    print("list----", list)
    # -2为列表倒数第二位，即a8，由于索引默认为从左往右，因此得出的结果相当于list[0:8]
    print("list[0:-2]----", list[0:-2])
    print("list[:-2]----", list[:-2])  # 如果不指定开始，则选定索引号为-2之前的所有项，等同于list[:8]
    print("list[-2:]----", list[-2:])  # 如果不指定结尾，则选定索引号为-2之后的所有项，等同于list[8:]
    # 选定索引号为从-2到6之间的所有项，等同于list[8:6]，由于步长默认为正，因此不会有任何输出
    print("list[-2:6]----", list[-2:6])
    print("list[:]----", list[:])  # 不指定任何，相当于直接输出list
    # 使用冒号占位，即当选定的子列表为列表本身时，步数可以为正或负，如果步数为负值，则输出反转，并且间隔输出的方向均相反，因此从a9开始，向左间隔输出
    print("list[::-2]----", list[::-2])
    # 对于开始为列表的左侧，而结尾为列表的右侧的子列表，步长不能为负，否则无内容输出
    print("list[7:-1:-1]----", list[7:-1:-1])
    # 对于开始为列表的右侧，而结尾为列表的左侧的子列表，步长不能为正，否则无内容输出
    print("list[8:0:-1]----", list[8:0:-1])
    # 开始为列表的右侧，结尾为列表的左侧的子列表，步长为负，并且每次间隔1个字符
    print("list[5:1:-2]----", list[5:1:-2])
    # 开始为列表的右侧，结尾为列表的左侧的子列表，步长为负，并且每次间隔1个字符
    print("list[4:1:-2]----", list[4:1:-2])


# p108_432()


def p108_432_7():  # 与字符串一样，列表也可以使用in等判断操作，返回的是布尔值True或False
    list = ["a", "b", "c", "d"]
    print("a" in list)  # 在in情况下的字符串不会作为标准输出被输出，而是会被处理后返回布尔值
    print("A" in list)
    print("A" not in list)


# p108_432_7()


def p109_433_1():
    list = [123, "xyz", "zara", "abc"]
    list.append(2009)  # append意为附加，即字面意义上，append()方法用以向列表最右侧添加一项内容
    print("列表已更新：", list)


# p109_433_1()


def p109_433_2():  # count()方法用以在列表里查找某个项目有几个，count()方法必须指定一个需要查找的项
    list = [123, "xyz", "zara", "abc", 123]
    print("字符串123的数量是：", list.count(123))
    print("字符串zara的数量是：", list.count("zara"))
    print("字符串abc的数量是：", list.count("abc"))


# p109_433_2()


def p110_433_3():
    list1 = [123, "xyz", "zara", "abc", 123]
    list2 = [2009, "manni"]
    list1.extend(list2)  # extend，即延长、拓展，用以将原列表进行延长，可以添加可迭代对象(即列表，字典，元组，集合，字符串)
    print("延长列表：", list1)  # 另一种实现方法可以是list1 += list2


# p110_433_3()


def p110_433_4():
    list = [123, "xyz", "zara", "abc"]
    print("xyz的索引号是：", list.index("xyz"))  # index()方法用以查找某个项在列表中的索引号为多少
    print("zara的索引号是：", list.index("zara"))
    print("000的索引号是：", list.index("000"))  # 如果需要查找的内容不存在于列表中，程序会中止运行，并返回错误


# p110_433_4()


def p110_433_5():
    list = [123, "xyz", "zara", "abc"]
    # insert()方法用以插入某个项至列表，需要两个参数，第一个是希望插入的位置，第二个为需要插入的项目，list.insert(3,2009)意为将字符串项"2009"插入到list列表中索引号为3的位置，而原本处于那个位置的项则会向右移动一个索引号
    list.insert(3, 2009)
    print("插入到列表：", list)


# p110_433_5()


def p111_433_6():
    list = [123, "xyz", "zara", "abc", "xyz"]
    list.remove("xyz")  # remove()方法一次只能移除一个位于最左侧的项，类似于find()方法，从左侧开始查找某个项
    print("从列表中移除xyz：", list)
    list.remove("abc")
    print("从列表中移除abc：", list)
    list.remove("000")  # 如果需要移除的内容不存在于列表中，程序会中止运行，并返回错误


# p111_433_6()


def p111_433_7():
    list = [123, "xyz", "zara", "abc"]
    del list[2]  # del关键字可以依照索引号删除掉列表里的某项字符串
    print(list)


# p111_433_7()


def p111_433_8():
    list = ["a", "b", "c", "d"]
    list.pop()  # pop()方法用以抛弃列表内指定索引号的项目，pop()方法的索引号默认为-1，即抛弃掉列表中最右侧的一项
    print(list)
    list.pop(0)  # 指定要抛弃掉索引号为0的项
    print(list)


# p111_433_8()


def p112_433_9():
    list = [123, "xyz", "zara", "abc", "xyz"]
    list.reverse()  # 反转列表内项目的排序顺序，但列表内项目的内容不改变，与list[::-1]相同
    print(list)


# p112_433_9()


def p112_433_10():
    list1 = ["123", "xyz", "zara", "abc", "xyz"]
    list1.sort()  # 对于sort()方法，需要确保列表内每个项目都为同类项
    print("排序列表：", list1)
    # 对于某个含有多种类型的项目的列表，方法会无法比较，抛出错误并中止程序
    list2 = [1, 6, 3, 2, "a"]
    list2.sort()
    print("排序列表：", list2)


# p112_433_10()


def p113_433():  # 函数内对于列表的调用是全局性的，与普通的数字和字符串不同

    def fun(list, number, string):
        list.append(1)  # 对从函数外传入的列表进行更改，在最右侧加入数值1
        number = 1
        string = "changed"
        print("函数内的值：", list, number, string)

    list = [10, 20, 30]
    number = 0
    string = "try"
    fun(list, number, string)  # 将list传入函数
    print("函数外的值：", list, number, string)  # 在函数外也观测到列表被改动


# p113_433()


def p113_434():

    def fun():
        list = []  # 建立一个列表
        for i in range(10):  # 创建一个从1到9的循环
            list.append(i)  # 将循环附加进列表中
        return list  # 返回list变量的内容，包括类型

    list = fun()  # 使外部变量list等于fun()函数传出的内容
    print(list)


# p113_434()


def p113_435():
    provinces = ["广东", "四川", "贵州"]  # 定义省份列表
    # 定义城市列表；列表可以嵌套，此城市列表由三块列表组成一个大列表，每块列表可以顺序对应省份列表的每一项，想要获取列表内指定的项，需要进行两次索引，如cities[0][1]，选中了cities列表内第一块里的第二项，即深圳
    cities = [["广州", "深圳", "惠州", "珠海"], [
        "成都", "内江", "乐山"], ["贵阳", "六盘水", "遵义"]]

    def fromProvinceFindCity():  # 定义函数用以从省份查找城市
        findProvince = input("输入要查找的省份：")
        found = False  # 初始化查找状态变量
        for prov in range(len(provinces)):  # 从省份列表获得长度为3，确定省份列表内的最大索引号
            if provinces[prov] == findProvince:  # 遍历省份列表，如果有一项符合需要查找的省份
                print(provinces[prov], end=":")  # 输出那项省份，并加上冒号符
                # 用以输出省份下的城市，获得某省份下的城市列表的长度，并遍历
                for ci in range(len(cities[prov])):
                    print(cities[prov][ci], end=" ")  # 输出某省份下的城市，每次输出以空格结尾
                found = True  # 将查找状态改为真
                break  # 退出循环
        if not found:  # if对变量的判断默认为if True，在此条语句中意思是，如果found变量不是True，也就是说，如果found变量是False的话
            print("没有此省份")  # 输出未成功的结果

    def fromCityFindProvince():  # 定义函数用以从城市查找省份
        findCity = input("输入要查找的城市：")
        for ci in range(len(cities)):  # 遍历城市列表里的每块列表
            for each in cities[ci]:  # 遍历每块列表里的每项字串
                if each == findCity:  # 如果有一字串等于输入内容
                    print(findCity, "在", provinces[ci]+"省")  # 输出查找结果
                    return  # 退出循环
            print("查找失败")  # 如果直到遍历完所有城市均未有结果，输出此语句

    fromProvinceFindCity()
    fromCityFindProvince()


# p113_435()


def p116_441():  # 元组与列表类似，使用半角英文括号创建，并且元组内的数值为常量，不可改变
    tuple = (1, 3, 2, 3, 4, 5)
    print(tuple)
    print(type(tuple))


# p116_441()


def p116_442():
    week = ("日", "一", "二", "三", "四", "五", "六")
    print(week)
    day = int(input("输入一个0-6的整数，获取对于星期数："))
    if day >= 0 and day <= 6:
        print("星期"+week[day])  # 元组与列表类似，每个项均有索引号
    else:
        print("错误输入")


# p116_442()


def p117_443_U():

    # 在函数传入时，如果一个变量前带"*"号，那么这个变量是一个可选参数，该变量会创建一个元组，用以将位置参数和默认参数等之外的可选参数传入此变量，通常放在位置参数的后方，一般在函数传入时使用"fun(a,b,1,2,3,4)"传入，其中1,2,3,4会自动传入可选参数
    # 特别地，可以使用"fun(a,b,*(1,2,3,4))"来指定传入
    def fun(x, y, *args):
        print(x, y)
        print(args)

    # 在包含可选参数的函数定义下，位置参数不能被特别指定，所有传入的值必须按照函数定义的顺序来放置
    fun(1, 2)
    fun(1, 2, 3)
    fun(1, 2, 3, 4)
    fun(1, 2, (3, 4))


# p117_443_U()


def p117_443_D():

    def argsMax(*args):  # 函数argsMax有且仅有一个参数，可选参数args
        print(args)
        maxNum = args[0]  # 将最大数值初始化
        for i in range(len(args)):  # 遍历元组列表args
            if maxNum < args[i]:  # 如果现在最大的数小于某个位置的数
                maxNum = args[i]  # 将现在最大的数替换为那个位置的数
        return maxNum  # 返回最大值

    print(argsMax(1, 2))
    print(argsMax(1, 2, 3, 4))


# p117_443_D()


def p118_452():  # 字典类型使用花括号表示，字典类型为键值类型，由"键：值"组成，键可以理解为一个对象(变量)的属性，值则是这个对象的属性所含有的内容，键(属性)的名称实际应用上不能重复，而值则可以
    dict = {"Alice": "2341", "Beth": "9102", "Cecil": "3258"}  # 创建一个字典
    print(type(dict))  # 输出dict变量的类型


# p118_452()


def p119_452_1():
    dict = {"Name": "Zara", "Age": "7", "Class": "First"}
    # 通过方括号，可以达成类似索引的效果；在dict中查找键为Name的值，即Zara
    print('dict["Name"]', dict["Name"])
    print('dict["Age"]', dict["Age"])  # 在dict中查找属性(键)为Age的值，即7
    # 对于在字典中不存在的属性名，如果无法查询到结果，则抛出错误，并中止程序
    print('dict["Alice"]', dict["Alice"])


# p119_452_1()


def p119_452_2():  # 可以通过"="符来更改或添加字典
    dict = {"Name": "Zara", "Age": "7", "Class": "First"}
    dict["Age"] = 8  # 将字典内的Age属性设为8
    # 将字典内School属性的值设为SIT School，对于"="符，实际上起到了创建的效果
    dict["School"] = "SIT School"
    print('dict', dict)
    print('dict["Age"]', dict["Age"])
    print('dict["School"]', dict["School"])


# p119_452_2()


def p120_452_3():
    dict = {"Name": "Zara", "Age": "7", "Class": "First"}
    del dict["Name"]  # 通过del关键字，将字典内的Name属性删除，属性删除的同时也将Name属性下的值Zara删除
    print(dict)
    dict.clear()  # 可对字典使用clear()方法将字典清空
    print(dict)
    del dict  # del关键字同时也可以删除字典本身
    print(dict)  # 删除字典后无法输出，报错并中止


# p120_452_3()


def p120_452_4():
    # 字典原则上可以使用相同的键，但在键相同的情况下，输出时只会输出最右侧的的值；键可使用的种类有数值，字符串，元组，而值的种类可以是任意类型的值
    dict1 = {"Name": "Zara", "Age": "7", "Name": "Manni"}  # 一个包含了两个相同的键的字典
    # 在输出这个具有重复键的字典的指定重复键Name时，仅输出一个值，并且此值为且仅为字典最右侧的键Name包含的值
    print('dict1["Name"]', dict1["Name"])

    dict2 = {"Name": "Zara", (1, 2): "7"}  # 一个键中包含了元组的字典
    print('dict2[(1,2)]', dict2[(1, 2)])  # 将元组作为键是合规的，并且能正常查询到值
    dict2 = {["Name"]: "Zara", (1, 2): "7"}  # 将列表作为键是不合规的，程序会中止


# p120_452_4()


def p121_452_5():
    dict = {"name": "Zara", "Age": 7}
    print("长度：", len(dict))  # 在字典中，每个键值组合为一个长度


# p121_452_5()


def p121_452_6():
    dict = {"Name": "Zara", "Age": 7}
    print("初始长度：", len(dict))
    dict.clear()  # clear()方法可以清除字典内的所有内容，而不删除字典本身
    print("清除后长度：", len(dict))  # 字典仍存在，只是内容被清空


# p121_452_6()


def p121_452_7():
    dict = {"Name": "Zara", "Age": 7}
    print("字典的键有：", dict.keys())  # 使用key()方法可以输出字典内的所有键


# p121_452_7()


def p121_452_8():  # 对于get()方法，有get(key,default=None)，用于返回指定键的值，其中key为指定键，default定义了：如果指定键不存在，则输出default的值，默认为None，可手动传入
    dict = {"Name": "Zara", "Age": 27}
    print("值： % s" % dict.get("Age"))
    print("值： % s" % dict.get("Gender", "Never"))


# p121_452_8()


def p122_453():

    def studentList():
        global student
        student = []
        student.append({"Name": "张三", "Gender": "男", "Age": "20"})
        student.append({"Name": "李四", "Gender": "女", "Age": "21"})
        student.append({"Name": "王五", "Gender": "男", "Age": "22"})

    def seekStudent(Name):
        for i in student:
            if i["Name"] == Name:
                print(i["Name"], i["Gender"], i["Age"])
                return
        print(f"没有姓名为{Name}的人")

    global student

    studentList()
    seekStudent("张三")
    seekStudent("李四")


# p122_453()


def p123_461():  # 字典与列表一样，在函数内的调用具有全局性

    def fun(dict):
        dict["Name"] = "aaa"
        print("函数内部", dict)

    dict = {"Name": "Zara", "Age": 7}
    print("执行函数前", dict)
    fun(dict)
    print("执行函数后", dict)  # 键Name在执行函数后改变


# p123_461()


def p124_462():

    def createDict():  # 定义函数创建字典
        dict = {}  # 创建空字典
        dict["Name"] = "张三"  # 添加键Name，值张三
        dict["Age"] = 20  # 添加键Age，值20
        dict["Gender"] = "男"  # 添加键Gender，值男
        return dict  # 将被更改后的字典传出

    def output(dict):  # 定义函数遍历字典
        keys = dict.keys()  # 将字典中的所有属性汇成列表传至变量keys
        for key in keys:  # 遍历字典的所有属性
            print(key, dict[key])  # 输出属性和属性的值

    dict = createDict()  # dict变量接受从createDict内传出的字典
    print(dict)
    output(dict)


# p124_462()


def p125_463():
    # 在函数传入中，如果一个变量前带有两个"*"号，即"**kwargs"，那么这个变量是一个键值型可选参数(keyword arguments)，该变量会创建一个字典，并将识别到的键值参数传入此变量，在函数传入时使用"fun('key'='word')"传入键值参数
    # 特别地，可以使用"fun(**{'key':'word'})"来指定传入键值可选参数

    def fun(x, y=2, **kwargs):  # 在定义函数时，可选参数必须在位置参数的右侧
        print(x, y)
        print(kwargs)

    fun(1, 2)  # 变量kwargs在这种情况下不会被传入任何值
    fun(1, 2, z=3)  # 此时变量kwarg被传入z=3，即键为z，值为3
    fun(1, 2, a=3, b="demo")  # 向kwargs传入多个参数
    fun(x=1, y=2, z=3)  # 编译器会识别传入的键是否为函数已定义的位置参数或默认参数，是则将其传入至已定义的变量，否则传入键值参数
    fun(y=1, x=2, z=5, s="demo")  # 可以任意打乱顺序
    fun(z=3, x=1)  # 对于在函数内部已经定义了的变量x，即使其在键值参数的右侧，但编译器仍会将其自动传入进内部已被定义的变量x
    fun(x=1, y=2, **{"a": "lion"})


# p125_463()


def p125_464():

    def fun(x, y=2, *args, **kwargs):  # 在包含有两种可选参数的情况下，元组可选参数必须在键值可选参数左侧
        print(x, y)
        print(args)
        print(kwargs)

    fun(1, 2)  # 位置参数必须被定义
    fun(1, 2, 3, 4)  # 将位置参数和默认参数以外的数值加入元组
    fun(1, 2, 3, 4, s="demo")  # 将位置参数，默认参数以及可选参数以外的键值对加入字典
    fun(1, 2, *(3, 4), **{"a": "demo"})  # 对于拥有一般可选参数的函数定义*args，必须将传入的数值与函数定义对齐


# p125_464()


def p126_464():
    provinces = {}  # 创建用以存储省份的字典provinces

    def appendDict(province, city):  # 定义函数用以添加字典，函数包含了两个变量，即省份province以及省份的城市city，其中城市的数值类型为列表
        if province not in provinces.keys():  # 判断省份是否存在，如果不存在
            provinces[province] = city  # 向省份字典添加键为省份，值为城市列表的键值对
        else:  # 否则存在则返回已经存在
            print(province+"已经存在")

    def output():  # 定义函数用以输出字典内容
        for perProvince in provinces.keys():  # 遍历字典中的所有键
            print(perProvince, provinces[perProvince])  # 输出键，和键包含的值，即城市列表

    def seekProvince(province):  # 定义函数用以查找省份，需要传入的值为省名
        if province in provinces.keys():  # 如果省份存在于字典中的键
            print(province, end=":")  # 输出省份后以冒号结尾
            for city in provinces[province]:  # 遍历指定省份键的值，即遍历某个省份的所有城市
                print(city, end=" ")  # 输出城市
            print()  # 输出完毕后换行
        else:  # 如果传入的值不为字典内的任何键
            print("省份不存在")

    def seekCity(city):  # 定义函数用以查找城市
        for perProvince in provinces.keys():  # 遍历字典内所有省份键
            # 列表查询，如果传入的值可以在省份的值内找到，即传入的值能在某一城市列表找到
            if city in provinces[perProvince]:
                print(city+"属于"+perProvince+"省")  # 则输出那个城市以及在哪个省找到的
                return
        print("没有此城市")  # 如果遍历完后无输出结果，则城市不存在

    appendDict("广东", ["广州", "深圳"])  # 为字典添加省份与城市
    appendDict("四川", ["成都", "内江", "乐山"])
    appendDict("贵州", ["贵阳", "六盘水", "兴义"])
    output()  # 输出字典
    seekProvince("四川")  # 查找字典包含“四川”的省份键，并输出它的城市
    seekCity("六盘水")  # 查找名为“六盘水”的城市，以及它的省份


# p126_464()


def p128_472():  # 在此程序中，将会使用到二分法；二分法可适用于寻找按某种方法排序的一组可迭代数列中的一个数值
    # 建立一个包含字典的列表，即每个单词都有两个键值对，并以列表方式存储每个单词
    wordDict = [{"word": "about", "chinese": "在附近，关于"},
                {"word": "post", "chinese": "邮寄，投递"}]

    def show():  # 定义函数用以输出单词
        for word in wordDict:  # 遍历列表中的字典，word变量会被赋值一个键值对
            # 输出单词和中文，单词部分占位16个字符
            print("% -16s:% s" % (word["word"], word["chinese"]))

    def seekWord(word):  # 定义函数用以查找指定单词
        dictLeftIndex = 0  # 设置列表最左侧字典的索引
        dictRightIndex = len(wordDict) - 1  # 获取列表最右侧字典的索引
        while dictLeftIndex <= dictRightIndex:  # 当字典左侧索引小于等于字典右侧索引时，即当左侧范围索引位于右侧范围索引的左边或与右侧范围索引重合时，执行以下代码块
            # 定义字典中dictLeftIndex与dictRightIndex中间所处键值对的索引号，类似于给出一条线，求出它的中点
            middleIndex = (dictLeftIndex + dictRightIndex) // 2
            if wordDict[middleIndex]["word"] == word:  # 如果有某个位于中位索引的单词等于需要查找的单词
                print("% -16s : % s" %
                      (word, wordDict[middleIndex]["chinese"]))  # 输出那个单词和单词的中文
                return  # 退出while
            # 使用二分法对其进行查找，由于字典的单词按从小到大排序，即从a-z排序，因此如果需要查找的单词小于现在中位索引所在的单词
            elif wordDict[middleIndex]["word"] > word:
                # 则将右侧范围的索引使用中位索引减去1，即右侧范围从原来向左缩小了一半，类似于将一条线分为两半，选取左边半条，因此中位索引也向左移动了一定距离
                dictRightIndex = middleIndex - 1
            else:  # 在以上两种例外的情况，即如果中位索引所处的单词小于需要查询的单词时
                # 中位索引需要向右移动以查找，将左侧范围的索引使用中位索引加上1，类似于将一条线分为两半，选取右边半条，因此中位索引也向右移动了一定距离
                dictLeftIndex = middleIndex + 1
        print(word+"---没有此单词")  # 如果在查询完列表后仍无结果，输出指定语句

    def inputWord():  # 定义函数用以将输入的内容整形为字典
        wordNeedInsert = {}
        wordNeedInsert["word"] = input("单词：")
        wordNeedInsert["chinese"] = input("中文意义：")
        return wordNeedInsert

    def insertWord(wordNeedInsert):  # 定义函数用以插入单词
        dictLeftIndex = 0
        dictRightIndex = len(wordDict) - 1
        while dictLeftIndex <= dictRightIndex:
            middleIndex = (dictLeftIndex + dictRightIndex) // 2
            if wordDict[middleIndex]["word"] == wordNeedInsert["word"]:
                print(wordNeedInsert["word"]+"---已存在")
                return
            elif wordDict[middleIndex]["word"] > wordNeedInsert["word"]:
                dictRightIndex = middleIndex - 1
            else:
                dictLeftIndex = middleIndex + 1
        # 由于在最后左侧的范围总是会在右侧范围的右侧，因此左侧范围可用于测定这个单词应该按序放于何处
        wordDict.insert(dictLeftIndex, wordNeedInsert)
        print(wordNeedInsert["word"]+"---添加成功")

    def updateWord(wordNeedUpdate):  # 定义函数用以更改单词的翻译
        dictLeftIndex = 0
        dictRightIndex = len(wordDict) - 1
        while dictLeftIndex <= dictRightIndex:
            middleIndex = (dictLeftIndex + dictRightIndex) // 2
            if wordDict[middleIndex]["word"] == wordNeedUpdate["word"]:
                wordDict[middleIndex]["chinese"] = wordNeedUpdate["chinese"]
                print(wordNeedUpdate["word"]+"---更新成功")
                return
            elif wordDict[middleIndex]["word"] > wordNeedUpdate["word"]:
                dictRightIndex = middleIndex - 1
            else:
                dictLeftIndex = middleIndex + 1
        print(wordNeedUpdate["word"]+"---单词不存在")

    def deleteWord(wordNeedDelete):  # 定义函数用以删除单词
        dictLeftIndex = 0
        dictRightIndex = len(wordDict) - 1
        while dictLeftIndex <= dictRightIndex:
            middleIndex = (dictLeftIndex + dictRightIndex) // 2
            if wordDict[middleIndex]["word"] == wordNeedDelete:
                del wordDict[middleIndex]
                print(wordNeedDelete+"---已删除")
                return
            elif wordDict[middleIndex]["word"] > wordNeedDelete:
                dictRightIndex = middleIndex - 1
            else:
                dictLeftIndex = middleIndex + 1
        print(wordNeedDelete+"---单词不存在")

    while True:  # 主程序根据输入数值调用上方函数
        print("--------单词笔记簿--------")
        print("1.列出 2.查找 3.添加 4.更改 5.删除 6.退出")
        intInput = input("输入数字以指定操作：")
        if intInput == "1":
            show()
        elif intInput == "2":
            seekWord(input("请输入要查找的单词："))
        elif intInput == "3":
            # 指定单词经过inputWord()整形后传入insertWord()；选项4用以更改单词的函数同理
            insertWord(inputWord())
        elif intInput == "4":
            updateWord(inputWord())
        elif intInput == "5":
            deleteWord(input("要删除的单词："))  # 只删除字典中的键，值跟随键一起删除
        elif intInput == "6":
            break
        print()  # 输出空格，美化UI
    print("程序结束")


# p128_472()


def p132_exercise():

    def exercise1():
        print("直接修改字符串内的某个字符")
        string = "abc"
        # string[0] = "1"   # 由于字符串不可变，因此直接使用索引方法是不合规的
        # 以下方法为裁剪组合法，是合规的，且均为索引方式修改
        string = "abc"
        string = "1" + string[1:]  # 切片法
        print(string)

        string = "abc"
        lstring = list(string)  # 转列表后修改法
        lstring[0] = "1"
        string = "".join(lstring)
        print(string)

    exercise1()

    def exercise2():
        string = input("输入一串字符串，找出所有数字：")
        digit = ""
        for i in string:
            if i.isdigit():
                digit += str(i)
        print(digit)

    exercise2()

    def exercise3():

        def reverse(string):
            return string[::-1]

        print(reverse("abc"))

    exercise3()

    def exercise5():
        print("列表可以存放任何类型的元素")
        list = []
        list.append(1)
        list.append("list")
        list.append(float(7/3))
        list.append({"a": "1"})
        list.append((1, 2, 3))
        print(list)

    exercise5()

    def exercise6():
        print("列表可嵌套，因为列表存储任何类型的元素，也可输出某个嵌套的值")
        list = [[[1]], [2]]
        print(list[0][0][0], list[1][0])

    exercise6()

    def exercise7():
        date = {"year": "2023", "month": "5", "day": "27"}
        print(date["year"], date["month"], date["day"])

    exercise7()

    def exercise9():  # 理解以下内容需要一些数据库基础
        # 可以将变量d理解为数据库，student则是一张表，而student的值是一个列表，用以记录每个学生的每个属性，表内每一个字典包含了每一个学生的属性
        d = {"students": [{"name": "A", "sex": "M"},
                          {"name": "B", "sex": "c"}]}
        for k1 in d.keys():  # k1用以遍历数据库，可以查找到名为student的表
            for k2 in d[k1]:  # k2用以遍历表的所有内容，并一次获取一个学生的信息，包括学生属性与属性的值，即k2的内容为学生信息的字典
                for k3 in k2.keys():  # k3用以遍历学生的属性，即遍历每个学生字典的键，为"man"，"sex"
                    print(k3, k2[k3])  # 因此最后输出学生属性k3，即字典的键，以及k3所含的值，即字典的值

    exercise9()

    def exercise10():

        def interval(t1, t2):
            # 计算两个时间的秒数形式
            t1_second = t1["hour"] * 3600 + t1["minute"] * 60 + t1["second"]
            t2_second = t2["hour"] * 3600 + t2["minute"] * 60 + t2["second"]
            t_second = t1_second - t2_second
            dict = {"hour": 0, "minute": 0, "second": 0}  # 创建字典
            if t1_second < t2_second:
                t_second = t2_second - t1_second
            elif t1_second == t2_second:
                return dict  # 返回空值的字典
            hour = t_second // 3600
            minute = t_second // 60 % 60
            second = t_second % 60 % 60
            dict = {"hour": hour, "minute": minute, "second": second}
            return dict  # 返回计算完毕的字典

        t1 = {"hour": 12, "minute": 23, "second": 34}
        t2 = {"hour": 11, "minute": 45, "second": 14}
        print(interval(t1, t2))

    exercise10()


# p132_exercise()


def p136_513():

    class person:  # 定义一个名为person的类，即将person视为一个拥有属性及其值的对象
        name = "james"  # 定义了属性name，其值为"james"
        age = 12  # 定义了属性age，其值为12

    p = person()  # 可将一个类链接进一个变量当中,此时变量p为类person的一个实例对象
    print(person.name, person.age)  # 需要访问时，使用“类名.属性名”来访问，此时只是访问一个类内的变量
    print(p.name, p.age)  # 由于变量p为类person的一个实例，因此也可以对其访问


# p136_513()


def p137_514():

    class person:
        name = "james"
        age = 12

    # 变量p1为类person的一个实例对象，也就是说，p1为person的一个只读链接副本，因此，对p1的改动不会影响到person，而对person的改动则会影响到p1
    p1 = person()  # 注意：当且仅当类后为括号时，变量p1才会成为类person的实例对象
    p2 = person  # 否则对于使用"="符连接类person，类person直接赋值进变量p2，因此如果变量p2一旦被改动，类person也相当于被改动了
    print(person.name, person.age)
    print(p1.name, p1.age)
    print(p2.name, p2.age)
    person.name = "robert"  # 更改类person中属性name的值
    p1.age = 15  # 更改实例p1中属性age的值
    p2.age = 20  # 更改变量p2中属性age的值，即相当于更改类person中属性为age的值
    print(person.name, person.age)
    print(p1.name, p1.age)
    print(p2.name, p2.age)
    # 输出内存地址，可看出变量p2与类person的值一致，而实例p1却不同于其他两个值
    print(id(p1), id(p2), id(person))


# p137_514()


def p139_515_U():

    class person():  # 创建一个具有私有属性的类
        __name = "james"  # 在属性前方添加2个下划线"_"，即将属性name设为私有属性
        __age = 12  # 将属性age设为私有属性

        def show():  # 在类的内部定义函数，而在类的外部则称之为类的方法，如果此时将函数名左侧也添加下划线，那么show()函数将变为私有函数，无法在类外调用
            # 当且仅当定义函数位于类的内部时，才具有对私有类属性的访问权限，并且访问时的属性名也要添加下划线
            print(person.__name, person.__age)

    # print(person.__name, person.__age)  # 当在类的外部访问类的私有属性时，会抛出没有此属性的错误
    person.show()  # 对类person使用show()方法，即通过person内的show()函数来访问person内的属性


# p139_515_U()


def p139_515_D():

    class person:  # 对于类的创建，如果不需要将某个变量传入，实际上可以不需要括号，能够增加代码可读性
        name = "XXX"
        gender = "X"
        age = 0

    # 类的实例，可以理解为一个基于类为状态的对象，与类相关，并且类与实例为单向连接，类->实例；因此实例内的某个属性一旦被其他函数改变，而不是被类改变，则类内的属性与实例的连接将断开
    aPerson = person()
    print(aPerson.name, aPerson.gender, aPerson.age)
    print(person.name, person.gender, person.age)
    aPerson.name = "A"
    aPerson.gender = "男"
    aPerson.age = 20
    person.name = "B"
    person.gender = "女"
    person.age = 21
    print(aPerson.name, aPerson.gender, aPerson.age)
    print(person.name, person.gender, person.age)


# p139_515_D()


def p141_521():

    class person:
        __name = "james"  # 创建私有类属性
        __age = 12

        # 在类内创建函数，即，类外的方法
        def getName(self):  # 变量self传入函数，即，将实例对象自身传入至函数中，而不是类的自身，在创建函数时，self必须是函数的第一个参数；当然，self只是约定俗成，可以替换为其他任何有效变量名
            return self.__name  # 函数获取私有属性的值后返回至调用，但此私有属性的值是属于实例对象的，而不是类的

        def getAge(self):  # 函数getAge()得到实例自身
            return self.__age  # 返回实例自身的私有属性的值

    p = person()
    print(p.getName(), p.getAge())  # 实例在执行方法时会将自己的属性传递给类内函数中的self


# p141_521()


def p142_522():  # python中有三种方法：类方法、静态方法、实例方法，这些方法在函数上方有"@"用以修饰函数
    class person:
        __name = "james"
        __age = 12

        # classmethod用以修饰(声明)某个函数是给类用的
        @ classmethod
        # 由于在没有修饰的情况下，也就是一般的实例方法下，类不能传入至实例方法，因此必须声明此函数为类方法后才能传入
        def showClass(cls):  # 函数的第一个参数作为传入类属性的变量，约定俗成地，这个参数的变量名为cls
            print(cls.__name, cls.__age)

    person.showClass()


# p142_522()


def p142_523():

    class person:
        __name = "james"
        __age = 12

        # 以下修饰过的方法可以且仅有这些方法能访问类内属性
        # 静态方法不会将任何类或实例相关的参数自我传入至函数内，但可以定义函数的传入参数后手动将类或实例传入至函数内
        @ staticmethod
        def showStatic():
            print(person.__name, person.__age)

        # 类方法是给类用的方法，一般的方法为实例方法，由于类无法使用实例方法，因此使用类方法来访问传入的类的属性
        @ classmethod
        def showClass(cls):
            print(cls.__name, cls.__age)

    person.showStatic()
    person.showClass()


# p142_523()


def p143_523():

    # 需要注意的是，python三种类型的方法都可以给实例使用
    class person:
        name = "XXX"
        gender = "X"
        age = 0

        def showInstance(self):
            print(self.name, self.gender, self.age)

        @ classmethod
        def showClass(cls):
            print(cls.name, cls.gender, cls.age)

        @ staticmethod
        def showStatic():
            # 在内部实现静态方法对于类的调用，实例并没有被传入
            print(person.name, person.gender, person.age)

    p = person()
    p.showInstance()
    p.showClass()
    p.showStatic()


# p143_523()


def p145_531():

    class person:

        # python自带的初始化函数init，即initialize，会在实例对象创建时自动调用，因此初始化函数的第一个参数必须是实例对象，而且如果初始化函数指定了位置参数，那么在创建实例时，必须传入参数
        def __init__(self, n):
            print("__init__", self, n)
            self.name = n  # 在初始化过程中，在实例对象内创建一个属性name，然后将变量n的值赋值至name属性

        # python自带的函数del，在程序结束时自动调用，用以销毁某个实例对象，一般是销毁实例对象自身，可以用以释放资源
        def __del__(self):
            print("__del__", self)

        def show(self):
            print("show", self, self.name)

    p = person("james")
    p.show()  # 对实例对象使用show()方法
    print(p)  # 输出实例对象p，可看出在创建实例对象时会输出三行，第一行是初始化，第二行是实例自身，第三行是销毁


# p145_531()


def p147_532():

    class person:

        def __init__(self, name, gender, age):  # 在类person内定义初始化，可接收的变量为实例自身，以及需要传入的三个变量
            # 由于类的内容为空，因此需要在实例对象内创建各属性，并将接收到的值传入这些属性
            self.name = name
            self.gender = gender
            self.age = age

        def show(self):  # 定义函数用以输出实例对象的属性值
            print(self.name, self.gender, self.age)

    p = person("james", "male", 12)  # 在执行创建实例对象的行为时，括号内的三个值被传入至初始化函数
    p.show()  # 对实例对象使用show()方法，输出的值均为实例对象内后来添加的值


# p147_532()


def p148_533():

    class person:

        def __init__(self, name="", gender="male", age=0):  # 为初始化函数创建默认参数
            self.name = name
            self.gender = gender
            self.age = age

        def show(self):
            print(self.name, self.gender, self.age)

    a = person("james")  # 定义了默认参数的方法可以不需要填写全部参数
    b = person("james", "female")
    c = person("james", "male", 20)
    a.show()
    b.show()
    c.show()


# p148_533()


def p148_534():

    class person:

        def __init__(self, name="", gender="male", age=0):
            self.name = name
            self.gender = gender
            self.age = age

        def show(self):
            print(self)
            print(self.name, self.gender, self.age)

    p = person("james", 'male', 20)
    # 之前提到了类不能使用实例方法，原因是无法将自身传入函数，因此类实际上是可以使用实例方法的，手动指定某个实例对象传入至方法即可
    person.show(p)
    p.show()  # 当然，通过person手动传入方法与实例对象自动传入方法并无任何差别；一般地，选择后者


# p148_534()


def p149_535():

    class dateClass:  # 定义类用以检测传入日期的合规性
        __months = [0, 31, 28, 31, 30, 31, 30, 31, 31,
                    30, 31, 30, 31]  # 在类内部创建一个列表，用以存储每月的天数

        def __init__(self, year, month, day):  # 定义初始化函数用以执行以下检测代码块
            if year < 0:
                raise Exception("错误的年份")
            if month < 1 or month > 12:
                raise Exception("错误的月份")
            if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:  # 计算闰年，如果为闰年，2月为29，否则28
                dateClass.__months[2] = 29
            else:
                dateClass.__months[2] = 28
            # 只有在计算完闰年后才能对日期进行检测，否则2月会出现错误
            if day < 1 or day > dateClass.__months[month]:
                raise Exception("错误的日期")
            self.year, self.month, self.day = year, month, day

        def showDate(self, end="\n"):  # 定义默认参数end，用以传入print()内，即换行
            print("%04d-%02d-%02d" % (self.year, self.month, self.day),
                  end=end)  # 将输出格式化，左侧为空的向左填0，并将函数的end传入至print()的end

    try:  # 为主程序加入错误捕捉
        date = dateClass(2017, 7, 8)
        date.showDate()
    except Exception as err:
        print(err)


# p149_535()


def p151_541():  # 父类必须在子类上方
    # 定义一个类person，派生出student，也就是说，person是父类，因此student是person的子类
    class person:  # 定义类person，用以处理基本信息

        def __init__(self, name, gender, age):  # 初始化函数定义了将传入参数赋值进实例的属性
            self.name = name
            self.gender = gender
            self.age = age

        def showData(self, end="\n"):  # 定义函数用以接受实例对象，并输出实例前半部分的属性与值
            print(self.name, self.gender, self.age, end=end)

    # 创建一个子类，内容包含父类的属性，而自身也可能包含其他的的属性，这样说，子类student是父类person的继承，创建子类的方法"class 子类名(父类名)"
    class student(person):  # 定义子类student，用以处理额外信息

        # 定义子类的初始化函数，这样在创建类student的实例时可传入全部内容
        def __init__(self, name, gender, age, major, depart):
            # 对于子类，无法使用隐藏式调用将参数自动传入init，而是手动调用init并将参数传入；将基本信息传入类person的初始化进行处理后，self，也就是实例student已经拥有了基本信息的属性值
            person.__init__(self, name, gender, age)
            self.major = major  # 将额外的属性及其值传入至实例student的内部
            self.depart = depart

        def showData(self):  # 定义子类student的输出函数
            # 前半部分基本信息由父类person进行输出，将实例student交给person类的showData()函数,并以空格结尾
            person.showData(self, " ")
            print(self.major, self.depart)  # 后半部分信息由子类student定义输出，

    # 在执行此行代码时，由于是子类内部调用了父类的函数，因此只有1个实例在类间互相调用
    stu = student("james", "male", 20, "software", "computer")
    stu.showData()


# p151_541()


def p152_542():

    class person:

        def __init__(self, name, gender, age):
            self.name = name
            self.gender = gender
            self.age = age

        def showData(self, end="\n"):  # 定义一个与子类某函数重名的函数名
            print(self.name, self.gender, self.age, end=end)

        def showData1(self, end="\n"):  # 定义一个与上方函数相同但函数名不同的函数
            print(self.name, self.gender, self.age, end=end)

    class student(person):

        def __init__(self, name, gender, age, major, depart):
            person.__init__(self, name, gender, age)
            self.major = major
            self.depart = depart

        def showData(self):  # 定义一个与父类重名的函数名
            person.showData(self, " ")
            print(self.major, self.depart)

        def changeName(self, name):
            self.name = name

    stu = student("james", "male", 20, "software", "computer")
    stu.showData()  # 如果子类有一个函数与父类同名，则称类student重写了类person的showData()，即，用类student的showData()函数覆盖了原本类person的函数，因此此外部调用方法的代码块是属于类student的
    stu.showData1()
    stu.changeName("robert")  # 方法changeName用以更改实例属性name的值
    stu.showData()
    stu.showData1()


# p152_542()


def p153_543():

    class dateClass:
        __months = [0, 31, 28, 31, 30, 31, 30, 31, 31,
                    30, 31, 30, 31]

        def __init__(self, year, month, day):
            if year < 0:
                raise Exception("错误的年份")
            if month < 1 or month > 12:
                raise Exception("错误的月份")
            if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
                dateClass.__months[2] = 29
            else:
                dateClass.__months[2] = 28
            if day < 1 or day > dateClass.__months[month]:
                raise Exception("错误的日期")
            self.year, self.month, self.day = year, month, day

        def showDate(self, end="\n"):
            print("%04d-%02d-%02d" %
                  (self.year, self.month, self.day), end=end)

    class dayClass(dateClass):  # 定义时分秒类为日期类的子类

        # 将日期交给日期类判断并添加实例属性后，自己判断时分秒合规性，并添加至实例的属性
        def __init__(self, year, month, day, hour, minute, second):
            dateClass.__init__(self, year, month, day)
            if hour < 0 or hour > 23 or minute < 0 or minute > 59 or second < 0 or second > 59:
                raise Exception("错误的时分秒")
            self.hour = hour
            self.minute = minute
            self.second = second

        # 先将实例交给日期类显示日期，然后交给自己的代码显示时分秒
        def showDate(self, end="\n"):
            dateClass.showDate(self, " ")
            print("%02d:%02d:%02d" %
                  (self.hour, self.minute, self.second), end=end)

    try:  # 为主程序加入错误捕捉
        date = dayClass(2017, 7, 8, 23, 12, 34)
        date.showDate()
    except Exception as err:
        print(err)


# p153_543()


def p156_552():  # 此代码已经过重写

    class student:  # 类student定义了如何对列表进行输入或输出

        def __init__(self, Num, Name, Gender, Age):  # 为实例创建属性
            self.Num = Num
            self.Name = Name
            self.Gender = Gender
            self.Age = Age

        def show(self):
            print("%-16s %-16s %-8s %-4d" %
                  (self.Num, self.Name, self.Gender, self.Age))  # 按一定格式输出属性的数据

    class operateStudentList:  # 类operateStudentList定义了一系列对学生列表的操作

        def __init__(self):  # 在创建实例时为实例创建一个列表用以存储学生数据
            self.students = []

        def __studentSeek(self, Num):  # 定义一个私有函数用以查找某个编号，仅允许类内函数调用，该函数使用二分法，并以编号Num进行排序
            start = 0
            end = len(self.students)-1
            while start <= end:
                middle = (start + end) // 2
                if self.students[middle].Num == Num:
                    return True, middle  # 如果查询有结果，返回True与查找到的位置
                elif self.students[middle].Num > Num:
                    end = middle - 1
                else:
                    start = middle + 1
            return False, start  # 如果无结果，则返回小于传入编号Num最近的编号右侧的位置

        def __insert(self, studentNeedAdd):  # 定义私有函数，作为添加某个学生的核心部分
            judgement, number = self.__studentSeek(
                studentNeedAdd.Num)  # 将某个编号放入查找函数，并得出是否存在的布尔值和具体的位置值
            if judgement:  # 如果是True，则查找成功，即已存在
                print(f"编号{studentNeedAdd.Num}已存在")
            else:  # 否则不存在
                # 对列表使用insert()方法将学生数据插入到得到的位置
                self.students.insert(number, studentNeedAdd)
                print("添加成功")

        def __update(self, studentNeedUpdate):
            judgement, number = self.__studentSeek(studentNeedUpdate.Num)
            if judgement:  # 如果存在，对列表做更改
                self.students[number].Name = studentNeedUpdate.Name
                self.students[number].Gender = studentNeedUpdate.Gender
                self.students[number].Age = studentNeedUpdate.Age
                print("更改成功")
            else:  # 否则不存在
                print("没有此学生")

        def __delete(self, Num):
            judgement, number = self.__studentSeek(Num)
            if judgement:  # 存在，则删除某位置的数据
                del self.students[number]
                print("删除成功")
            else:  # 否则不存在
                print("没有此学生")

        def __infoCheck(self):  # 定义私有函数作为信息输入的接口，以及用以检测学生信息的合规性
            Num = input("学生编号：")
            Name = input("学生姓名：")
            Gender = input("学生性别：")
            Age = input("学生年龄：")
            judgement = False  # 创建判断变量
            if Gender == "男" or Gender == "女":
                judgement = True  # 如果输入合规，判断变量变为True
            else:
                print("无效的性别")
                judgement = False  # 否则为False
            if Age.isdigit():  # 如果年龄有效，则整形为int
                Age = int(Age)
            else:  # 否则年龄为0
                Age = 0
            if Num.isdigit() == False or Name == "":
                print("学号与姓名错误")
                judgement = False  # 如果学号与姓名为空，判断变量也为False
            return judgement, Num, Name, Gender, Age

        def show(self):  # 定义输出列表的主函数
            print("%-16s %-16s %-8s %-4s" % ("No.", "Name", "Gender", "Age"))
            for i in self.students:
                i.show()

        def delete(self):  # 定义公开函数，可被外部作为方法调用
            Num = input("请输入需要删除的号数：")
            if Num != "":
                self.__delete(Num)

        def insert(self):
            judgement, Num, Name, Gender, Age = self.__infoCheck()
            if judgement:
                self.__insert(student(Num, Name, Gender, Age))

        def update(self):
            judgement, Num, Name, Gender, Age = self.__infoCheck()
            if judgement:
                self.__update(student(Num, Name, Gender, Age))

        def process(self):
            while True:
                print("1.列出 2.插入 3.更改 4.删除 5.退出")
                string = input("请输入要执行的选项>")
                list = [0, False, False, False, False,
                        False, False]  # 采用检测列表改变方法，类似于开关
                if string.isdigit() and int(string) < 6:
                    list[int(string)] = True
                if list[1]:
                    self.show()
                if list[2]:
                    self.insert()
                if list[3]:
                    self.update()
                if list[4]:
                    self.delete()
                if list[5]:
                    break

    start = operateStudentList()
    start.process()


# p156_552()


def p160_exercise():

    def exercise1():

        class complex:

            def __init__(self, a=0, b=0):
                self.a = a
                self.b = b

            def showComplex(self, a=float(0), b=int(0)):
                self.__init__(a, b)
                print(f"({self.a}+{self.b}j)")

        com = complex()
        com.showComplex(1, 2)

    exercise1()

    def exercise2():

        class myComputer:

            def __init__(self, Cpu=str, RAM=int, DiskVol=int):
                self.Cpu = Cpu
                self.RAM = RAM
                self.DiskVol = DiskVol

            def show(self):
                print(f"CPU是{self.Cpu},内存大小是{self.RAM}G,硬盘大小是{self.DiskVol}G")

        mc = myComputer("8核32线程", 8, 500)
        mc.show()

    exercise2()

    def exercise3():

        class myIntager:

            def __init__(self, value):
                self.value = value

            def toBin(self):
                print(bin(self.value))

            def toHex(self):
                print(hex(self.value))

        mi = myIntager(2)
        mi.toBin()
        mi.toHex()

    exercise3()

    def exercise4():

        class person:

            def __init__(self, name, sex, age):
                self.__m_name = name
                self.__m_sex = sex
                self.__m_age = age

            def show(self):
                print(self.__m_name, self.__m_sex, self.__m_age, end=" ")

        class student(person):

            def __init__(self, name=str, sex=str, age=int, m_class=int, m_major=str):
                # super()，即超类，或父类；使用super()可直接指定父类，而无需输入父类名，甚至无需手动传入实例
                super().__init__(name, sex, age)
                self.m_class = m_class
                self.m_major = m_major

            def sClass(self):
                print(self.m_class)

            def sMajor(self):
                print(self.m_major)

            def show(self):
                super().show()
                print(self.m_class, self.m_major)

        stu = student("张三", "男", "18", "高三", "理科")
        stu.show()

    exercise4()

    def exercise5():

        class time:

            def __init__(self, hour, minute, second):
                self.hour = hour
                self.minute = minute
                self.second = second

            def show(self):
                print("%02d:%02d:%02d" % (self.hour, self.minute, self.second))

            def compare(self, otherTime):
                time_1 = self.hour * 3600 + self.minute * 60 + self.second
                time_2 = otherTime.hour * 3600 + otherTime.minute * 60 + otherTime.second
                if time_1 < time_2:
                    print("%02d:%02d:%02d" %
                          (otherTime.hour, otherTime.minute, otherTime.second)+"大")
                else:
                    print("%02d:%02d:%02d" %
                          (self.hour, self.minute, self.second)+"大")

        time_1 = time(10, 5, 15)
        time_2 = time(22, 2, 56)
        time_1.show()
        time_1.compare(time_2)

    exercise5()


# p160_exercise()


def p163_613():
    # 使用open()函数可对一个文件进行打开操作，在open()函数中必需定义文件路径
    # 在模式中r为读read，对已存在的文件有效；w为写write，无论文件是否存在均有效；a为追加add，无论文件是否存在均有效；x为独占创建exclusive，对已存在的文件无效
    # t即text，以文本文件操作，以字符为单位；b即binary，以二进制文件进行操作，以字节为单位；+即update，对文件进行读写(更新)的操作
    # 由于open()函数对于模式的默认值有t，因此rwax等同于rt,wt,at,xt，得到有rt,wt,at,xt,rb,wb,ab,xb,r+,w+,a+,x+，即以文本方式读写添创，以二进制方式读写添创，更新文件的读写添创
    try:
        # 对于不存在的文件Foo.txt，读模式下会返回错误，错误类型为IO(输入输出)异常
        file = open("./Foo.txt", "rt")
        read = file.read()
        file.close()
    except:
        print("打开失败")


# p163_613()


def p164_611():
    try:  # 由于在读写文件时遇到错误的可能性较大，因此最好使用try...except...语句
        # open()函数需要配合close()方法使用，只有打开文件后才能对文件内部进行操作，对于文件路径，有绝对路径与相对路径的写法
        file = open("C:/61.txt", "wt")  # 以写文本模式，在C盘根目录下创建文件611.txt
        file.write("Hello World!")  # 向文本内写内容
        file.close()  # 对文件使用close()方法，目的是节约内存空间
    except Exception as err:
        print(err)


# p164_611()


def p164_612():
    try:
        file = open("C:/61.txt", "at")  # 对上面创建的文件使用文本追加模式
        file.write("\n添加模式")  # 写入换行符号与字符串
        file.close()  # 关闭文件
    except Exception as err:
        print(err)


# p164_612()


def p165_615():

    def inputStudent(tick):  # 定义函数用以接收学生信息
        print(f"现在是第{tick}个学生")
        try:
            name = input("姓名：")
            if name.strip() == "":
                raise Exception("姓名无效")
            gender = input("性别：")
            if gender != "男" and gender != "女":
                raise Exception("性别无效")
            age = float(input("年龄："))
            if age < 18 or age > 30:
                raise Exception("无效的年龄")
            studentDict = {}  # 创建字典
            studentDict["Name"] = name  # 将学生信息以字典方式填入
            studentDict["Gender"] = gender
            studentDict["Age"] = age
            return studentDict  # 传出完成的字典
        except Exception as err:
            print(err)
            return None  # 如果出现错误，返回空值

    tick = 1  # 初始化计数器
    try:
        # 在open()函数中使用相对路径，即，文件将会创建在此Python文件所处的目录内
        file = open("students.txt", "wt")  # 以写文本方式打开这个文件
        while True:
            content = inputStudent(tick)
            if content:  # 判断inputStudent()函数传出的值是否有效，如果是None则数据非真，如果返回字典则为真，执行写入文件
                # 从变量content得到字典的值，并写入文件，每输出一个值换行
                file.write(
                    f'{content["Name"]}\n{content["Gender"]}\n{str(content["Age"])}\n')
                tick += 1  # 计数器加1
            continuely = input("是否继续输入[Y/N]")  # 将数值传入
            if continuely != "Y" and continuely != "y":  # 为防止大小写未改变，因此如果变量continuely不为Y和y
                break  # 退出循环
        file.close()  # 关闭文件
    except Exception as err:
        print(err)


# p165_615()


def p167_621():

    def writeFile():  # 定义函数用以读取文件
        file = open("Foo.txt", "wt")  # 以写文本方式打开文件
        file.write("你好\n世界！")  # 写入字符串
        file.close()  # 关闭文件

    def readFile():
        # 位于python项目文件同一目录下的文件，可直接指定文件名用以打开
        file = open("Foo.txt", "rt")  # 以读文本方式打开文件
        read = file.read()  # 将读到的内容赋值变量read
        print(read)
        file.close()  # 关闭文件

    try:
        writeFile()
        readFile()
    except Exception as err:
        print(err)


# p167_621()


def p168_622():

    def writeFile():  # 定义函数用以读取文件
        file = open("Bar.txt", "wt")  # 以写文本方式打开文件
        file.write("你好\n世界！")  # 写入字符串
        file.close()  # 关闭文件

    def readFile(size):
        file = open("Bar.txt", "rt")  # 以读文本方式打开文件
        # read()方法可以填入需要获取的字符数量，例如4，在文本"abcde"中可得到结果"abcd"
        read = file.read(size)
        print(read)
        file.close()  # 关闭文件

    try:
        writeFile()
        n = 3
        readFile(n)  # 传入想要读取的字符量；注意，在文本文件中，换行符也将被视为一个字符，因此输出的结果会包含一个换行符
    except Exception as err:
        print(err)


# p168_622()


def p169_623():

    def writeFile():
        file = open("Foo.txt", "wt")  # 以写文本方式打开文件
        file.write("你好\n世界！")
        file.close()

    def readFile():  # 定义函数用以读文件的全部内容
        file = open("Foo.txt", "rt")  # 以读文本方式打开文件
        judgement = True  # 创建判断变量
        string = ""  # 创建字符串变量
        while judgement:
            # 在使用open()对文件进行操作的情况下，存在文件指针系统，类似于在一个文本文件内的光标，当读一个字符时，光标就向右移动一个字符
            read = file.read(1)
            if read != "":  # 当有内容被读到时，将读到的内容添加进字符串变量；在文件指针的移动下，指针最终会到达文件的结尾，由于到结尾后不会再拥有字符，因此返回空内容
                string += read
            else:  # 如果是空内容，则将判断变量转为False，即，结束循环
                judgement = False
        file.close()
        print(string)  # 输出得到的字符串结果

    try:
        writeFile()
        readFile()  # 实际上函数readFile()函数与read()方法实现的功能相同
    except Exception as err:
        print(err)


# p169_623()


def p170_624():

    def writeFile():
        file = open("Bar.txt", "wt")
        file.write("你好\n世界！")
        file.close()

    def readFile():
        file = open("Bar.txt", "rt")
        # readline()方法将文件内的每行进行分割；一般地，文本编辑器为了方便考虑，而将一行文本格式化为多行，因此只有手动换行，即回车，也就是输入换行符进行分隔，才会被视为换行符，换行符在python内为"\n"符
        read = file.readline()  # 因此文件游标的工作方式为从某行首到下一行首之间的字符串
        print(read, "length=", len(read))  # 换行符也将算作一个字符，并且在截取时，换行符也会被一并输出
        read = file.readline()
        print(read, "length=", len(read))
        read = file.readline()  # 游标已到结尾的情况下继续读取，将得到空内容
        print(read, "length=", len(read))
        file.close()

    try:
        writeFile()
        readFile()
    except Exception as err:
        print(err)


# p170_624()


def p171_625():

    def writeFile():
        file = open("Foo.txt", "wt")
        file.write("你好\n世界！")
        file.close()

    def readFile():
        file = open("Foo.txt", "rt")
        judgement = True
        string = ""
        while judgement:
            read = file.readline()  # 与read()方法类似，每次将光标向下一行首移动
            if read != "":
                string += read
            else:
                judgement = False
        file.close()
        print(string)

    try:
        writeFile()
        readFile()
    except Exception as err:
        print(err)


# p171_625()


def p172_626():

    def writeFile():
        file = open("Bar.txt", "wt")
        file.write("你好\n世界！\nHello, world!")
        file.close()

    def readFile():
        file = open("Bar.txt", "rt")
        readLines = file.readlines()  # 使用readlines()方法读取的结果会转为一个列表，将每行的内容存于一个列表之中
        print(readLines)
        for eachLine in readLines:  # 遍历生成的列表，列表内的换行符"\n"会转为文本型换行符
            print(eachLine, end="")  # 验证产生的换行并非为print()函数产生
        file.close()

    try:
        writeFile()
        readFile()
    except Exception as err:
        print(err)


# p172_626()


def p173_623():

    class student:

        def __init__(self, name, gender, age):
            self.name = name
            self.gender = gender
            self.age = age

        def show(self):
            print(self.name, self.gender, self.age)

    studentList = []  # 新建一个学生列表用以存储读到的学生
    try:
        p165_615()  # 在p165_615中，创建的学生文件为姓名、性别、年龄各占一行
        file = open("students.txt", "rt")
        while True:
            # 从游标开始读取，即读取存有名字的行，由于在p173_623中的每个信息是换行写入，因此将每行的换行符移除
            name = file.readline().strip("\n")
            if name == "":  # 如果姓名为空，即一旦到达文本末尾，或是姓名为空，则退出
                break
            gender = file.readline().strip("\n")  # 姓名向下一行，即性别行
            age = float(file.readline().strip("\n"))  # 性别向下一行，即年龄行
            studentList.append(student(name, gender, age))  # 将得到的数据加入学生列表
        file.close()  # 如果全部读取完毕，即退出while循环，则关闭文件
        for each in studentList:  # 定义递归输出学生列表
            each.show()
    except Exception as err:
        print(err)


# p173_623()


def p175_632():
    # 向文本执行指定的操作时，可以使用默认参数encoding更改文本编码格式
    file = open("Foo.txt", "wt", encoding="utf-8")
    file.write("你好，world!")
    file.close()


# p175_632()


def p175_633():

    def writeFile():
        file = open("Bar.txt", "wt", encoding="utf-8")  # 在写入文件时使用utf-8进行编码
        file.write("你好，world!")
        file.close()

    def readFileGBK():
        file = open("Bar.txt", "rt")  # 在读取文件时使用默认参数encoding的值，即GBK进行解码
        rows = file.readlines()
        for row in rows:
            print(row)

    def readFileUTF8():
        file = open("Bar.txt", "rt", encoding="utf-8")  # 在读取文件时使用utf-8进行解码
        rows = file.readlines()
        for row in rows:
            print(row)

    try:
        writeFile()
        readFileGBK()  # 使用GBK解码读utf-8文件时，英文字符以外的字符不能被正常读取
        readFileUTF8()  # 使用utf-8读取utf-8则可全部正常读出
    except Exception as err:
        print(err)


# p175_633()


def p178_641():  # 在open()函数下，有指针系统，而对于指针的位置，有tell()和seek()方法用以对指针操作，tell()方法用以查询指针目前所在位置，seek()方法用以更改指针位置，指针的单位为字节
    file = open("Foo.txt", "wt")  # 打开一个空文件
    print(file.tell())  # 由于文件尚空，因此tell()返回的是目前指针所在位置
    file.write("hello")  # 将5个英文字符写入
    print(file.tell())  # 由于对文件进行了操作，因此指针也会跟随指定操作而改变位置，此时指针位置为5
    file.write("世界")  # 写入两个中文字符
    print(file.tell())  # 由于每个中文字符占2个字节，因此指针向后移动了4位
    file.close()


# p178_641()


def p179_642():

    def writeFile():
        file = open("Foo.txt", "wt+")  # 以wt的特性打开文件，但是包含读写权限
        print(file.tell())  # 输出打开文件后的游标，为0
        file.write("123")  # 写入字节量为3
        print(file.tell())  # 游标位于第三个字节
        # seek()方法可以改变游标的位置，用例seek(offset,whence)，其中whence代表从何处开始，0为文件开头，1为当前游标所处位置，2为文件末尾，默认为0；而offset则为偏移值，基于whence的偏移值，正负均可
        file.seek(2, 0)  # seek(2,0)为从文件开头开始，向右偏移2字节
        print(file.tell())  # 改变后查看游标，游标变为2
        file.write("abc")  # 在第二个字节后写入abc，即，将3进行替换，变为12abc
        print(file.tell())  # 查看游标，为5，即代表abc已写入至文件内
        file.close()
    # 在以上情况下，如果将打开方式改为at+，则字符3不会被替换，游标会自动移到无字符的位置进行写入

    def readFile():
        file = open("Foo.txt", "rt+")  # 以rt的特性打开文件，但是包含读写权限
        read = file.read()
        print(read)
        file.close()

    try:
        writeFile()
        readFile()
    except Exception as err:
        print(err)


# p179_642()


def p180_644():

    def writeFile():
        file = open("Bar.txt", "wt+")
        print(file.tell())
        file.write("123")
        print(file.tell())
        file.seek(2, 0)  # 调整游标位置
        print(file.tell())
        file.write("abc")  # 此时Bar.txt的内容为12abc
        print(file.tell())
        file.close()

    def readFile():
        # 对于模式rt+，由于继承了r的特性，因此即使可写入，也必须是在文件存在的情况下写入
        file = open("Bar.txt", "rt+")  # 在非追加模式下，游标通常位于文本首部
        file.write("我们")  # 对于中文字符，两个字符则意味着4个字节，因此"12abc"被替换为"我们c"
        file.seek(0, 0)  # 由于read()方法仅读取游标后的内容，因此如果想要读取全文，必须先将游标放置到开头
        read = file.read()
        print(read)
        file.close()

    try:
        writeFile()
        readFile()
    except Exception as err:
        print(err)


# p180_644()


def p183_651():
    # 对于二进制文件，其定义是一个与编码方式无关的字节内容文件；因此在open()方法下，默认参数encoding=在二进制模式中不可用

    def writeFile():
        file = open("Foo.txt", "wt")  # 以GBK编码方式写入文件
        file.write("你好，world!")
        file.close()

    def readFile():
        # 在二进制模式下，读取结果不会被解码为自然语言符号，而是机器码等人类不可读内容，此时，Foo.txt可被视为一个二进制文件
        file = open("Foo.txt", "rb")
        binaryRead = file.read()
        for i in range(len(binaryRead)):  # 获取该二进制文件的长度，即12个字节
            print(hex(binaryRead[i]), end=" ")  # 将二进制内容转码为16进制后输出
        file.close()

    try:
        writeFile()
        readFile()
    except Exception as err:
        print(err)


# p183_651()


def p184_654_1():

    def writeFileBinary():
        file = open("Foo.txt", "wb")
        # 对于字符串，有方法encode()将字符串编码为指定的机器码，再将其以二进制流方式输入至文件内,当且仅当写入流为机器码时，写二进制才有效
        file.write("你好，world!".encode("gbk"))
        file.close()

    def writeFileText():
        file = open("Bar.txt", "wt")  # 对于wt模式，文本会自动转为机器码，然后以二进制流写入至文件
        file.write("你好，world!")
        file.close()

    def readFile(fileName):
        file = open(fileName, "rb")  # 将文件以二进制文件流方式读取
        readBinary = file.read()
        for i in range(len(readBinary)):
            print(hex(readBinary[i]), end=" ")  # 将二进制文件内容转码为16进制
        print()
        file.close()

    try:
        writeFileBinary()
        writeFileText()
        readFile("Foo.txt")
        readFile("Bar.txt")
    except Exception as err:
        print(err)


# p184_654_1()


def p185_654_2():

    def writeFileBinary():
        file = open("Foo.txt", "wb")
        file.write("你好，world!".encode("utf-8"))  # 对于utf-8格式，二进制编码也是可用的
        file.close()

    def writeFileText():
        file = open("Bar.txt", "wt", encoding="utf8")
        file.write("你好，world!")
        file.close()

    def readFile(fileName):
        file = open(fileName, "rb")
        readBinary = file.read()
        for i in range(len(readBinary)):
            print(hex(readBinary[i]), end=" ")
        print()
        file.close()

    try:
        writeFileBinary()
        writeFileText()
        readFile("Foo.txt")
        readFile("Bar.txt")
    except Exception as err:
        print(err)


# p185_654_2()


def p186_662():

    class book:  # 定义类book用以格式化输入内容

        def __init__(self, ISBN, title, author, publisher):
            self.ISBN = ISBN
            self.title = title
            self.author = author
            self.publisher = publisher

        def show(self):  # 定义函数用以按格式列出表内内容
            print("%-16s%-16s%-16s%-16s" %
                  (self.ISBN, self.title, self.author, self.publisher))

    class bookList:  # 定义类bookList用以对数据进行操作

        def __init__(self):  # 初始化书的列表
            self.bookList = []

        def show(self):  # 重写函数，用以输出表内属性
            print("%-16s%-16s%-16s%-16s" %
                  ("ISBN", "Title", "Author", "Publisher"))
            for book in self.bookList:
                book.show()  # 调用类book的方法用以输出每行记录

        def __insert(self, record):  # 定义私有函数insert，作为插入数据的核心函数
            tick = 0  # 初始化计数器
            # 当计数器不超过列表长度时，使用ISBN进行顺序排序；对于类，有属性可用于确定列表中某项的值
            while tick < len(self.bookList) and record.ISBN > self.bookList[tick].ISBN:
                tick += 1
            # 当计数器不超过列表长度时，如果某个记录的ISBN号与现在要插入的ISBN号冲突
            if tick < len(self.bookList) and record.ISBN == self.bookList[tick].ISBN:
                print(record.ISBN+"已经存在")
                return False  # 返回False
            # 否则如果直到遍历完比要插入的ISBN号小的号，也没有相同的ISBN号，则将记录插入到比传入的ISBN号小的记录的后面
            self.bookList.insert(tick, record)
            print("增加成功")
            return True  # 返回True

        def __update(self, record):  # 定义私有函数update，用以更改指定数据
            judgement = False  # 将判断变量改为False
            for i in range(len(self.bookList)):  # 获得书表的长度
                # 遍历书表中每本书的ISBN号，如果存在，那就更改记录
                if record.ISBN == self.bookList[i].ISBN:
                    self.bookList[i].title = record.title
                    self.bookList[i].author = record.author
                    self.bookList[i].publisher = record.publisher
                    print("修改成功")
                    judgement = True  # 将判断变量改为True
                    break
            if not judgement:  # 如果判断变量不为正
                print("没有此教材")  # 输出错误
            return judgement  # 返回判断变量的值

        def __delete(self, ISBN):  # 定义私有函数delete，用以删除数据
            judgement = False
            for i in range(len(self.bookList)):
                if self.bookList[i].ISBN == ISBN:  # 如果存在ISBN号
                    del self.bookList[i]  # 删除列表中那本书的数据
                    print("删除成功")
                    judgement = True
                    break
            if not judgement:
                print("没有此教材")
            return judgement

        def delete(self):  # 定义函数用以处理要删除的数据
            ISBN = input("ISBN=")
            if ISBN != "":  # 如果传入的ISBN不为空，则删除指定的ISBN所在的列表
                self.__delete(ISBN)

        def insert(self):  # 定义函数用以处理要插入的数据
            ISBN = input("ISBN=")
            title = input("Title=")
            author = input("Author=")
            publisher = input("Publisher=")
            if ISBN != "" and title != "":
                # 将数据传入类book进行格式化并将值附加至book的属性后，在insert中获取属性值并插入至书表中
                self.__insert(book(ISBN, title, author, publisher))
            else:
                print("ISBN与教材名称不能为空")

        def update(self):  # 定义函数用以处理要更改的数据
            ISBN = input("ISBN=")
            title = input("Title=")
            author = input("Author=")
            publisher = input("Publisher=")
            if ISBN != "" and title != "":
                # 确认ISBN号与标题不为空后更改表内容
                self.__update(book(ISBN, title, author, publisher))
            else:
                print("ISBN与教材名称不能为空")

        def save(self):  # 定义函数用以保存数据
            try:
                file = open("bookList.txt", "wt")  # 以文本写入方式打开文件
                for book in self.bookList:  # 遍历书表，并将每个属性值写入至文件中，每个值用换行符分隔
                    file.write(book.ISBN+"\n")
                    file.write(book.title+"\n")
                    file.write(book.author+"\n")
                    file.write(book.publisher+"\n")
                file.close()  # 写入所有值后关闭文件
            except Exception as err:
                print(err)

        def read(self):  # 定义函数用以读取文件内存储的数据
            self.bookList = []  # 初始化书表
            try:
                file = open("bookList.txt", "rt")  # 读文件
                while True:  # 读取每一行，并去除每一行末尾的换行符
                    ISBN = file.readline().strip("\n")
                    title = file.readline().strip("\n")
                    author = file.readline().strip("\n")
                    publisher = file.readline().strip("\n")
                    if ISBN != "" and title != "" and author != "" and publisher != "":  # 对于四个属性填写不完全的，在读取时会中止，因此只有有效的数据会被插入至书表中
                        self.bookList.append(
                            book(ISBN, title, author, publisher))
                    else:
                        break
                file.close()
            except Exception as err:
                pass  # pass语句用以对某个判断或条件语句进行占位，即使条件被触发了，也不做任何事

        def process(self):
            self.read()
            while True:
                print("1.列出 2.插入 3.更改 4.删除 5.退出")
                string = input()
                if string == "1":
                    self.show()
                elif string == "2":
                    self.insert()
                elif string == "3":
                    self.update()
                elif string == "4":
                    self.delete()
                elif string == "5":
                    break
            self.save()  # 在每次退出后保存书表内的数据到文件内

    books = bookList()
    books.process()


p186_662()


def p191_exercise():

    def exercise1():
        file = open("abc.txt", "wt")
        file.write("abc\n")
        file.close()
        file = open("abc.txt", "rb")
        print(len(file.read()))  # 换行符包含两个字节的位置
        file.close()

    exercise1()

    def exercise2():
        try:
            file = open("xyz.txt", "rt")
            tick = 0
            while True:
                read = file.read(1)
                if read == "":
                    break
                tick += 1
            print(tick)
        except Exception as err:
            print(err)

    exercise2()

    def exercise4():
        file = open("marks.txt", "rt", encoding="utf-8")
        list = []
        while True:
            read = file.readline().strip("\n").split(" ")
            if read[0] == "":
                break
            read[1] = float(read[1])
            list.append(read)
        file.close()
        for each in range(len(list)):
            for next in range(each+1, len(list)):
                if list[next][1] > list[each][1]:
                    buffer = list[each]
                    list[each] = list[next]
                    list[next] = buffer
        print(list)
        file = open("sorted.txt", "wt")
        for i in list:
            file.write(i[0]+" "+str(i[1])+"\n")
        file.close()

    exercise4()

    def exercise5():
        file=open("abc.txt","wb")
        file.write("abc\r\nxyz\n\r123\r456\n".encode())
        file.close()
        file=open("abc.txt","rt")
        while True:
            read=file.read(1)
            if read == "":
                break
            print(read)
        file.close()

    exercise5()


# p191_exercise()


def p195_711():
    import pymysql  # 导入pymysql库
    try:
        # host指安装了MySQL的IP地址，port指端口号，默认为3306，user指MySQL的管理账号，passwd即密码，db指想要连接的数据库，charset即字符集，对应open()函数的encoding参数
        connect = pymysql.connect(host="10.1.85.172", port=3306,
                                  user="root", passwd="123456", db="mydb", charset="utf8")
        print("连接成功")
        connect.close()  # 类似于文件系统，连接到数据库执行完指令后也需要关闭
    except Exception as err:
        print(err)


# p195_711()


def p195_712():
    import pymysql
    # sql变量指定了需要在数据库内执行的命令，五条指令从上到下依次是，创建名为students的表，属性有Num，值的最大长度为16字符，是主键；
    # 属性有Name，最大长度16；属性有Gender，最大长度16；属性有Age，其值为整数类型；对于在python编辑器中参入了换行符的字符串，需要在上下两侧分别加入三个引号以示字符串
    sql = """
    create table students
    (
        Num varchar(16) primary key,
        Name varchar(16),
        Gender varchar(16),
        Age int
    )
    """
    connect = pymysql.connect(host="10.1.85.172", port=3306,
                              user="root", passwd="123456", db="mydb", charset="utf8")
    # 对于数据库连接，有游标系统用以对数据库执行指定的操作，以pymsql创建一个指针，其中DictCursor指将查询到的结果格式化为字典格式，并将创建的指针赋予给已连接的数据库
    cursor = connect.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute(sql)  # 执行的命令则是在游标上执行的
        print("执行成功")
    except Exception as err:
        print(err)
    connect.close()


# p195_712()


def p196_714():
    import pymysql
    sql = """
    create table students
    (
        Num varchar(16) primary key,
        Name varchar(16),
        Gender varchar(16),
        Age int
    )
    """
    connect = pymysql.connect(host="10.1.85.172", port=3306,
                              user="root", passwd="123456", db="mydb", charset="utf8")
    cursor = connect.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute(sql)  # 如果表已创建，则会返回错误信息，即此语句不能被成功执行
    except:
        # 如果表已存在，则执行语句，即从学生表中删除所有记录，且不包括表的属性等
        cursor.execute("delete from students")
    # 在MySql中，有简写语法，这意味着只要按照属性顺序填写值即可
    cursor.execute("insert into students values('1','A','男','20')")
    # 以下MySql语句为，将值2,B,女,21插入至学生表，需要注意的是，MySql语句对双引号敏感，因此对于字符串，需要有单引号以声明此为字符串
    cursor.execute("insert into students values('2','B','女','21')")
    connect.commit()  # 由于在数据库中存在事务系统，因此如果需要对数据库做出改变，必须向数据库提交更改，否则操作未完成，数据库会回滚至改动前的状态
    connect.close()
    print("完成")


# p196_714()


def p199_721():
    p196_714()  # 先决条件
    import pymysql
    try:
        connect = pymysql.connect(host="10.1.85.172", port=3306,
                                  user="root", passwd="123456", db="mydb", charset="utf8")
        cursor = connect.cursor(pymysql.cursors.DictCursor)
        # 此Sql语句意为，从students表中选择所有记录
        cursor.execute("select * from students")
        while True:
            # fetchone，即获取一行；首先通过指针获得学生记录，再通过fetchone()方法一行行得到每行的内容；作为一个指针，其也具备执行指令后移动指针的特性；在此代码块中，通过一行行读取来达到读取全文的效果
            row = cursor.fetchone()
            print(row)
            if not row:  # 如果row的值为空
                break
        connect.close()
    except Exception as err:
        print(err)


# p199_721()


def p199_722():
    p196_714()
    import pymysql
    try:
        connect = pymysql.connect(host="10.1.85.172", port=3306,
                                  user="root", passwd="123456", db="mydb", charset="utf8")
        cursor = connect.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select * from students")
        while True:
            row = cursor.fetchone()
            if not row:
                break
            print(row["Name"], row["Gender"], row["Age"])  # 使用列表特性获取每个键的值
        connect.close()
    except Exception as err:
        print(err)


# p199_722()


def p200_723():
    p196_714()
    import pymysql
    try:
        connect = pymysql.connect(host="10.1.85.172", port=3306,
                                  user="root", passwd="123456", db="mydb", charset="utf8")
        cursor = connect.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select * from students")
        rows = cursor.fetchall()  # 通过使用fetchall()方法，可从指针中取得全部记录
        for row in rows:  # 遍历每一行
            print(row["Name"], row["Gender"], row["Age"])
        connect.close()
    except Exception as err:
        print(err)


# p200_723()


def p201_723():
    import pymysql
    try:
        connect = pymysql.connect(host="10.1.85.172", port=3306,
                                  user="root", passwd="123456", db="mydb", charset="utf8")
        cursor = connect.cursor(pymysql.cursors.DictCursor)
        cursor.execute("delete from students")
        # 对于指针系统，有内置变量rowcount用以记录由于上次更改相关的操作而受到影响的行数为多少
        print(f"删除全部学生后{cursor.rowcount}")
        cursor.execute("insert into students values('1','A','男','20')")
        print(f"添加第一个记录后{cursor.rowcount}")
        cursor.execute("insert into students values('2','B','女','21')")
        print(f"添加第二个记录后{cursor.rowcount}")
        # 更改学生表内编号为1的学生姓名为X
        cursor.execute("update students set Name='X' where Num='1'")
        print(f"更改记录1后{cursor.rowcount}")
        # 更改学生表内编号为3的学生姓名为X
        cursor.execute("update students set Name='X' where Num='3'")
        print(f"更改记录3后{cursor.rowcount}")  # 由于编号3并不存在，因此未做任何改动，因此rowcount数为0
        cursor.execute("delete from students where Num='1'")  # 删除编号为1的学生
        print(f"删除记录1后{cursor.rowcount}")
        cursor.execute("delete from students where Num='3'")  # 删除编号为3的学生
        print(f"删除记录3后{cursor.rowcount}")  # 由于编号3并不存在，因此未做任何改动，因此rowcount数为0
        connect.commit()  # 提交更改，即在数据库表中，两个记录的姓名均为"X"
        connect.close()
    except Exception as err:
        print(err)


# p201_723()


def p204_733():
    import pymysql

    class studentDB:

        def open(self):#定义函数用以打开连接并创建表
            self.connect = connect = pymysql.connect(
                host="10.1.85.172", port=3306, user="root", passwd="123456", db="mydb", charset="utf8")
            self.cursor = self.connect.cursor(pymysql.cursors.DictCursor)
            try:
                sql = """
                        create table students
                        (
                            Num varchar(16) primary key,
                            Name varchar(16),
                            Gender varchar(8),
                            Age int
                        )
                      """
                self.cursor.execute(sql)
            except:
                pass
            
        def close(self):#定义函数用以提交更改并关闭连接
            self.connect.commit()
            self.connect.close()

        def clear(self):#定义函数用以清空表内记录
            try:
                self.cursor.execute("delete from students")
            except Exception as err:
                print(err)

        def show(self):#定义函数用以显示表内容
            self.cursor.execute("select Num,Name,Gender,Age from students")#选择相关属性的所有值
            print("%-16s%-16s%-8s%-4s" % ("Num","Name","Gender","Age"))#按一定格式输出各属性名
            rows=self.cursor.fetchall()#获得游标的所有内容
            for row in rows:#遍历每行内容
                print("%-16s%-16s%-8s%-4d" % (row["Num"],row["Name"],row["Gender"],row["Age"]))#输出每行中每个键具体的值

        def insert(self,Num,Name,Gender,Age):#定义函数用以插入数据到表内
            try:
                sql="insert into students values(%s,%s,%s,%s)"#对于pymysql，可以传入一个元组作为需要插入的值，并格式化
                self.cursor.execute(sql,(Num,Name,Gender,Age))#元组值作为可选参数使用，在需要时传入至Sql语句内
                print(self.cursor.rowcount,"行已插入")
            except Exception as err:
                print(err)
        
        def update(self,Num,Name,Gender,Age):#定义函数用以更改表内数据
            try:
                sql="update students set Name=%s,Gender=%s,Age=%s where Num=%s"
                self.cursor.execute(sql,(Name,Gender,Age,Num))
                print(self.cursor.rowcount,"行已更新")
            except Exception as err:
                print(err)

        def delete(self,Num):
            try:
                sql="delete from students where Num=%s"
                self.cursor.execute(sql,(Num,))#只有在变量内加入逗号，这个变量才会被视为元组的元素
                print(self.cursor.rowcount,"行已删除")
            except Exception as err:
                print(err)
        
    db=studentDB()
    db.open()
    db.clear()
    db.insert("5","E","女",32)
    db.show()
    db.update("5","X","女",30)
    db.show()
    db.insert("1","A","男",20)
    db.show()
    db.delete("1")
    db.show()
    db.close()


#p204_733()


def p208_741():#sqlite是一个轻量级的数据文件管理系统，数据库的所有内容都被存储在一个文件内
    import sqlite3
    try:
        connect=sqlite3.connect("students.db")#如果文件不存在，则创建，否则接入此文件
        print("连接成功")
        connect.close()
    except Exception as err:
        print(err)


#p208_741()


def p209_742():
    import sqlite3
    sql = """
            create table students
            (
                Num varchar(16) primary key,
                Name varchar(16),
                Gender varchar(8),
                Age int
            )
            """
    try:
        connect = sqlite3.connect("students.db")
        cursor=connect.cursor()
        try:
            cursor.execute(sql)
        except:
            cursor.execute("delete from students")
        cursor.execute("insert into students values('1','A','男','20')")
        cursor.execute("insert into students values('2','B','女','21')")
        cursor.execute("select * from students")
        rows=cursor.fetchall()#如果不指定指针的读取模式，则默认的sqlite输出格式为元组型
        for row in rows:
            print(row[0],row[1],row[2],row[3])#使用索引用以输出每个值
        connect.commit()
        connect.close()
    except Exception as err:
        print(err)


#p209_742()


def p210_745():
    p209_742()
    import sqlite3
    try:
        connect = sqlite3.connect("students.db")
        cursor=connect.cursor()
        cursor.execute("delete from students")
        print(f"删除了{cursor.rowcount}行")#sqlite3中的rowcount功能与pymysql中的功能相同
        #在sqlite中，对于需要传入至sql语句的值，在sql语句内用英文问号来指定，sql语句内无内置格式化
        cursor.execute("insert into students values(?,?,?,?)",("1","A,","男",20))
        print(f"增加了{cursor.rowcount}行")
        cursor.execute("insert into students values(?,?,?,?)",("2","B,","女",21))
        print(f"增加了{cursor.rowcount}行")
        cursor.execute("update students set Name=? where Num=?",("X",1))
        print(f"更改了{cursor.rowcount}行")
        cursor.execute("update students set Name=? where Num=?",("X",3))
        print(f"更改了{cursor.rowcount}行")
        cursor.execute("delete from students where Num=?",(1,)) 
        print(f"删除了{cursor.rowcount}行")
        cursor.execute("delete from students where Num=?",(3,))  
        print(f"删除了{cursor.rowcount}行")
        connect.commit()
        connect.close()
    except Exception as err:
        print(err)
    #因此，sqlite与MySQL类似，只是sqlite是基于本地的轻量级数据库

p210_745()

            
