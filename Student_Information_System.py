from tkinter import*
from tkinter import ttk
import tkinter.ttk as ttk
import tkinter.messagebox
import os
import csv

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Information System")
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#6C1118")
        self.root.resizable(False,False)
        self.data=dict()
        self.temp=dict()
        self.filename="Student_infos.csv"

        Student_ID_number= StringVar()
        First_name = StringVar()
        Middle_name = StringVar()
        Sur_name = StringVar()
        Year_level = StringVar()
        Gender = StringVar()
        Course = StringVar()
        Searchbar=StringVar()
        

        title=Label(self.root, text = "STUDENT INFORMATION SYSTEM",bd=4,relief=RIDGE, font=("Times New Roman",40,"bold"),bg="#FFB7B8", fg="maroon")
        title.pack(side=TOP, fill=X)
        
        if not os.path.exists(self.filename):
            with open('Student_infos.csv',mode = 'w') as csv_file:
                fieldnames = ["Student_ID_number", "First_name", "Middle_name", "Sur_name", "Course", "Year_level", "Gender"]
                writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
                writer.writeheader()
        else:
            with open('Student_infos.csv', newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    self.data[row["Student_ID_number"]] = {'First_name': row["First_name"], 'Middle_name': row["Middle_name"], 'Sur_name': row["Sur_name"], 'Course': row["Course"],'Year_level': row["Year_level"], 'Gender': row["Gender"]}
            self.temp = self.data.copy()
            

        #======Functions========

        def iExit():
            iExit = tkinter.messagebox.askyesno("Student Information System","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
            
        
        def addData():
            with open('Student_infos.csv', "a", newline="") as file:
                csvfile = csv.writer(file)
                if Student_ID_number.get()=="" or First_name.get()=="" or Sur_name.get()=="" or Year_level.get()=="":
                    tkinter.messagebox.showinfo("Student Information System","Please fill in the box.")
                else:
                    ID = Student_ID_number.get()
                    ID_list = []
                    for i in ID:
                        ID_list.append(i)
                    if "-" in ID_list:
                        x = ID.split("-")
                        y = x[0]
                        n = x[1]
                        if y.isdigit()==False or n.isdigit()==False:
                            try:
                                tkinter.messagebox.showerror("Student Information System", "ID Number is INVALID")
                            except:
                                pass
                        elif y==" " or n==" ":
                            try:
                                tkinter.messagebox.showerror("Student Information System", "ID Number is INVALID")
                            except:
                                pass
                        else:
                            if ID in self.data:
                                tkinter.messagebox.showinfo("Student Information System","Student ID is already RECORDED")
                            else:
                                self.data[Student_ID_number.get()] = {'First_name': First_name.get(), 'Middle_name': Middle_name.get(), 'Sur_name': Sur_name.get(), 'Course': Course.get(),'Year_level': Year_level.get(), 'Gender': Gender.get()}
                                self.saveData()
                                tkinter.messagebox.showinfo("Student Information System", "Student Information is Recorded Successfully")
                                Clear()
                    else:
                        tkinter.messagebox.showerror("Student Information System", "ID Number is INVALID")      
                displayData()

    
        def Clear():
            Student_ID_number.set("")
            First_name.set("")
            Middle_name.set("")
            Sur_name.set("")
            Year_level.set("")
            Gender.set("")
            Course.set("")

        def displayData():
            tree.delete(*tree.get_children())
            with open('Student_infos.csv') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    Student_ID_number=row['Student_ID_number']
                    First_name=row['First_name']
                    Middle_name=row['Middle_name']
                    Sur_name=row['Sur_name']
                    Year_level=row['Year_level']
                    Course=row['Course']
                    Gender=row['Gender']
                    tree.insert("",0, values=(Student_ID_number, First_name, Middle_name, Sur_name,Course, Year_level, Gender))
                    
        def search():
            if self.Search.get() in self.data:
                vals = list(self.data[self.Search.get()].values())
                tree.delete(*tree.get_children())
                tree.insert("",0, values=(self.Search.get(), vals[0],vals[1],vals[2],vals[3],vals[4],vals[5]))
            elif self.Search.get() == "":
                displayData()
            else:
                tkinter.messagebox.showerror("Student Information System","Student not found")
                return

        def delete():
            if tree.focus()=="":
                tkinter.messagebox.showerror("Student Information System","Please select a student record from the table")
                return
            id_no = tree.item(tree.focus(),"values")[0]
            
            self.data.pop(id_no, None)
            self.saveData()
            tree.delete(tree.focus())
            tkinter.messagebox.showinfo("Student Information System","Student Record Deleted Successfully")
            displayData()

        def editData():
            if tree.focus() == "":
                tkinter.messagebox.showerror("Student Information System", "Please select a student record from the table")
                return
            values = tree.item(tree.focus(), "values")
            Student_ID_number.set(values[0])
            First_name.set(values[1])
            Middle_name.set(values[2])
            Sur_name.set(values[3])
            Course.set(values[4])
            Year_level.set(values[5])
            Gender.set(values[6])
       
       
        def updateData():
            with open('Student_infos.csv', "a", newline="") as file:
                csvfile = csv.writer(file)
                if Student_ID_number.get()=="" or First_name.get()=="" or Sur_name.get()=="" or Course.get()=="" or Year_level.get()=="":
                    tkinter.messagebox.showinfo("Student Information System","Please select a student record from the table")
                else:
                    self.data[Student_ID_number.get()] = {'First_name': First_name.get(), 'Middle_name': Middle_name.get(), 'Sur_name': Sur_name.get(), 'Course': Course.get(),'Year_level': Year_level.get(), 'Gender': Gender.get()}
                    self.saveData()
                    tkinter.messagebox.showinfo("Student Information System", "Successfully Updated")
                Clear()
                displayData()     
        
            
        
        #------------- FRAMES -------------#
        
        
        ManageFrame=Frame(self.root, bd=4, relief =RIDGE, bg="#ecc19c")
        ManageFrame.place(x=880, y=100,width=450, height=560)
        
        DetailFrame=Frame(self.root, bd=4, relief =RIDGE, bg="#ecc19c")
        DetailFrame.place(x=20, y=100,width=830, height=560)

        ButtonFrame=Frame(ManageFrame, bd=4, relief=RIDGE, bg="#ecc19c")
        ButtonFrame.place(x=10,y=410, width=420, height=130)


        #------------- LABELS AND ENTRY WIDGETS -------------#
        

        title=Label(ManageFrame, text="STUDENT INFORMATION",bg="#FFB7B8", fg="maroon", font=("Times New Roman",20,"bold"))
        title.grid(row=0, columnspan=2, pady=20)
        
        self.lblStdID = Label(ManageFrame, font=("Times New Roman",15,"bold"),text="ID Number:", padx=2, pady=2, bg="#FFB7B8", fg="maroon")
        self.lblStdID.grid(row=1, column=0,padx=5,pady=5, sticky="w")
        self.txtStdID = Entry(ManageFrame, font=("Times New Roman",13,"normal"),textvariable=Student_ID_number, relief=GROOVE, width=31)
        self.txtStdID.grid(row=1, column=1)
        self.txtStdID.insert(0, "YYYY-NNNN")
        self.txtStdID.grid(row=1, column=1)

        self.lblFirstname = Label(ManageFrame,font=("Times New Roman",15,"bold"),text="First Name:", padx=2, pady=2, bg="#FFB7B8", fg="maroon")
        self.lblFirstname.grid(row=2, column=0,padx=5,pady=5, sticky="w")
        self.txtFirstname = Entry(ManageFrame, font=("Times New Roman",13,"normal"),textvariable=First_name, relief=GROOVE,width=31)
        self.txtFirstname.grid(row=2, column=1)
        
        self.lblMidname = Label(ManageFrame, font=("Times New Roman",15,"bold"),text="Middle Initial:", padx=2, pady=2, bg="#FFB7B8", fg="maroon")
        self.lblMidname.grid(row=3, column=0,padx=5,pady=5, sticky="w")
        self.txtMidname = Entry(ManageFrame, font=("Times New Roman",13,"normal"),textvariable=Middle_name, relief=GROOVE,width=31)
        self.txtMidname.grid(row=3, column=1)

        self.lblSurname = Label(ManageFrame, font=("Times New Roman",15,"bold"),text="Surname:", padx=2, pady=2, bg="#FFB7B8", fg="maroon")
        self.lblSurname.grid(row=4, column=0,padx=5,pady=5, sticky="w")
        self.txtSurname = Entry(ManageFrame, font=("Times New Roman",13,"normal"),textvariable=Sur_name, relief=GROOVE,width=31)
        self.txtSurname.grid(row=4, column=1)

        self.lblYearlevel = Label(ManageFrame, font=("Times New Roman",15,"bold"),text="Year Level:", padx=2, pady=2, bg="#FFB7B8", fg="maroon")
        self.lblYearlevel.grid(row=5, column=0,padx=5,pady=5, sticky="w")
        self.comboYearlevel=ttk.Combobox(ManageFrame,font=("Times New Roman",13,"normal"), state="readonly",width=29, textvariable=Year_level)
        self.comboYearlevel['values']=("First Year","Second Year", "Third Year", "Fourth Year")
        self.comboYearlevel.grid(row=5,column=1)

        self.lblGender = Label(ManageFrame, font=("Times New Roman",15,"bold"),text="Gender:", padx=2, pady=2, bg="#FFB7B8", fg="maroon")
        self.lblGender.grid(row=6, column=0,padx=5,pady=5, sticky="w")
        self.comboGender=ttk.Combobox(ManageFrame,font=("Times New Roman",13,"normal"), state="readonly",width=29, textvariable=Gender)
        self.comboGender['values']=("Male", "Female")
        self.comboGender.grid(row=6,column=1)

        self.lblCourse = Label(ManageFrame, font=("Times New Roman",15,"bold"),text="Course:", padx=2, pady=2, bg="#FFB7B8", fg="maroon")
        self.lblCourse.grid(row=7, column=0,padx=5,pady=5, sticky="w")
        self.txtCourse = Entry(ManageFrame, font=("Times New Roman",13,"normal"),textvariable=Course, relief=GROOVE,width=31)
        self.txtCourse.grid(row=7, column=1)

        #-------------Button Widget---------

        self.btnAddData = Button(ButtonFrame, text="Add", font=("Times New Roman",10,"bold"),bg="#6C1118", fg="white", height=1, width=12, bd=4,command=addData)
        self.btnAddData.grid(row=0, column=0, padx=15, pady=15)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=("Times New Roman",10,"bold"),bg="#6C1118", fg="white", height=1, width=12, bd=4, command=updateData)
        self.btnUpdateData.grid(row=0, column=2, padx=15, pady=15)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=("Times New Roman",10,"bold"),bg="#6C1118", fg="white", height=1, width=12, bd=4,command=Clear)
        self.btnClearData.grid(row=1, column=0,padx=15, pady=15)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=("Times New Roman",10,"bold"),bg="#6C1118", fg="white", height=1, width=12, bd=4, command=delete)
        self.btnDeleteData.grid(row=1, column=1,padx=15, pady=15)

        self.btnExit = Button(ButtonFrame, text="Exit", font=("Times New Roman",10,"bold"),bg="#6C1118", fg="white", height=1, width=12, bd=4, command=iExit)
        self.btnExit.grid(row=1, column=2,padx=15, pady=15)


        #-------------Detail Frame ---------
        self.lblSearch = Label(DetailFrame, font=('Times New Roman',10,'bold'),text="Search by ID Number", padx=2, pady=2, bg="#FFB7B8", fg="maroon")
        self.lblSearch.grid(row=1, column=0,padx=5,pady=5, sticky="w")
        self.Search = Entry(DetailFrame, font=('Times New Roman',10,'normal'),textvariable=Searchbar, relief=GROOVE,width=25)
        self.Search.grid(row=1, column=1)

        self.btnSearch = Button(DetailFrame, text="Search",font=("Times New Roman",10,"bold"),bg="#6C1118", fg="white", height=1, width=12, bd=4, command=search)
        self.btnSearch.grid(row=1, column=2,padx=15, pady=15)
        
        self.btnDisplayData = Button(DetailFrame, text="Select", font=("Times New Roman",10,"bold"),bg="#6C1118", fg="white", height=1, width=12, bd=4,command=editData)
        self.btnDisplayData.grid(row=1, column=3, padx=15, pady=15)
        
        TableFrame=Frame(DetailFrame, bd=4,relief=RIDGE,bg='#FFB7B8')
        TableFrame.place(x=10,y=80, width=790, height=450)


        #-------------Treeview ---------

        scroll_y=Scrollbar(TableFrame, orient=VERTICAL)

        tree = ttk.Treeview(TableFrame, height=10, columns=("Student_ID_number","First_name","Middle_name","Sur_name","Course","Year_level","Gender"), yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT, fill=Y)

        tree.heading("Student_ID_number", text="Student ID")
        tree.heading("First_name", text="First Name")
        tree.heading("Middle_name", text="Middle Name")
        tree.heading("Sur_name", text="Surname")
        tree.heading("Course", text="Course")
        tree.heading("Year_level", text="Year Level")
        tree.heading("Gender", text="Gender")
        tree['show'] = 'headings'

        tree.column("Student_ID_number", width=70)
        tree.column("First_name", width=100)
        tree.column("Middle_name", width=70)
        tree.column("Sur_name", width=100)
        tree.column("Course", width=120)
        tree.column("Year_level", width=70)
        tree.column("Gender", width=70)
        tree.pack(fill=BOTH,expand=1)

        displayData()

    def saveData(self):
        temps = []
        with open('Student_infos.csv', "w", newline ='') as update:
            fieldnames = ["Student_ID_number","First_name","Middle_name","Sur_name","Course","Year_level","Gender"]
            writer = csv.DictWriter(update, fieldnames=fieldnames, lineterminator='\n')
            writer.writeheader()
            for id, val in self.data.items():
                temp ={"Student_ID_number": id}
                for key, value in val.items():
                    temp[key] = value
                temps.append(temp)
            writer.writerows(temps)

        
        


if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
