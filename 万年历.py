# 判断是否是闰年
def isleapyear(year):
    return True if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0 else False

# 判断每个月有多少天
def monthday(year,month):
    daylist=[31,28,31,30,31,30,31,31,30,31,30,31]
    if isleapyear(year):
        daylist[1]= 29
    return daylist[month-1]

# 距离1900年1月1日的天数
def totalday(year,month):
    day=0
    for y in range(1900,year):
        day += 366 if isleapyear(y) else 365
    for m in range(1,month):
        day += monthday(year,m)
    return day

# 定义一个展示函数
def show():
    year,month = eval(input("请输入年份和月份："))
    # 判断空格数
    print(totalday(year,month))
    space_num = totalday(year,month)%7+1
    # print(space_num)

    print(" 星期日\t一\t二\t三\t四\t五\t六")

    for d in range(1,monthday(year,month)+1):
        if d == 1:
            for i in range(space_num%7):
                print("\t",end="")
        print("\t%2d"%d,end="")
        if (d+space_num)%7 == 0:
            print()




show()

