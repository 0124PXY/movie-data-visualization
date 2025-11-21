import time
import random
import requests as requests
import xlwt   #进行excel操作
import sqlite3 #进行SQLlite数据库操作
import json
def getData():
    head={#模拟浏览器头部信息，向豆瓣服务器发送消息。
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53"
    }#用户代理，表示告诉豆瓣服务器，我们是什么类型的机器，浏览器（本质上告诉浏览器我们可以接收什么水平的文件内容）
    baseurl = "https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=&countries=%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86"
    datalist = []
    str_index = baseurl.find('&countries')
    j=0
    for i in range(0,10):#爬取十页
        time.sleep(random.randint(0,3))#爬一次随机间隔0~3秒,防止被封ip
        baseurl = baseurl[:str_index]+str(j)+baseurl[str_index:]#找到每一页的url规律
        res= requests.get(baseurl,headers=head)#获取请求信息
        data=res.text#解决中文乱码问题
        dic=json.loads(data)#把json数据转换为python数据
        dif=dic['data']#可以观察到需要的影片信息都在data字典里面
        for item in dif:
            datas=[]
            directors=item["directors"]
            if(len(directors)!=0):
                datas.append(directors[0]) #添加导演
            else:
                datas.append(" ")
            rate = item["rate"]#添加评分
            datas.append(rate)
            title = item["title"]
            datas.append(title)#添加影名
            url = item["url"]
            datas.append(url)#添加影片链接
            casts = item["casts"]
            if(len(casts)!=0):
                datas.append(casts[0]) #添加演员名单
            else:
                datas.append(" ")
            cover = item["cover"]
            datas.append(cover)#添加图片详情
            datalist.append(datas)
        baseurl = "https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=&countries=%E4%B8%AD%E5%9B%BD%E5%A4%A7%E9%99%86"
        j=j+20
    return datalist
def saveData(datalist,savapath):
    print("save...")
    book = xlwt.Workbook(encoding='utf-8',style_compression=0)#创建workbook对象
    sheet = book.add_sheet('豆瓣中国大陆电影TOP200',cell_overwrite_ok=True)  #创建工作表
    col = ("导演","评分","影片名","影片链接","演员","图片链接")
    for i in range(0,6):
        sheet.write(0,i,col[i])#列名
    for i in range(0,200):
        print("第%d条"%i)
        data = datalist[i]
        for j in range(0,6):
            sheet.write(i+1,j,data[j]) #数据
    book.save(savapath)     #保存数据表
def saveData2DB(datalist,dbpath):
    init_db(dbpath)#调用函数，创建数据库
    conn = sqlite3.connect(dbpath)#连接数据库
    cur = conn.cursor()#获取游标
    for data in datalist:#把datalist列表里面的数据取出来
        for index in range(len(data)):#找下标
            if index ==1:
                continue
            data[index]='"'+data[index]+'"'
        sql = '''
              insert into movie200(
                  directors, rate, title, url, casts, cover)
              values(?, ?, ?, ?, ?, ?) \
              '''#把data列表每一个中间用逗号连接起来
        cur.execute(sql, data)

        conn.commit()
    cur.close()
    conn.close()

def init_db(dbpath):
    sql = '''
    create table movie200
    (
    id integer primary key autoincrement,
    directors text,
    rate numeric,  
    title varchar,
    url text,
    casts text,
    cover text
    ) 
    '''#创建数据表
    conn = sqlite3.connect(dbpath)#连接数据库
    cursor = conn.cursor()#获取游标
    cursor.execute(sql)#执行sql语句
    conn.commit()#提交表单
    conn.close()#释放资源

def main():
    #1、获取数据
    datalist = getData()#获取数据列表
    savepath='.\\豆瓣中国大陆电影TOP200.xls'
    dbpath = 'chinamovie.db'
    #2、保存数据
    saveData(datalist,savepath)#将datalist里的数据保存到.\\豆瓣中国大陆电影TOP200.xls
    saveData2DB(datalist,dbpath)#将datalist里的数据保存到'chinamovie.db'数据库
if __name__ == "__main__":#当程序执行时
    #调用函数
    main()
    print("爬取完毕！")

