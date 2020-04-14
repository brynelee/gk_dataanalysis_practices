import pymysql
conn = pymysql.connect(host='xdubuntu1810', port=3306, user='root',
                       passwd='time4@FUN', db='test', charset='utf8', connect_timeout=1000)
cursor = conn.cursor()
sql = '''create table if not exists class (id int(10) primary key auto_increment, name varchar(20) not null, text varchar(20) not null)'''
result = cursor.execute(sql)
print(result)
tables = cursor.execute('show tables')
print(tables)
