"""
@date:2020-07-27
@time：15:13
@author:smq
@description:描述
"""
from App.dbModel import *
from App.myTime import *
from App.rpt.rptConfig import *


# 单品日表
def tb_proD(t0=getDayBeforeToday(7), t1=getDayBeforeToday(1)):
    # 可以在设置里修改常用ID列表,此处建议不要修改
    good_list = list(FOW_GOOD_ID.keys())
    # 根据时间生成时间列表
    timeList = getDateList(t0, t1)
    # 返回结果
    data = {
        "header": ['日期', '商品ID', "商品名称", '访客数', '销售额', '买家数', '转化率', "客单价", '收藏人数', "销售占比"],
        "data": {},
        "sortKey": "访客数"
    }
    for time in timeList:
        shop = SycmShopSaleD.query.filter(SycmShopSaleD.createtime == time).first()
        data["data"][time] = {}
        if shop:
            sale = shop.sale_amt
            data["data"][time]["total"] = {"日期": time, "商品ID": "生意参谋全店", "商品名称": "全部", "访客数": shop.UV,
                                           "销售额": shop.sale_amt, "买家数": shop.sale_num, "转化率": shop.sale_roc,
                                           "客单价": shop.per_price, "收藏人数": shop.collect_num, "销售占比": 1}
        else:
            sale = 1
            data["data"][time]["total"] = {"日期": time, "商品ID": "生意参谋全店", "商品名称": "暂未产出", "访客数": 1,
                                           "销售额": 1, "买家数": 1, "转化率": 1,
                                           "客单价": 1, "收藏人数": 1, "销售占比": 1}
        data["data"][time]["detail"] = []
        for good in good_list:
            item = ProSaleD.query.filter(ProSaleD.goods_id == good, ProSaleD.createtime == time).first()
            if item:
                data["data"][time]["detail"].append({"日期": time, "商品ID": good, "商品名称": FOW_GOOD_ID[good], "访客数": item.UV, "销售额": item.sale_amt,
                                                     "买家数": item.sale_num, "转化率": item.sale_roc, "客单价": item.per_price,
                                                     "收藏人数": item.collect_num, "销售占比": round(item.sale_amt / sale, 4)})
    return data


# 单品日对比,默认同上周事件对比
def tb_proD_comp(t0=getYesterday(), t1=getDayBeforeToday(7)):
    return {}


# 单品周数据对比,默认选择昨天年份
def tb_flowW_comp(n0, n1, year=getYesterday()):
    n0, n1 = int(n0), int(n1)
    # 对比第几周和第几周
    data = {
        "title": "单品周数据UV去重",
        "tableData": {},
        "status": "ok",
        "sortKey": "访客数",
    }
    t0S, t0E = getWeekList(year)[n0 + 1].split('~')
    t1S, t1E = getWeekList(year)[n1 + 1].split('~')

    return data


# 单品销售指定周期对比数据,可以选定任意时间段
def tb_saleW_comp(T0, T1):
    t0s, t0e = T0.split('~')
    t1s, t1e = T1.split('~')
    ProSaleD.query.filter(ProSaleD.createtime)
    data = {
        "title": "单品销售指定周期对比,流量按天汇总",
        "tableDate": {},
        "status": "ok"
    }
    tableData = {
        "conner": [["商品ID", "商品简称"]],
        "columns": [["时间周期", "时间周期", "增幅"], ["-", "-"], ["访客数1", ""]]
    }

    return data


# 每日top5商品的基本信息
def pro_top5_by_day():
    thead = ["商品名称", "访客数", "销售额", "买家数", "转化率", "客单价", "手淘搜索", "付费推广", "购物车", "我的淘宝"]
    tbody = []
    data = {"thead": thead, "status": "ok"}
    saleD = ProSaleD.query.filter(ProSaleD.createtime == getYesterday()).order_by(db.desc(ProSaleD.sale_amt)).all()
    if saleD:
        for i in range(5):
            piece = saleD[i]
            Flow = ProFlowD.query.filter(ProFlowD.createtime == getYesterday(), ProFlowD.goods_id == piece.goods_id)
            if Flow.all():
                # 取6个渠道的访客数据
                a = Flow.filter(ProFlowD.flow_source_detail == "手淘搜索").first()
                b = Flow.filter(ProFlowD.flow_source_detail == "直通车").first()
                c = Flow.filter(ProFlowD.flow_source_detail == "智钻").first()
                d = Flow.filter(ProFlowD.flow_source_detail == "超级推荐").first()
                e = Flow.filter(ProFlowD.flow_source_detail == "购物车").first()
                f = Flow.filter(ProFlowD.flow_source_detail == "我的淘宝").first()
                a = a.UV if a else 0
                b = b.UV if b else 0
                c = c.UV if c else 0
                d = d.UV if d else 0
                e = e.UV if e else 0
                f = f.UV if f else 0
                tbody.append({"商品名称": GOOD_DICT[piece.goods_id] if piece.goods_id in GOOD_DICT.keys() else piece.goods_id,
                              "访客数": piece.UV,
                              "销售额": "%.2f" % piece.sale_amt,
                              "买家数": piece.sale_num,
                              "转化率": '%.2f' % (piece.sale_roc * 100) + "%",
                              "客单价": "%.2f" % piece.per_price,
                              "手淘搜索": a,
                              "付费推广": b + c + d,
                              "购物车": e,
                              "我的淘宝": f})
            else:
                tbody.append({"商品名称": GOOD_DICT[piece.goods_id] if piece.goods_id in GOOD_DICT.keys() else piece.goods_id,
                              "访客数": piece.UV,
                              "销售额": "%.2f" % piece.sale_amt,
                              "买家数": piece.sale_num,
                              "转化率": '%.2f' % (piece.sale_roc * 100) + "%",
                              "客单价": "%.2f" % piece.per_price,
                              "手淘搜索": "暂未产出",
                              "付费推广": "暂未产出",
                              "购物车": "暂未产出",
                              "我的淘宝": "暂未产出"})
                data["status"] = "part ok"
    else:
        for i in range(5):
            tbody.append({"商品名称": "暂未产出",
                          "访客数": "暂未产出",
                          "销售额": "暂未产出",
                          "买家数": "暂未产出",
                          "转化率": "暂未产出",
                          "客单价": "暂未产出",
                          "手淘搜索": "暂未产出",
                          "付费推广": "暂未产出",
                          "购物车": "暂未产出",
                          "我的淘宝": "暂未产出"})
        data["status"] = "please wait"
    data["tbody"] = tbody
    return data


if __name__ == '__main__':
    pro_top5_by_day()
