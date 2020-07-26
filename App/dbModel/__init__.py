"""
@author:admin
@file: __init__.py.py
@time: 2020/07/25
@description:数据库模型初始化,
类命名规则，sale销售，flow流量，D日表，W周表，M月表，pro产品，shop店铺，tar目标，syj生意经维度，sycm，生意参谋维度，大驼峰格式命名
"""
from App.view import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


# 单品销售日表
class ProSaleD(db.Model):
    __tablename__ = 'f_product_sale_by_day'
    createtime = db.Column(db.DATE, primary_key=True)
    goods_id = db.Column(db.String(50), primary_key=True)
    PV = db.Column(db.Integer)
    UV = db.Column(db.Integer)
    sale_amt = db.Column(db.FLOAT(4))
    sale_qty = db.Column(db.Integer)
    sale_num = db.Column(db.Integer)
    per_price = db.Column(db.FLOAT(4))
    sale_roc = db.Column(db.FLOAT(4))
    collect_num = db.Column(db.Integer)
    gwc_num = db.Column(db.Integer)
    gwc_qty = db.Column(db.Integer)

    def __repr__(self):
        return self.goods_id


class ProFlowD(db.Model):
    __tablename__ = 'f_product_flow_by_day'
    createtime = db.Column(db.DATE, primary_key=True)
    goods_id = db.Column(db.String(50), primary_key=True)
    flow_source_detail = db.Column(db.String(50), primary_key=True)
    PV = db.Column(db.Integer)
    UV = db.Column(db.Integer)
    sale_amt = db.Column(db.FLOAT(4))
    sale_qty = db.Column(db.Integer)
    sale_num = db.Column(db.Integer)
    sale_roc = db.Column(db.FLOAT(4))
    collect_num = db.Column(db.Integer)
    gwc_num = db.Column(db.Integer)

    def __repr__(self):
        return self.goods_id


class ProFlowW(db.Model):
    __tablename__ = 'f_product_flow_by_week'

    def __repr__(self):
        return self.__tablename__


class ProFlowM(db.Model):
    __tablename__ = 'f_product_flow_by_month'

    def __repr__(self):
        return self.__tablename__


class ProSaleM(db.Model):
    __tablename__ = 'f_product_sale_by_month'

    def __repr__(self):
        return self.__tablename__


class SyjShopSaleD(db.Model):
    __tablename__ = 'f_shop_syj_sale_by_day'
    createtime = db.Column(db.DATE, primary_key=True)
    UV = db.Column(db.Integer)
    sale_amt = db.Column(db.FLOAT(4))
    sale_qty = db.Column(db.Integer)
    sale_num = db.Column(db.Integer)
    sale_roc = db.Column(db.FLOAT(4))
    per_price = db.Column(db.FLOAT(4))

    def __repr__(self):
        return self.__tablename__


class SycmShopSaleD(db.Model):
    __tablename__ = 'f_shop_sale_by_day'
    createtime = db.Column(db.DATE, primary_key=True)
    UV = db.Column(db.Integer)
    sale_amt = db.Column(db.FLOAT(4))
    sale_qty = db.Column(db.Integer)
    sale_num = db.Column(db.Integer)
    sale_roc = db.Column(db.FLOAT(4))
    per_price = db.Column(db.FLOAT(4))

    def __repr__(self):
        return self.createtime


class SycmShopSaleM(db.Model):
    __tablename__ = 'f_shop_sale_by_month'
    month_id = db.Column(db.Integer, primary_key=True)
    sale_amt = db.Column(db.FLOAT(4))
    sale_qty = db.Column(db.Integer)
    sale_num = db.Column(db.Integer)
    sale_roc = db.Column(db.FLOAT(4))
    old_sale_num = db.Column(db.Integer)  # 支付老买家数量
    old_sale_amt = db.Column(db.FLOAT(4))

    def __repr__(self):
        return self.month_id


class SycmShopFlowD(db.Model):
    __tablename__ = 'f_shop_flow_wx_by_day'
    createtime = db.Column(db.DATE, primary_key=True)
    flow_source = db.Column(db.String(50), primary_key=True)
    flow_source_detail = db.Column(db.String(50), primary_key=True)
    UV = db.Column(db.Integer)

    def __repr__(self):
        return self.__tablename__


class User(db.Model):
    __tablename__ = 'user'
    __bind_key__ = 'test'
    name = db.Column(db.String(255), primary_key=True)
    password = db.Column(db.String(255), primary_key=True)
    last = db.Column(db.BIGINT)
    num = db.Column(db.Integer, primary_key=True)
    modified = db.Column(db.TIMESTAMP)

    def __repr__(self):
        return self.__table__
