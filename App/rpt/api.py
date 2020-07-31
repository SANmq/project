"""
@date:2020-07-29
@time：10:14
@author:smq
@description:接口数据传递
"""
from App.dbModel import *
from App.myTime import *
from App.rpt.rptConfig import *
from flask import render_template
from sqlalchemy import func, and_, or_
from App.rpt.myCalc import *


# 单品销售展示

def pro_sale_show(t0, t1, goodID, rqType):
    thead = ["日期", "店铺节奏", "访客数", "销售额", "销售占比", "买家数", "转化率", "支付件数",
             "加购件数", "加购率", "收藏人数", "客单价", "件单价", "人均件数"]
    tbody = []
    data = {"goodID": goodID,
            "goodName": GOOD_DICT[goodID] if goodID in GOOD_DICT.keys() else goodID,
            "tRound1": "{}~{}".format(t0, t1),
            "tableData": {
                "title": "单品销售展示",
                "thead": thead,
            },
            "status": "ok"
            }
    data["tableData"]["tbody"] = tbody
    dateList = getDateList(t0, t1)
    for d in dateList:
        piece = ProSaleD.query.filter(ProSaleD.createtime == d, ProSaleD.goods_id == goodID).first()
        if piece:
            shop_sale = SycmShopSaleD.query.filter(SycmShopSaleD.createtime == d).first()
            shop_sale = shop_sale.sale_amt if shop_sale else 1
            sale_zb = "%.2f" % (piece.sale_amt / shop_sale * 100) + "%"
            active = ActivityD.query.filter(ActivityD.createtime == d).first()
            active = active.status if active.status else "暂未更新"
            tbody.append({
                "日期": d,
                "店铺节奏": active,
                "访客数": piece.UV,
                "销售额": "%.2f" % piece.sale_amt,
                "销售占比": sale_zb,
                "买家数": piece.sale_num,
                "转化率": "%.2f" % (piece.sale_roc * 100) + "%",
                "支付件数": piece.sale_qty,
                "加购件数": piece.gwc_qty,
                "加购率": "%.2f" % (piece.gwc_num / piece.UV * 100) + "%",
                "收藏人数": piece.collect_num,
                "客单价": "%.2f" % (piece.per_price if piece.per_price else 0),
                "件单价": "%.2f" % (piece.sale_amt / (piece.sale_qty if piece.sale_qty else 1)),
                "人均件数": "%.2f" % (piece.sale_qty / (piece.sale_num if piece.sale_num else 1))
            })
        else:
            tbody.append({
                "日期": d,
                "店铺节奏": "暂无数据",
                "访客数": "暂无数据",
                "销售额": "暂无数据",
                "销售占比": "暂无数据",
                "买家数": "暂无数据",
                "转化率": "暂无数据",
                "支付件数": "暂无数据",
                "加购件数": "暂无数据",
                "加购率": "暂无数据",
                "收藏人数": "暂无数据",
                "客单价": "暂无数据",
                "件单价": "暂无数据",
                "人均件数": "暂无数据"
            })
    if rqType == "download":
        data["downloadTable"] = render_template("downloadTable.html", table=data["tableData"])
    else:
        data["renderTable"] = render_template("renderTable.html", table=data["tableData"], tableId="tb0")
    return data


def pro_sale_compare_show(T0, T1, rqType):
    t0S, t0E = T0.split('~')
    t1S, t1E = T1.split('~')
    good_list = list(PRO_SALE_ID.keys())
    index = ["商品ID", "商品简称"]
    thead = ["访客数", "销售额", "买家数", "转化率", "加购件数", "加购率", "UV价值"]
    showThead = ["访客数", "销售额", "买家数", "转化率",]
    data = {"error": "",
            "tRound1": "{}~{}".format(t0S, t0E),
            "tRound2": "{}~{}".format(t1S, t1E),
            }

    def sgS(a, b, c):
        return ProSaleD.query.filter(ProSaleD.createtime.between(a, b), ProSaleD.goods_id.in_(c)).group_by(
            ProSaleD.goods_id).with_entities(ProSaleD.goods_id.label("goods_id"),
                                             func.sum(ProSaleD.UV).label("UV"),
                                             func.sum(ProSaleD.sale_amt).label("sale_amt"),
                                             func.sum(ProSaleD.sale_num).label("sale_num"),
                                             (func.sum(ProSaleD.sale_num) / func.sum(ProSaleD.UV)).label("sale_roc"),
                                             (func.sum(ProSaleD.sale_amt) / func.sum(ProSaleD.UV)).label("UV_value"),
                                             func.sum(ProSaleD.gwc_qty).label("gwc_qty"),
                                             (func.sum(ProSaleD.gwc_num) / func.sum(ProSaleD.UV)).label("gwc_roc")
                                             ).all()

    s1 = sgS(t0S, t0E, good_list)
    s2 = sgS(t1S, t1E, good_list)

    def qu(_s):
        tr = {}
        for i in _s:
            tr[i.goods_id] = {
                "访客数": int(i.UV),
                "销售额": float(i.sale_amt),
                "买家数": int(i.sale_num),
                "转化率": float(i.sale_roc),
                "UV价值": float(i.UV_value),
                "加购件数": int(i.gwc_qty),
                "加购率": float(i.gwc_roc)
            }
        return tr

    tr1, tr2 = qu(s1), qu(s2)
    cmp = {}
    for k in tr1:
        cmp[k] = {}
        for j in tr1[k]:
            cmp[k][j] = chu(tr1[k][j], tr2[k][j]) - 1
        tr1[k], tr2[k], cmp[k] = ge(tr1[k]), ge(tr2[k]), ge(cmp[k], True)
        tr1[k]["商品ID"] = tr2[k]["商品ID"] = cmp[k]["商品ID"] = k
        tr1[k]["商品简称"] = tr2[k]["商品简称"] = cmp[k]["商品简称"] = GOOD_DICT[k]

    data["tableData"] = {
        "title": "单品销售对比",
        "index": index,
        "thead": thead,
        "showThead": showThead,
        "tRound1": list(tr1.values()),
        "tRound2": tr2,
        "compare": cmp,
        "tableID": "tb1"
    }
    if rqType == "download":
        data["downloadTable"] = render_template("downloadTable.html", table=data["tableData"])
    else:
        data["renderTable"] = render_template("renderTable.html", table=data["tableData"])
    return data


