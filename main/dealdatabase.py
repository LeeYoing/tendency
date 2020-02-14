# coding=utf-8 ##
import pymssql

host_ = "127.0.0.1"  # 连接服务器地址
user_ = "sa"  # 连接帐号
password_ = "li1995116"  # 连接密码
database_ = "msdb"  # 连接的数据库名字


#  用于保存数据到数据库
def save_data(ranktable):
        conn = pymssql.connect(host=host_, user=user_, password=password_, database=database_)  # 获取连接
        cursor = conn.cursor()  # 获取光标
        if not cursor:
            raise (NameError, "连接数据库失败")
        else:
            print("连接数据库成功")
            if len(ranktable) != 0:  # 判断传入的数据是否为空
                for i in range(len(ranktable)):  # 遍历整个数组
                    #print(ranktable[i])
                    ranktable[i] = tuple(ranktable[i])  # 将数组的每一行变成tuple，也就是数据库插入需要的格式
                    cursor.execute(
                        "INSERT INTO hotrank VALUES (%d, %s, %d, %s)", ranktable[i])
                conn.commit()  # 对数据库的变更变更操作要commit后才行
                print("保存成功！ 共保存", len(ranktable), "条数据")
                return


# 检索数据库
def search_data(string):
    conn = pymssql.connect(host=host_, user=user_, password=password_, database=database_)  # 获取连接
    cursor = conn.cursor()  # 获取光标
    temp_table = []
    if not cursor:
        raise (NameError, "连接数据库失败")
    else:
        print("连接数据库成功")
    cursor.execute(string)
    result = cursor.fetchall()
    for row in result:
        temp_table.append([row[0], row[1].encode('latin-1').decode('gbk'), row[2], row[3]])
    return temp_table

# 清空数据库
def clear_data():
    conn = pymssql.connect(host=host_, user=user_, password=password_, database=database_)  # 获取连接
    cursor = conn.cursor()  # 获取光标
    if not cursor:
        raise (NameError, "连接数据库失败")
    else:
        print("连接数据库成功")
    cursor.execute("delete from hotrank")
    conn.commit()
    print("清空数据成功！")
    cursor.close()

# 修改数据库
def change_data():
    conn = pymssql.connect(host=host_, user=user_, password=password_, database=database_)  # 获取连接
    cursor = conn.cursor()  # 获取光标
    if not cursor:
        raise (NameError, "连接数据库失败")
    else:
        print("连接数据库成功")
    cursor.execute("alter table hotrank alter column name varchar(50)")
    conn.commit()
    print("操作完成！")
    cursor.close()

# 操作数据库
def oper_data(str):
    conn = pymssql.connect(host=host_, user=user_, password=password_, database=database_)  # 获取连接
    cursor = conn.cursor()  # 获取光标
    if not cursor:
        raise (NameError, "连接数据库失败")
    else:
        print("连接数据库成功")
    cursor.execute(str)
    conn.commit()
    print("操作完成！")
    cursor.close()










#  nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#  cursor.execute("CREATE TABLE Hotrank(RANK INT,Name VARCHAR(25),Number INT)")  # 创建hotrank表，三列数据
#  cursor.execute("alter table hotrank add time varchar(10)")  #为hotrank表增加一列
#  cursor.execute("alter table hotrank alter column time varchar(20)") # 修改某一列属性
#  cursor.execute("delete from hotrank")
#  ranktable = [["111", 'John Smith', '3333', '20:50'],
#                  ["222", 'Jane Doe', '4444', '20:50'],
#                  ["333", 'Mike T.', '5555', '20:50']]