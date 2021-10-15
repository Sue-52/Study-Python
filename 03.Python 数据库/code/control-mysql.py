# 导入 链接mysql的包
import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost",
                     user="root",
                     password="root",
                     database="pymysql",
                     autocommit=True)

# 使用 cursor() 方法床技安一个游标对象 cursor
cursor = db.cursor()

# 1. 测试数据库
# 使用 execute() 方法执行 SQL 语句
# cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据
# data = cursor.fetchone()

# print("数据库版本：%s" % data)

# 2. 创建数据库表
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# # 使用预处理语句创建表
# sql = """
#     CREATE TABLE EMPLOYEE (
#         FIRST_NAME CHAR(20) NOT NULL,
#         LAST_NAME CHAR(20),
#         AGE INT,
#         SEX CHAR(1),
#         INCOME FLOAT
#     )
# """
# cursor.execute(sql)

# 3. 插入数据
# sql = """
#     INSERT INTO EMPLOYEE(FIRST_NAME, \
#     LAST_NAME,AGE,SEX,INCOME) \
#     VALUES('Mac','Mohan',20,'Male',2000)
# """

# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#        LAST_NAME,AGE,SEX,INCOME) \
#        VALUES(%s,%s,%s,%s,%s)"

# 可以一次性添加多个数据
# result = cursor.executemany(sql, [('Dante', 'V', 20, 'M', 1999),
#                                   ('Vigel', 'D', 24, 'M', 1998)])

# 4. 查询数据
sql = "SELECT * FROM EMPLOYEE \
    WHERE INCOME > %s" % (1000)

try:
    # 执行 sql 语句
    cursor.execute(sql)
    # 提交到数据库并执行 --> 只在添加时使用
    # db.commit()

    # fetchall() 查找所有；fetchone() 该方法获取下一个查询结果集。
    results = cursor.fetchall()
    # print(results)
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print("fname={0},lname={1},age={2},sex={3},income={4}".format(
            fname, lname, age, sex, income))
except:
    # 如果发生错误则回滚
    # db.rollback()

    print("Error")

# 关闭数据库连接
db.close()
