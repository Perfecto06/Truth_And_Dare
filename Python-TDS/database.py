import pymysql

db=pymysql.connect(host="localhost", user="root", passwd="", database="pythontd")
cursor=db.cursor()
cursor.execute("DROP TABLE IF EXISTS players")
sql = """CREATE TABLE players (
         ID INT PRIMARY KEY AUTO_INCREMENT,
         Name  VARCHAR(20) NOT NULL,
         Score INT NOT NULL)"""
cursor.execute(sql)