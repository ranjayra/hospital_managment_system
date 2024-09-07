from tkinter import*
from tkinter import ttk;
# from tkinter import Tk
import random
import time
import datetime
from tkinter import messagebox
import _mysql_connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1300x800+0+0")
        
        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.Numberoftablets=StringVar()
        self.Lot=StringVar()
        
        self.Issuedate=StringVar()
        self.Expdate=StringVar()
        self.Dailydose=StringVar()

        self.sideeffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.Drivingusingmachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsnumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfiBirth=StringVar()
        self.PatientAddress=StringVar()
        self.Dose=StringVar()
    
        lbltitle=Label(self.root,bd=10,relief=RIDGE,text="Hospital Management System",fg="red",bg="white",font=("time new roman ",30,"bold"))
        lbltitle.pack(side=TOP,fill=X) 
        
    #=====================================data frame=============#
        Dataframe=Frame(self.root,bd=15,padx=10,relief=RIDGE)
        Dataframe.place(x=0,y=85,width=1260,height=380)
        
        DataframeLeft=LabelFrame(Dataframe,bd=7,padx=15,relief=RIDGE,
                                                    font=("arial",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=7500,height=330)
        
        DataframeRight=LabelFrame(Dataframe,bd=7,padx=15,relief=RIDGE,
                                                    font=("arial",12,"bold"),text="Prescription")
        DataframeRight.place(x=770,y=5,width=460,height=330)
        
        #======================button frame=======================#
        
        Buttonframe=Frame(self.root,bd=7,padx=10,relief=RIDGE)
        Buttonframe.place(x=0,y=465,width=1260,height=55)
        
        #====================details frame====================================================#
        
        Detailsframe=Frame(self.root,bd=15,padx=10,relief=RIDGE)
        Detailsframe.place(x=0,y=517,width=1260,height=125)
        
        #=======================detail frame left=====================================================#
        lblNameTablet=Label(DataframeLeft,text="Name of Tablets",font=("time new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)
        conNametablet=ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,font=("time new roman",12,"bold"),
                                                                                 width=23)
        conNametablet["value"]=("Nice","Corona Vacacine","Acetaminophen","Adderall","Amlodipine","Ativan")
        conNametablet.grid(row=0,column=1)
        
        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Refence No",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        textref=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.ref,width=23)
        textref.grid(row=1,column=1)
        
        lblDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        textDose=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Dose,width=23)
        textDose.grid(row=2,column=1)
        
        lblNoOftablets=Label(DataframeLeft,font=("arial",12,"bold"),text="No Of Tablets:",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        textNoOftablets=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Numberoftablets,width=23)
        textNoOftablets.grid(row=3,column=1)
        
        lblLot=Label(DataframeLeft,font=("arial",12,"bold"),text="Lote:",padx=2,pady=4)
        lblLot.grid(row=4,column=0,sticky=W)
        textLot=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Lot,width=23)
        textLot.grid(row=4,column=1)
        
        lblissueDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        textissueDate=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Issuedate,width=23)
        textissueDate.grid(row=5,column=1)
        
        lblExpDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        textExpDate=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Expdate,width=23)
        textExpDate.grid(row=6,column=1)
        
        lblDailyDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        textDailyDose=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Dailydose,width=23)
        textDailyDose.grid(row=7,column=1)
        
        lblSideEfect=Label(DataframeLeft,font=("arial",12,"bold"),text="Side Efect:",padx=2,pady=4)
        lblSideEfect.grid(row=8,column=0,sticky=W)
        textSideEfect=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.sideeffect,width=23)
        textSideEfect.grid(row=8,column=1)
        
        lblFurtherInfo=Label(DataframeLeft,font=("arial",12,"bold"),text="Further Information:",padx=2,pady=6)
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        textFurtherInfo=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.FurtherInformation,width=23)
        textFurtherInfo.grid(row=0,column=3)
        
        lblBloodPressure=Label(DataframeLeft,font=("arial",12,"bold"),text="BloodPressure:",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        textBloodPressure=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Drivingusingmachine,width=23)
        textBloodPressure.grid(row=1,column=3)
        
        lblStorage=Label(DataframeLeft,font=("arial",12,"bold"),text="Storage:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        textStorage=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.StorageAdvice,width=23)
        textStorage.grid(row=2,column=3)
        
        lblMedicine=Label(DataframeLeft,font=("arial",12,"bold"),text="Medicine",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        textMedicine=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.HowToUseMedication,width=23)
        textMedicine.grid(row=3,column=3)
        
        lblPatientId=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Id:",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        textPatientId=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.PatientId,width=23)
        textPatientId.grid(row=4,column=3)
        
        lblNhsNumber=Label(DataframeLeft,font=("arial",12,"bold"),text="NHS Number:",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        textNhsNumber=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.nhsnumber,width=23)
        textNhsNumber.grid(row=5,column=3)
        
        lbltientname=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Name",padx=2,pady=6)
        lbltientname.grid(row=6,column=2,sticky=W)
        texttientname=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.PatientName,width=23)
        texttientname.grid(row=6,column=3)
        
        lblDateOfBirth=Label(DataframeLeft,font=("arial",12,"bold"),text="Date Of Birth:",padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        textDateOfBirth=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.DateOfiBirth,width=23)
        textDateOfBirth.grid(row=7,column=3)
        
        
        lblPatientAddress=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        textPatientAddress=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.PatientAddress,width=23)
        textPatientAddress.grid(row=8,column=3)
        
        #=============================Data frome right===============================================#
        self.txtPrescriptiopn=Text(DataframeRight,font=("arial",12,"bold"),width=45,height=15,padx=2,pady=6)
        self.txtPrescriptiopn.grid(row=0,column=0)
        #========================================Button=================================================
        btnPrescription=Button(Buttonframe,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=19)
        btnPrescription.grid(row=0,column=0)
        
        btnPrescriptionData=Button(Buttonframe,text="Prescription Data",bg="green",fg="white",font=("arial",12,"bold"),width=19)
        btnPrescriptionData.grid(row=0,column=1)
        
        btnUpdate=Button(Buttonframe,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=19)
        btnUpdate.grid(row=0,column=2)
        
        btnDelete=Button(Buttonframe,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=19)
        btnDelete.grid(row=0,column=3)
        
        btnClear=Button(Buttonframe,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=19)
        btnClear.grid(row=0,column=4)
        
        btnExit=Button(Buttonframe,text="Exite",bg="green",fg="white",font=("arial",12,"bold"),width=19)
        btnExit.grid(row=0,column=5)
        #======================================Table=============================================
        #=====================================scrollbar=========================================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,columns=("nameoftable","ref","dose","nooftablets","lot","issuedate",
                                                               "expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        
        self.hospital_table.heading("nameoftable",text="Name of Table")
        self.hospital_table.heading("ref",text="Reference No")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="ExpDate")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")
        
        
        self.hospital_table["show"]="headings"
        
        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)
    
        self.hospital_table.pack(fill=BOTH,expand=1)
        
        
     #==============================functionality description================================
        def iPrescriptionData(self):
          if self.Nameoftablets.get()==""or self.ref.get()=="":
              messagebox.showerror("error","all file are required")
          else:
              conn=_mysql_connector.connect(host="localhost",user="root",password="ranjay@123",database="project")
              my_cursor=conn.cursor()
              my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (
                                  self.Nameoftablets.get(),  
                                  self.ref.get(),  # Change this to match "Refrence_No"
                                  self.Dose.get(),  
                                  self.Numberoftablets.get(),  
                                  self.Lot.get(),  
                                  self.Issuedate.get(),  
                                  self.Expdate.get(),  
                                  self.Dailydose.get(),  
                                  self.StorageAdvice.get(),  # Change this to match "storage"
                                  self.nhsnumber.get(),
                                  self.PatientName.get(),
                                  self.DateOfBirth.get(),
                                  self.PatientAddress.get()
                            
                            
                                  ))
              conn.commit()
              conn.close()
              messagebox.showinfo("success","record has beeen inserted")
        
        
           
        
root=Tk()
ob=Hospital(root)
root.mainloop()      