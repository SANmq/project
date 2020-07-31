"""
@date:2020-07-27
@time：13:32
@author:smq
@description:描述
"""
from flask import Blueprint, request, redirect, url_for, jsonify
from App.gFun import prove_login, get_user_config
from App.rpt.handle import *
from App.rpt.api import *

rpt = Blueprint('rpt', __name__)


@rpt.route('/rpt/<string:name>', methods=['GET', 'POST'])
def rptHome(name):
    user = request.cookies.get('user')
    if prove_login(user):
        # 登录成功
        if name == "单品数据":
            context = {"title": name,
                       "smallTitle": "昨日商品销售排名top5商品(注:正常时间9点半出)",
                       "tableList": ["单品销售展示", "单品销售对比", "单品剔除淘客对比", "单品流量对比", "单品流量数据"],
                       "css": [url_for("static", filename="css/layout.css"), url_for("static", filename="css/单品数据.css")],
                       "user": get_user_config(user),
                       "top": pro_top5_by_day(),
                       "js": [url_for("static", filename="js/单品数据.js")]
                       }
            return render_template('rptBase1.html', **context)
        else:
            return render_template('error.html', err="没有这张表哦")
    else:
        return redirect(url_for('login.home'))


@rpt.route('/rpt/api/<string:name>', methods=["POST", "GET"])
def rptApi(name):
    user = request.cookies.get('user')
    if prove_login(user):
        user_config = get_user_config(user)
        print("当前用户{}访问表{}".format(user_config.name, name))

        if name == "单品销售展示":
            t0 = getDayBeforeToday(40)
            t1 = getDayBeforeToday(1)
            goodID = "35399645973"
            rqType = "select"
            if request.method == "POST":
                if "t0" in request.form.keys() and "t1" in request.form.keys():
                    t0 = request.form.get("t0")
                    t1 = request.form.get("t1")
                    if "goodID" in request.form.keys():
                        goodID = request.form.get("goodID")
                    if "rqType" in request.form.keys():
                        rqType = request.form.get("rqType")
                    if t0 > t1:
                        temp = t0
                        t0 = t1
                        t1 = temp
            return pro_sale_show(t0, t1, goodID, rqType)
        elif name == "单品销售对比":
            rqType = "select"
            T0 = getWeekBeforeToday(1)
            T1 = getWeekBeforeToday(2)
            if request.method == "POST":
                if "T0" in request.form.keys() and "T1" in request.form.keys():
                    T0 = request.form.get("T0")
                    T1 = request.form.get("T1")
                    if "rqType" in request.form.keys():
                        rqType = request.form.get("rqType")
            return pro_sale_compare_show(T0, T1, rqType)
        if name == "单品剔除淘客对比":
            rqType = "select"
            T0 = getWeekBeforeToday(1)
            T1 = getWeekBeforeToday(2)
            if request.method == "POST":
                if "T0" in request.form.keys() and "T1" in request.form.keys():
                    T0 = request.form.get("T0")
                    T1 = request.form.get("T1")
                    if "rqType" in request.form.keys():
                        rqType = request.form.get("rqType")
            return pro_sale_filter_taoke(T0, T1, rqType)

        return render_template("error.html", err="没有这个接口")
    else:
        return jsonify({"status": "失败"})


@rpt.route('/rpt/api/', methods=["POST", "GET"])
def rptApiInfo():
    return "这里是接口的相关文档"
