import tkinter as tk
from tkinter import * 
import sqlite3, time, datetime, random 
name_of_db='fitzy.db'
my_conn = sqlite3.connect(name_of_db)
cdb = my_conn.cursor()


'''def create_table():
    cdb.execute('CREATE TABLE IF NOT EXISTS fitzysDb(idno INTEGER PRIMARY KEY,datestamp TEXT, firstname TEXT, surname TEXT, age INTEGER)')
'''

def show_all():
    print("Button clicked to show all records")
    form2 = tk.Tk()
    form2.geometry("800x800") 
    form2.title("Results from Database showing all records")
    data_set=my_conn.execute("SELECT * FROM fitzysDb")
    # btnFullName.grid(columnspan=2, padx=15, pady=15)
    output_data(data_set,form2)
    clear_form()

def clear_form():
    firstEntry.delete(0, END)
    secondEntry.delete(0, END)
    thirdEntry.delete(0, END)
    fourthEntry.delete(0, END)
    fifthEntry.delete(0, END)
    sixthEntry.delete(0, END)

def output_data(data_set,form2):
    i=0 # row value inside the loop 
    for person in data_set: 
        for j in range(len(person)):
            e = Entry(form2, width=15, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, person[j])
        i=i+1
    return form2
def queryFirstname():

    print("Button clicked to query firstname")
    f_name = firstEntry.get()
    print(f_name)
    form2 = tk.Tk()
    form2.geometry("800x800") 
    form2.title("Results from Database Query Where Firstname is " + f_name)
    data_set=my_conn.execute("SELECT * FROM fitzysDb WHERE firstname=?", (f_name,))
    output_data(data_set,form2)
    clear_form()
    

def querySurname():
    s_name = secondEntry.get()
    print("Button clicked to query surname - searched for surname: " + s_name)
    form2 = tk.Tk()
    form2.geometry("800x800") 
    form2.title("Results from Database Query Where Surname is " + s_name)
    
    data_set=my_conn.execute("SELECT * FROM fitzysDb WHERE surname=?", (s_name,)) 
    output_data(data_set,form2)
    clear_form()

def queryAge():
    age = thirdEntry.get()
    print("Button clicked to query age - searched for age: " + age)
    form2 = tk.Tk()
    form2.geometry("800x800") 
    form2.title("Results from Database Query Where Age is " + age)
    data_set=my_conn.execute("SELECT * FROM fitzysDb WHERE age=?", (age,))
    output_data(data_set,form2)
    clear_form()


def putRecord():
    with my_conn:
        currtime = time.time()
        date = datetime.datetime.fromtimestamp(currtime).strftime('%c')
        firstname = fourthEntry.get()
        surname = fifthEntry.get()
        age = sixthEntry.get()
        cdb.execute("INSERT INTO fitzysDb (datestamp, firstname, surname, age) VALUES (?, ?, ?, ?)",
                  (date, firstname, surname, age))
        my_conn.commit()
        print("Added to DB")

        print("The following has been added to the DB " + name_of_db +"\n")
        print("FirstName: " + firstname)
        print("Surname: " + surname)
        print("Age: " + age)
    clear_form()   
        
        
'''create_table()'''

form = tk.Tk()
form.geometry("500x600")

menu1 = tk.Label(form, text="Drug Registry", background="red", fg="white")
menu1.grid(row=3, column=1)

drugname_Label = tk.Label(form, text="Drug name")
drugname_Entry = tk.Entry(form, relief="raised")
drugname_Label.grid(row=5, column=0, padx=15, pady=15)
drugname_Entry.grid(row=5, column=1)


brandname_Label = tk.Label(form, text="Brand name")
brandname_Entry = tk.Entry(form, relief="raised")
brandname_Label.grid(row=7, column=0, padx=15, pady=15)
brandname_Entry.grid(row=7, column=1)

drugcategory_Label = tk.Label(form, text="Drug Category")
drugcategory_Entry = tk.Entry(form, relief="raised")
drugcategory_Label.grid(row=9, column=0, padx=15, pady=15)
drugcategory_Entry.grid(row=9, column=1)

manufacture_Label = tk.Label(form, text="Manufacture")
manufacture_Entry = tk.Entry(form, relief="raised")
manufacture_Label.grid(row=11, column=0, padx=15, pady=15)
manufacture_Entry.grid(row=11, column=1)

manufacture_Label = tk.Label(form, text="Manufacture ")
manufacture_Entry = tk.Entry(form, relief="raised")
manufacture_Label.grid(row=11, column=0, padx=15, pady=15)
manufacture_Entry.grid(row=11, column=1)







date=tk.date

fifthLabel = tk.Label(form, text="Enter surname to add:")
fifthEntry = tk.Entry(form, relief="raised")
fifthLabel.grid(row=18, column=0, padx=15, pady=15)
fifthEntry.grid(row=18, column=1)

sixthLabel = tk.Label(form, text="Enter age add:")
sixthEntry = tk.Entry(form, relief="raised")
sixthLabel.grid(row=20, column=0, padx=15, pady=15)
sixthEntry.grid(row=20, column=1)

btnFullName4 = tk.Button(form, text="Submit", command=putRecord)
btnFullName4.grid(columnspan=2)



form.mainloop() #run form by default
