"""
@Name: 15.py

@Author: Drogon1573
@Date: 2019/6/13 23:13 CST
"""
import calendar
import datetime

if __name__ == "__main__":
    years = list()

    # 搜索符合要求的年份
    for year in range(1006, 1997, 10):
        date = datetime.datetime(year, 1, 27)
        if calendar.isleap(year) and date.weekday() == 1:
            years.append(year)

    # 排序（从小到大）并取出第2大的年份（年龄第2小）
    years.sort()
    print(years[-2])