# 单品剔除淘客对比
def pro_sale_filter_taoke(T0, T1, rqType):
    goodList = FOW_GOOD_ID.keys()
    t0S, t0E = T0.split('~')
    t1S, t1E = T1.split('~')
    index = ["商品ID", "商品简称"]
    thead = ["访客数", "销售额", "买家数", "转化率", "UV价值"]
    showThead = ["访客数", "买家数", "转化率"]
    data = {
        "status": "ok",
        "tRound1": "{}~{}".format(t0S, t0E),
        "tRound2": "{}~{}".format(t1S, t1E),
    }

    def sgS(a, b, c):
        return ProSaleD.query.filter(ProSaleD.createtime.between(a, b), ProSaleD.goods_id.in_(c)).group_by(
            ProSaleD.goods_id).with_entities(ProSaleD.goods_id.label("goods_id"),
                                             func.sum(ProSaleD.UV).label("UV"),
                                             func.sum(ProSaleD.sale_amt).label("sale_amt"),
                                             func.sum(ProSaleD.sale_num).label("sale_num"),
                                             (func.sum(ProSaleD.sale_num) / func.sum(ProSaleD.UV)).label("sale_roc"),
                                             (func.sum(ProSaleD.sale_amt) / func.sum(ProSaleD.UV)).label("UV_value")
                                             ).all()

    def sgF(a, b, c):
        return ProFlowD.query.filter(ProFlowD.createtime.between(a, b), ProFlowD.goods_id.in_(c),
                                     ProFlowD.flow_source_detail == "淘宝客").group_by(ProFlowD.goods_id).with_entities(
            ProFlowD.goods_id.label("goods_id"),
            func.sum(ProFlowD.UV).label("UV"),
            func.sum(ProFlowD.sale_amt).label("sale_amt"),
            func.sum(ProFlowD.sale_num).label("sale_num"),
            (func.sum(ProFlowD.sale_num) / func.sum(ProFlowD.UV)).label("sale_roc"),
            (func.sum(ProFlowD.sale_amt) / func.sum(ProFlowD.UV)).label("UV_value")
        ).all()

    s1 = sgS(t0S, t0E, goodList)
    s2 = sgS(t1S, t1E, goodList)
    f1 = sgF(t0S, t0E, goodList)
    f2 = sgF(t1S, t1E, goodList)

    def qu(_s, _f):
        tr = {}
        for i in _s:
            tr[i.goods_id] = {
                "访客数": int(i.UV),
                "销售额": float(i.sale_amt),
                "买家数": int(i.sale_num),
                "转化率": float(i.sale_roc),
                "UV价值": float(i.UV_value)
            }
        for i in _f:
            tr[i.goods_id]["访客数"] -= int(i.UV)
            tr[i.goods_id]["销售额"] -= float(i.sale_amt)
            tr[i.goods_id]["买家数"] -= int(i.sale_num)
            tr[i.goods_id]["转化率"] -= float(i.sale_roc)
            tr[i.goods_id]["UV价值"] -= float(i.UV_value)
        return tr

    tr1 = qu(s1, f1)
    tr2 = qu(s2, f2)
    cmp = {}
    for k in tr1:
        cmp[k] = {}
        for j in tr1[k]:
            cmp[k][j] = chu(tr1[k][j], tr2[k][j]) - 1
        tr1[k], tr2[k], cmp[k] = ge(tr1[k]), ge(tr2[k]), ge(cmp[k], True)
        tr1[k]["商品ID"] = tr2[k]["商品ID"] = cmp[k]["商品ID"] = k
        tr1[k]["商品简称"] = tr2[k]["商品简称"] = cmp[k]["商品简称"] = GOOD_DICT[k]

    data["tableData"] = {
        "title": "单品剔除淘客对比",
        "index": index,
        "thead": thead,
        "showThead": showThead,
        "tRound1": list(tr1.values()),
        "tRound2": tr2,
        "compare": cmp,
        "tableID": "tb2"
    }

    if rqType == "download":
        data["downloadTable"] = render_template("downloadTable.html", table=data["tableData"])
    else:
        data["renderTable"] = render_template("renderTable.html", table=data["tableData"])
    return data


def pro_flow_show():
    return {}


if __name__ == '__main__':
    pass
    # T0 = getWeekBeforeToday(1)
    # T1 = getWeekBeforeToday(2)
    # aaa = pro_sale_filter_taoke(T0, T1, "select")
    # print(T0, T1, aaa)
