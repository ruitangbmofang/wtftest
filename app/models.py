# -*- coding:utf-8 -*-
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:1984423@192.168.3.149:3306/testforflask'
db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False, comment=u'用户名')
    password = db.Column(db.String(32), nullable=False, comment=u'密码')
    email = db.Column(db.String(50), unique=True, nullable=False, comment=u'邮箱')
    role = db.Column(db.Integer, default=1, comment=u'权限:0管理员,1成员')
    status = db.Column(db.Integer, comment=u'-1删除，0冻结，1正常', default=1)

    def __init__(self, username, password, email):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '%r' % self.username


class Case(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, comment=u'项目id')
    section_id = db.Column(db.Integer, comment=u'模块')
    title = db.Column(db.String(100), comment=u'标题')
    template_type = db.Column(db.Integer, comment=u'1接口用例，2功能用例')
    precondition = db.Column(db.String(200), comment=u'前提条件')
    content = db.Column(db.String(200), comment=u'用例描述')
    expected = db.Column(db.String(200), comment=u'期望结果')
    created_user_id = db.Column(db.Integer, comment=u'创建者id')
    created_time = db.Column(db.DateTime, default=datetime.now, comment=u'创建时间')
    updated_user_id = db.Column(db.Integer, nullable=True, comment=u'更新者id')
    updated_time = db.Column(db.DateTime, nullable=True, default=datetime.now, onupdate=datetime.now, comment=u'更新时间')
    keyword = db.Column(db.String(200), nullable=True, comment=u'关键字')


class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, comment=u'项目id')
    parent_id = db.Column(db.Integer, nullable=True, comment=u'父节点')
    name = db.Column(db.String(200), comment=u'名称')
    remark = db.Column(db.String(200), comment=u'备注')
    keyword = db.Column(db.String(200), nullable=True, comment=u'关键字')


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), comment=u'名称')
    description = db.Column(db.String(200), comment=u'描述')
    created_time = db.Column(db.DateTime, default=datetime.now, comment=u'创建时间')
    keyword = db.Column(db.String(200), nullable=True, comment=u'关键字')


class YouPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, comment=u'项目id')
    name = db.Column(db.String(200), nullable=False)
    case_ids = db.Column(db.String(200), comment=u'需要执行的用例id')
    description = db.Column(db.String(200), comment=u'描述')
    assignee_user_id = db.Column(db.String(200), comment=u'执行人员id', nullable=True)
    passed_count = db.Column(db.Integer, comment=u'通过的测试用例数量')
    failed_count = db.Column(db.Integer, comment=u'失败的测试用例数量')
    untested_count = db.Column(db.Integer, comment=u'未测试的测试用例数量')
    blocked_count = db.Column(db.Integer, comment=u'阻塞的测试用例数量')
    created_user_id = db.Column(db.Integer, comment=u'创建者id')
    created_time = db.Column(db.DateTime, default=datetime.now, comment=u'创建时间')
    updated_user_id = db.Column(db.Integer, nullable=True, comment=u'更新者id')
    updated_time = db.Column(db.DateTime, nullable=True, default=datetime.now, onupdate=datetime.now, comment=u'更新时间')


class RunObject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, comment=u'项目id')
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), comment=u'描述')
    assignee_user_id = db.Column(db.String(200), comment=u'执行人员id', nullable=True)


if __name__ == "__main__":
    db.drop_all()
    db.create_all()
