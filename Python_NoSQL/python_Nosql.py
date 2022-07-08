from pymongo import MongoClient # khai báo thư viện pymongo
from pprint import pprint # sử dụng thư viện pprint


client=MongoClient() #tạo đối tượng client

db=client.test #kết nối đến database

student=db.student 

student_record={ # tạo record sinh viên
'Name':'Dang Quoc Bao',
'ID':'1654',
'Age':'22'}

result=student.insert_one(student_record) # insert record vào database

pprint(student.find_one({'Age':'22'})) # show ra một sinh viên có tuổi 22