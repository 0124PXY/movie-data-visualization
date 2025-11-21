# -*- codeing = utf-8 -*-
# @Software ：IntelliJ IDEA
from flask import Flask,render_template
import sqlite3
app = Flask(__name__)

@app. route('/')
def index() :
    return render_template("index.html")

@app. route('/index')#网址/index
def home() :
    return render_template("index.html")

@app. route('/movie')
def movie() :
    i=1
    datalist = []#建造一个空列表，存放data数据
    con = sqlite3.connect("chinamovie.db")#获取连接对象
    cur = con.cursor()#获取游标
    sql = "select * from movie200 order by rate desc "
    data = cur.execute(sql)
    for item in data:
        item=item+(i,)
        datalist.append(item)
        i=i+1
    cur.close()
    con.close()
    return render_template("movie.html",movies = datalist)#把datalist数据传给movies变量，放到网页上


@app. route('/rates')
def rates():
    rate = []#建造一个空列表，存放评分数据
    num = []#每一个评分的统计出的数目
    con = sqlite3.connect("chinamovie.db")#获取连接对象
    cur = con.cursor()#获取游标
    sql = "select rate ,count(rate) from movie200 group by rate"#按评分筛选出每个评分有多少部影片
    data = cur.execute(sql)
    for item in data:
        rate.append(item[0])
        num.append(item[1])
    cur.close()
    con.close()
    return render_template("rates.html",rate=rate,num= num)

@app. route('/actors')
def actors() :
    return render_template("actors.html")

@app. route('/team')
def team() :
    return render_template("team.html")

if __name__ == '__main__' :
    app.run()

