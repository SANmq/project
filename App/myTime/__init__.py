"""
@date:2020-07-27
@time：16:17
@author:smq
@description:自定义时间方法
"""
from datetime import date, timedelta, datetime
from re import findall


def getToday(fmt="%Y-%m-%d"):
    return date.today().strftime(fmt)


def getYesterday(fmt="%Y-%m-%d"):
    return (date.today() - timedelta(days=1)).strftime(fmt)


def getFirstDayOfMonth(fmt="%Y-%m-%d"):
    """
        获取获得一个月中的最后一天
        :return: string
        """
    any_day = date.today() - timedelta(days=1)
    next_month = any_day.replace(day=28) + timedelta(days=4)  # this will never fail
    return (next_month - timedelta(days=next_month.day)).strftime(fmt)


def getDayBeforeToday(delta, fmt="%Y-%m-%d"):
    return (date.today() - timedelta(days=delta)).strftime(fmt)


def getDateList(t0, t1, fmt="%Y-%m-%d"):
    dateList = []
    t0 = datetime.strptime(t0, fmt)
    t1 = datetime.strptime(t1, fmt)
    for i in range(730):
        if t0 > t1:
            break
        dateList.append(t1.strftime(fmt))
        t1 = t1 - timedelta(days=1)
    return dateList


def getWeekList(year, fmt="%Y-%m-%d"):
    year = findall('^\d{4}', year)[0]
    firstDay = date(int(year), 1, 1)
    fy, fwn, fdn = firstDay.isocalendar()
    nextDay = firstDay + timedelta(days=(8 - fdn))  # 这个是下周的第一天时间
    lastDay = date(int(year), 12, 31)
    ly, lwn, ldn = lastDay.isocalendar()
    endDay = lastDay - timedelta(days=(ldn + 6))
    weekList = [firstDay.strftime(fmt) + "~" + (nextDay - timedelta(days=1)).strftime(fmt)]
    while nextDay <= endDay:
        weekList.append(nextDay.strftime(fmt) + "~" + (nextDay + timedelta(days=6)).strftime(fmt))
        nextDay = nextDay + timedelta(days=7)
    weekList.append(nextDay.strftime(fmt) + "~" + lastDay.strftime(fmt))
    return weekList


# 获得当日所在周的前一周的周期时间
def getWeekBeforeToday(n):
    day = date.today()
    y, w, d = day.isocalendar()

    if w == 1:
        day = day - timedelta(days=7)
        y, w, d = day.isocalendar()
        w = w + 1

    return getWeekList(str(y))[w - n - 1]


def getTimedelta(a, b, fmt="%Y-%m-%d"):
    t0 = datetime.strptime(a, fmt)
    t1 = datetime.strptime(b, fmt)
    cha = t1 - t0
    return cha.days


if __name__ == '__main__':
    print(getTimedelta("2020-05-07", "2020-07-21"))
