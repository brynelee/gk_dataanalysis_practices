#encoding=utf-8
import jieba
 
seg_list = jieba.cut("伟大的北京天安门",cut_all=True)
print("Full Mode:", "/ ".join(seg_list)  )    #全模式
 
seg_list = jieba.cut("伟大的北京天安门",cut_all=False)
print("Default Mode:", "/ ".join(seg_list)  ) #精确模式
 
seg_list = jieba.cut("这里是伟大的北京天安门")    #默认是精确模式
print(", ".join(seg_list)  )
 
seg_list = jieba.cut_for_search("这里是伟大的北京天安门，伟大的中华人民共和国！") #搜索引擎模式
print(", ".join(seg_list) )

