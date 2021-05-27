import os
import time
import random
os.system("cls")

#for new user
def register():
    os.system("cls")
    print("\n\n\n\n\n")
    print("\t\t\t welcome")
    print("\t\t\t----------")
    print()
    username=input("\t\t\tEnter user name: ")
    password=input("\t\t\tEnter password: ")
    file=open("register.txt","a")
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()
    print("\n\n")
    
#for old user
def login():
    os.system("cls")
    print("\n\n\n\n\n")
    print("\t\t\t Login")
    print("\t\t\t-------")
    print()
    username=input("\t\t\tUSERNAME: ")
    password=input("\t\t\tPASSWORD: ")
    print()
    with open ("register.txt","r") as fd:
        for line in fd:
            if username in line:
                if password in line:
                    print("  \t\t************Logged in*************")
                    return(1)
            else:
                print("\t\t\tIncorrect details!")
                return(-1)

#for viewing records
def view():
    os.system("cls")
    print("\t\t\tpatient list:")
    #file=open("Patient.txt","r")
    print("Id  NAME  AGE  ADDRESS  SEX  BLOOD GROUP  PHONE  EMAIL  HISTORY  DOCTOR NAME  \n")
    
    for i in open("Patient.txt","r").readlines():
        print(i)
    time.sleep(2)
    
#for searching records  
def search():
    os.system("cls")
    found = False
    try:
        file= open('patient.txt')
        line = file.readline()
        check = input('Enter patient number to search for ')
        while line != ' ':
            line = line.split(' ') #split into a list
            if check == line[0]:
                found = True
                name = line[1] 
                age = line[2]
                address = line[3]
                sex = line[4]
                blood_grp = line[5]
                phone_no= line[6]
                email_id = line[7]
                history=line[8]
                doctor_name=line[9]
                break
            line = file.readline() # read subsequent records
        file.close()
        if found:
            print("Name       :",name)
            print("Age        :",age)
            print("address    :",address)
            print("sex        :",sex)
            print("blood grp  :",blood_grp)
            print("phone      :",phone_no)
            print("email      :",email_id)
            print("History    :",history)
            print("Doctor name:",doctor_name)
        else:
            print('Employee is not listed')

    except FileNotFoundError:
        print("Error: File not found.")
        
#for deleting a record
def delete_fn():
    flag=0
    os.system("cls")
    with open('Patient.txt','r') as infile:
        with open('patient1.txt','w') as outfile:
           line=infile.readline()
           check=input("\t\t\tEnter patient number to delete: ")
           while(line!=""):
               line = line.split()
               if(check!=line[0]):
                   flag=1
                   pno=line[0]
                   name=line[1] 
                   age=line[2]
                   address=line[3]
                   sex=line[4]
                   blood_grp=line[5]
                   phone_no=line[6]
                   email_id=line[7]
                   history=line[8]
                   doctor_name=line[9]
                   
                   outfile.write(pno)
                   outfile.write(" ")
                   outfile.write(name)
                   outfile.write(" ")
                   outfile.write(age)
                   outfile.write(" ")
                   outfile.write(address)
                   outfile.write(" ")
                   outfile.write(address)
                   outfile.write(" ")
                   outfile.write(sex)
                   outfile.write(" ")
                   outfile.write(blood_grp)
                   outfile.write(" ")
                   outfile.write(phone_no)
                   outfile.write(" ")
                   outfile.write(email_id)
                   outfile.write(" ")
                   outfile.write(history)
                   outfile.write(" ")
                   outfile.write(doctor_name)
                   outfile.write("\n")
               line=infile.readline()  #read susequent records
           infile.close()
           outfile.close()
           os.remove("patient.txt")
           os.rename("patient1.txt","patient.txt")
           if(flag==1):
               print("\t\t\tRecord deleted successfully")
               print("\t\t\tUpdated file")
               print()
               print("Id  NAME  AGE  ADDRESS  SEX  BLOOD GROUP  PHONE  EMAIL  HISTORY  DOCTOR NAME  \n")
               for i in open("Patient.txt","r").readlines():
                   print(i)
               time.sleep(2)
                
           else:
               print("\t\t\tRecord not found")

#menu option for old patient
def old_patient():
    option='y'
    while(option=='y'):
        os.system("cls")
        print("\n\n\n\n\n")
        print("\t\t\t1.view details")
        print("\t\t\t2.delete details")
        print("\t\t\t3.Search patient")
        print("\t\t\t5.Exit")
        print()
        n=int(input("\t\t\tEnter option: "))
        if(n==1):
            view()
        elif(n==2):
            delete_fn()
        elif(n==3):
            search()
        elif(n==4):
            return(1)
        option=("Do you want to continue? ")
    else:
         exit
    time.sleep(2)

#to add new patient details
def new_patient():
    os.system("cls")
    file1=open("patient.txt","a")
    file1.seek(0,2)
    i_d=random.randrange(1,1000)
    new=str(i_d)
    print("\t\t\t*************Welcome*************")
    print()
    print("\t\t\tPatient id: ",new)
    print("\t\t\tEnter your details:")
    name=input("\t\t\tName: ")
    age=input("\t\t\tAge: ")
    address=input("\t\t\tAddress: ")
    sex=input("\t\t\tsex: ")
    blood_group=input("\t\t\tBlood group: ")
    phone_no=input("\t\t\tPhone no: ")
    email_id=input("\t\t\tEmail: ")
    history=input("\t\t\tHistory: ")
    doctor_name=input("\t\t\tDoctor name: ")
    file1.write(new)
    file1.write(" ")
    file1.write(name)
    file1.write(" ")
    file1.write(age)
    file1.write(" ")
    file1.write(address)
    file1.write(" ")
    file1.write(sex)
    file1.write(" ")
    file1.write(blood_group)
    file1.write(" ")
    file1.write(phone_no)
    file1.write(" ")
    file1.write(email_id)
    file1.write(" ")
    file1.write(history)
    file1.write(" ")
    file1.write(doctor_name)
    file1.write("\n")
    print()
    print("\t\t_______details saved______")
    time.sleep(2)
    file1.close()
    
def start():
    a=0
    os.system("cls")
    
    print("\t\t\t1.existing user")
    print("\t\t\t2.new user")
    print("\n")
    a=int(input("\t\t\tEnter option: "))
    if(a==1):
        s=login()
    elif(a==2):
        register()
        s=login()
    else:
        print("\t\t\tincorrect option")
    os.system("cls")   
    while(s==-1):
        print("\t\t\ttry again")
        start()
    cho='y'    
    while(cho=='y'):
        os.system("cls")
        print("\t\t\t1.old patient")
        print("\t\t\t2.new patient")
        print("\t\t\t3.exit")
        print()
        b=int(input("\t\t\tEnter option: "))
        if(b==1):
            a=old_patient()
        elif(b==2):
            new_patient()
        elif(b==3):
            exit
        else:
            print("\t\t\tWrong option")
        if(a==1):
            v=input("\t\t\tDO you want to exit?")
            if(v=='y'):
                exit()
            else:
                start()
        cho=input("Do u want to continue? ")       

start()

