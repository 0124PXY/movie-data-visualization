# -*- codeing = utf-8 -*-
# @File ：testwordcloud.py
# @Software ：IntelliJ IDEA
import jieba  #分词，一个句子分成很多词
from matplotlib import  pyplot as plt#绘图，数据可视化
from wordcloud import WordCloud      #词云
from PIL import Image                #图片处理
import numpy as np
import sqlite3
text = ""#空的文本
con = sqlite3.connect("chinamovie.db")#获取连接对象
cur = con.cursor()#获取游标
sql = "select casts from movie200"#找出演员名单
data = cur.execute(sql)
for item in data:
    text = item[0]+text
#print (item[0])
cur.close()
con.close()

cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))

img = Image.open(r'.\static\assets\img\tree.jpg')#打开图片，r作用是解决转义字符问题
img_array = np.array(img)#把图片转换为数组
WC = WordCloud(
    background_color="white",#背景色为白色
    mask = img_array,#遮罩的图片数组
    font_path="msyh.ttc"#字体所在位置C:\Windows\fonts
)
WC.generate_from_text(string)

#绘制图片
fig = plt.figure(1)#1是找第一个位置
plt.imshow(WC)#按照wc词云规则显示
plt.axis('off')#不显示坐标轴
# plt.show()#显示生成的词云图片
plt.savefig(r'.\static\assets\img\WCtree.jpg',dpi=1080)