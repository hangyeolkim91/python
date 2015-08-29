import datetime
import sqlite3

conn = sqlite3.connect("data.db")

cursor = conn.cursor()

#데이터와 데이터 베이스는 미리 만들어져 있음

# query = '''CREATE TABLE datedata (
#     date DATE,
#     int1 INT(4),
#     TEMP INT(4),
#     HUMI INT(4),
#     ASTO INT(4))'''
#
# cursor.execute(query)
# #cursor.execute('DROP TABLE IF EXISTS datedata')
# conn.commit()

class dao:
    def __init__(self,db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def insert_data(self,data_list):
        for d in data_list:
            query="INSERT INTO datedata VALUES('{date}',{int1},{TEMP},{HUMI},{ASTO});".format_map(d)
            self.cursor.execute(query)


        self.conn.commit()

    def excute_select(self,qr):
        self.cursor.execute(qr)
        for rec in self.cursor.fetchall():
            print(rec)


        self.conn.commit()

#파일에서 데이터를 불러오는 객체
class parser:
    def __init__(self):
        self.dlist = []  # 파일에서 가져온 데이터 dic타입으로 저장됨

    def parsing(self,filen):
        with open(filen) as f:
            data = f.readlines()

        for d in data:
            #데이터를 dictionary형태로 가공
            dsp = d
            dsp = dsp[:-1]
            dsp = dsp.split(',')
            dt = datetime.datetime.strptime(dsp[0],"%Y%m%d%H%M%S")
            dts = datetime.datetime.strftime(dt,'%Y-%m-%d:%H%M%S')


            self.dlist.append({'date':dts,'int1':dsp[1],'TEMP':dsp[2],'HUMI':dsp[3],'ASTO':dsp[4]})


    def get_data(self):
        return self.dlist


db = dao('data.db')

ps = parser()
ps.parsing('DATA')

db.insert_data(ps.get_data())
db.excute_select("SELECT * FROM datedata")