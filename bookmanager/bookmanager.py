import sqlite3

from tkinter import Tk, Text, BOTH, W, N, E, S, Listbox, StringVar,END
from tkinter.ttk import Frame, Button, Label, Style, Entry

#UI 클래
class BookManagerUi(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

        self.db = dao('blist') #데이터베이스 관리 클래스 생성


    def initUI(self):

        self.parent.title("Book Manager")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        self.rowconfigure(5, pad=3)
        self.rowconfigure(6, pad=3)


        self.input_bname=''
        self.input_aname=''
        self.input_price=0
        self.delete=''

        lb_bookname = Label(self, text="bookname:")
        lb_bookname.grid(row=0, column =0 ,sticky=W, pady=4, padx=5)

        self.entry_bookname = Entry(self)
        self.entry_bookname.grid(row=0, column = 1 )

        lb_author = Label(self, text="author:")
        lb_author.grid(row=0, column =2,sticky=W, pady=4, padx=5)

        self.entry_author = Entry(self)
        self.entry_author.grid(row=0, column = 3 )


        lb_price = Label(self, text="price:")
        lb_price.grid(row=0, column =4 ,sticky=W, pady=4, padx=5)

        self.entry_price = Entry(self)
        self.entry_price.grid(row=0, column = 5 ,padx=15)


        abtn = Button(self, text="Add", command=lambda:self.clicked_add())
        abtn.grid(row=0, column=6)

        sbtn = Button(self, text="Serach", command = lambda:self.clicked_search())
        sbtn.grid(row=1, column=6, pady=4)

        dbtn = Button(self, text="Delete", command = lambda:self.clicked_delete())
        dbtn.grid(row=2, column=6, pady=4)

        self.lb = Listbox(self)

        self.lb.grid(row=3,column = 0, columnspan = 6,rowspan= 4, sticky = E+W+S+N)
        self.lb.bind("<<ListboxSelect>>", self.onSelect)


    #삭제를 위한 select부분
    def onSelect(self,val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)

        self.delete = value

    # 데이터 추가 버튼
    def clicked_add(self):
        bname =self.entry_bookname.get()
        aname = self.entry_author.get()
        price = self.entry_price.get()

        self.lb.delete(0,END)


        # 입력받을 데이터가 모자란지 검사
        if(len(bname) >0 and len(aname)>0 and len(price)>0 ):
            #가격에 문자를 입력했을 경우 처리
            try:
                priceI = eval(price)
            except:
                self.lb.insert(END,"you input wrong price. it must be integer")

            #사용자가 입력한 내용중 중복된 책이름이 있을 경우(저자는 책이 여러가지일 수 있으니 제외)
            rec = self.db.excute_select(bname,'')
            if ( len(rec) >0):
                self.lb.insert(END,bname +" is already in the database")
            else:
                self.db.insert_data(bname,aname,priceI) # 모든 조건 만족시 데이터 입력 수행
                r =self.db.excute_select(bname,aname)
                for rs in r:
                    self.lb.insert(END,str(rs))


        else:
            s = StringVar()
            self.entry_price.config(textvariable = s)
            self.lb.insert(END,"you have to input more values")


    #검색버튼
    def clicked_search(self):
        bname =self.entry_bookname.get()
        aname = self.entry_author.get()

        self.lb.delete(0,END)

        #책이름 또는 저자이름 둘중 하나만입력 되어도 검색 가능하도록
        if(len(bname)>0 or len(aname)>0 ):
            rec = self.db.excute_select(bname,aname)

            for r in rec:
                self.lb.insert(END,str(r))
        else:
            self.lb.insert(END,"you have to input more values(bookname or author")

    #삭제 버튼
    def clicked_delete(self):
        self.lb.delete(0,END)
        q = self.db.excute_delete(self.delete)
        self.lb.insert(END,q+' is delete from database')



def main():
    root = Tk()
    root.geometry("800x300+300+300")
    app = BookManagerUi(root)
    root.mainloop()

#데이터베이스 접속 객체
class dao:
    def __init__(self,db_file):
        #데이터베이스 및 테이블 생성
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS booklist(bname VARCHAR(20),
                            aname VARCHAR(20), price INT(5))''')
        self.conn.commit()

        self.delete_s=''

    # 데이터 입력 부분
    def insert_data(self,bname,aname,price):
        query = "INSERT INTO booklist VALUES('{0}','{1}',{2})".format(bname,aname,price)
        self.cursor.execute(query)
        self.conn.commit()

    #데이터 조회 부분
    def excute_select(self,bname,aname):
        query = "SELECT * FROM booklist WHERE bname='{0}' OR aname='{1}'".format(bname,aname)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    #데이터 삭제 부분 책이름이 중복되지 않으므로 삭제가 가능하다.
    def excute_delete(self,d):
        self.delete_s = d.split(',')
        self.delete_s = self.delete_s[0]

        self.delete_s = self.delete_s[2:-1]

        query = "DELETE FROM booklist WHERE bname='{0}'".format(self.delete_s)

        self.cursor.execute(query)
        self.conn.commit()
        return self.delete_s


if __name__ == '__main__':
    main()