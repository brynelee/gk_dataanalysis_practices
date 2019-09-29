'''
# WordCloud demo usage
wc = WordCloud(
    background_color='white',# 设置背景颜色
    mask=backgroud_Image,# 设置背景图片
    font_path='../SimHei.ttf',  # 设置字体，针对中文的情况需要设置中文字体，否则显示乱码
    max_words=100, # 设置最大的字数
    stopwords=STOPWORDS,# 设置停用词
	max_font_size=150,# 设置字体最大值
	width=2000,# 设置画布的宽度
	height=1200,# 设置画布的高度
    random_state=30# 设置多少种随机状态，即多少种颜色
)

'''

#-*- coding:utf-8 -*-
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
from PIL import Image
import numpy as np
# 生成词云
def create_word_cloud(f, stopWordsArray):
     print('根据词频计算词云')
     text = " ".join(jieba.cut(f,cut_all=False, HMM=True))
     wc = WordCloud(
           font_path="../SimHei.ttf",
           max_words=100,
           stopwords=stopWordsArray,
           width=2000,
           height=1200,
    )
     wordcloud = wc.generate(text)
     # 写词云图片
     wordcloud.to_file("./wordcloud.jpg")
     # 显示词云文件
     plt.imshow(wordcloud)
     plt.axis("off")
     plt.show()

f = '数据分析全景图及修炼指南\
学习数据挖掘的最佳学习路径是什么？\
Python 基础语法：开始你的 Python 之旅\
Python 科学计算：NumPy\
Python 科学计算：Pandas\
学习数据分析要掌握哪些基本概念？\
用户画像：标签化就是数据的抽象能力\
数据采集：如何自动化采集数据？\
数据采集：如何用八爪鱼采集微博上的“D&G”评论？\
Python 爬虫：如何自动化下载王祖贤海报？\
数据清洗：数据科学家 80% 时间都花费在了这里？\
数据集成：这些大号一共 20 亿粉丝？\
数据变换：大学成绩要求正态分布合理么？\
数据可视化：掌握数据领域的万金油技能\
一次学会 Python 数据可视化的 10 种技能'

stopWords = ["数据", "Python", "如何", "学习"]

create_word_cloud(f, stopWords)

