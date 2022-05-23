# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:28:51 2022

@author: Aakash
"""
from tkinter import *
from pymysql import *
def show():
    con=connect(host='localhost',user='root',password='Aakas#sky1',db='emp')
    cur=con.cursor()
    cur.execute("""insert into emp(emp_name,emp_id,emp_dept,emp_salary,bonus)
                values('{}',{},'{}',{},{});""".format(en.get(),ei.get(),ed.get(),
                es.get(),eb.get()))
    con.commit()
    con.close()
    print("Employee added to rooster. ")

def search():
    con=connect(host='localhost',user='root',password='Aakas#sky1',db='emp')
    cur=con.cursor()
    a=int(input("Enter the Emp Id to view their records"))
    b=(a)
    cur.execute("""select * from emp where emp_id==%s""",b)
    search_a=mycursor.fetchall()
    for i in search_a:
        print(i)
    con.commit()
    con.close()
    print("Data of Employee is being displayed ")

    
def delete():
    con=connect(host='localhost',user='root',password='Aakas#sky1',db='emp')
    cur=con.cursor()
    a=int(input("Enter the Emp Id to view their records"))
    b=(a)
    cur.execute("""delete * from emp where emp_id==%s;""",b)
    search_a=mycursor.fetchall()
    for i in search_a:
        print(i)
    con.commit()
    con.close()
    print("Employee deleted from the rooster. ")
a=Tk()
a.geometry('700x500')
a.title('Employee rooster')    

Label(a,text='Welcome').pack()
Label(a,text='Emp Name').place(x=20,y=50)
en=Entry(a)
en.place(x=100,y=50)

Label(a,text='Emp ID').place(x=320,y=50)
ei=Entry(a)
ei.place(x=420,y=50)

Label(a,text='Emp Dept').place(x=20,y=100)
ed=Entry(a)
ed.place(x=100,y=100)

Label(a,text='Emp Salary').place(x=320,y=100)
es=Entry(a)
es.place(x=420,y=100)


Label(a,text='Emp Bonus').place(x=20,y=150)
eb=Entry(a)
eb.place(x=100,y=150)


Button(a,text='ADD',command=show).place(x=180,y=360)
Button(a,text='Search by ID',command=search).place(x=280,y=360)
Button(a,text='Delete by ID',command=delete).place(x=380,y=360)

a.mainloop()