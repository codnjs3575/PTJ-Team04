# pip install mysql.connector

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root", 
    password = "kim990312",
    database = "mysql"
)

mycursor = mydb.cursor()

sql = "INSERT INTO nodam_myboard VALUES(%s,%s,%s,%s,%s,0)"
val = [(1,'codnjs3575','안녕하세요!!','처음 뵙겠습니다. 잘 부탁드려요 ㅎㅎ','2022-02-22 01:50:19.008438'),
       (2,'jiyun','금연 성공!!','오늘로 금연 시작한지 5년입니다. 그 동안 참기 힘들 때도 많았지만 돌아보니 정말 보람차네요!','2022-02-22 01:50:19.008438'),
       (3,'test11','','','2022-02-23 01:50:19.008438'),
       (4,'korea45','','','2022-02-24 01:50:19.008438'),
       (5,'codnjs3575','','','2022-02-24 01:50:19.008438'),
       (6,'nodamangel','','','2022-02-24 01:50:19.008438'),
       (7,'multi05','','','2022-02-24 01:50:19.008438'),
       (9,'cheeze','','','2022-02-24 01:50:19.008438'),
       (10,'codnjs3575','','','2022-02-25 01:50:19.008438'),
       (11,'test11','','','2022-02-25 01:50:19.008438'),
       (12,'multi05','','','2022-02-25 01:50:19.008438'),
       (13,'korea45','','','2022-02-25 01:50:19.008438'),
       ]


for i in range(len(val)):
    mycursor.execute(sql, val[i])

mydb.commit()

print(mycursor.rowcount, "record inserted")