"""
@date:2020-07-31
@time：7:36
@author:smq
@description:描述
"""


def zhi(a):
    return a if a else 0


def chu(a, b):
    if b == 0 or a == 0:
        return 0
    else:
        return float(a) / float(b)


def ge(a, b=False):
    for key, value in a.items():
        if isinstance(value, str):
            continue
        else:
            if b:
                a[key] = "%.2f" % (value * 100) + "%"
            else:
                if "率" in key:
                    a[key] = "%.2f" % (value * 100) + "%"
                elif "数" in key:
                    a[key] = value
                elif "价值" in key or "额" in key:
                    a[key] = float("%.2f" % value)
    return a
