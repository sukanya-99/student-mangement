import sys
import os
import io
def main():
    
     print(""" 

      ------------------------------------------------------
     |======================================================| 
     |======== Welcome To Student Management System ========|
     |======================================================|
      ------------------------------------------------------

    Enter 1 : Login as admin
    Enter 2 : login as user 
            """)
     ch=input("Enter your choice")
     if ch == "1":
         passw=input("enter the admin password : ")#admin password=admin
         if(passw=="administrator"):
             print("Access granted","\n","welcome")
             menu()
     elif ch == "2":
         login()
        
    
    
def login():
    flag=0
    print("Enter username : ")
    answer1=input()
    print("Enter password : ")
    answer2=input()
    f3=open("project.txt","r+")
    for line in f3: 
        value=line.split() 
        if(answer1==value[8] and answer2==value[9]):
            flag=1
            print("user id and password is correct")
            flag1=0
            while(flag1==0):
                
                print("************USER MAIN MENU**************")
                ch1 = input("""
                          1: View student profile
                          2: Update Student details

                          Please enter your choice: """)
                if ch1 == "1":
                    print(" regno=",value[0],"\n","stud_name=",value[1],"\n","Date of Birth=",value[2],"\n","gender=",value[3],"\n",
                      "cast=",value[4],"\n","session_start=",value[5],"\n","session_end=",value[6],"\n","address=",value[7],"\n",
                      "User_id=",value[8],"\n","Password=",value[9],"\n")
                    f3.close()
                if ch1 == "2":
                    f4=open("project.txt","r+")
                    f5=open("project_temp.txt","w+")
                    for line in f4:
                         value1=line.split() 
                         if(answer1!=value1[8]):
                              z = "  "
                              f5.write(z.join(value1))
                              f5.write('\n')
                         else:
                              print('''1 for updating registration number
2 for updating Student Name
3 for updating Date of Birth
4 for updating Gender
5 for updating Cast
6 for updating Session_start
7 for updating Session_end
8 for updating Address
9 for updating Password''')
                              ch2=input("Enter your choice")
                              if ch2 == "1":
                                   reg_new=input('Enter the new registration number of student: ')
                                   value1[0]=reg_new
                              if ch2 == "2":
                                   name_new=input('Enter the new name of student: ')
                                   value1[1]=name_new
                              if ch2 == "3":
                                   dob_new=input('Enter new date of birth in format(dd/mm/yy): ')
                                   value1[2]=dob_new
                              if ch2 == "4":
                                   gen_new=input('Enter the new gender(f/m): ')
                                   value1[3]=gen_new
                              if ch2 == "5":
                                   cast_new=input('Enter the new cast(g/sc/st): ')
                                   value1[4]=cast_new
                              if ch2 == "6":
                                   ss_new=input("enter the new starting year")
                                   value1[5]=ss_new
                              if ch2 == "7":
                                   se_new=input("enter the ending year")
                                   value1[6]=se_new
                              if ch2 == "8":
                                   up=input("Enter new address : ")
                                   value1[7]=up
                              if ch2 == "9":
                                   psw_new=input("Enter new password : ")
                                   value1[9]=psw_new
                              y = "  "
                              f5.write(y.join(value1))
                              f5.write('\n')
                    #f3.close()
                    f4.close()
                    f5.close()
                    os.remove("project.txt")
                    os.rename("project_temp.txt","project.txt")
                    main()
                print("Do you want to continue(y for yes/n for no)")
                b=input()
                if(b=="y"):
                    flag1=0
                else:
                    flag1=1
                    main()
            
            
    if(flag==0):
        print("Wrong userid or password")
        login()
            
    
    
             

def menu():
    print("************ADMIN MAIN MENU**************")
    

    choice = input("""
                      1: Enter Student details
                      2: View all Student details
                      3: Quit/Log Out

                      Please enter your choice: """)

    if choice == "1":
        enterstudentdetails()
    elif choice=="2":
        viewallstudentdetails()
    elif choice=="3":
        main()
    else:
        print("You must only select either 1,2 or 3.")
        print("Please try again")
        menu()


def enterstudentdetails():
    f=open("project.txt","a")
    n=0
    while(n==0):
        regno = input('Enter the registration number of student: ')
        f.write(regno+"\t")
        
        stud_name = input('Enter the name of student: ')
        f.write(stud_name+"\t")

        dob = input('Enter date of birth in format(dd/mm/yy): ')
        f.write(dob+"\t")

        gender= input('Enter the gender(f/m): ')
        f.write(gender+"\t")
                      
        cast = input('Enter the cast(g/sc/st): ')
        f.write(cast+"\t")
                      
        sess_start = input("enter the starting year")
        f.write(sess_start+"\t")
        
        sess_end = input("enter the ending year")
        f.write(sess_end+"\t")

        addr=input('Enter address: ')
        f.write(addr+"\t")

        user_id=input('Enter userid: ')
        f.write(user_id+"\t")

        paswd=input('Enter password: ')
        f.write(paswd+"\t")
                      
        f.write("\n")
        
        print("1 Record has been successfully written to file")
        print("Do you want to enter another student details(y for yes/n for no)")
        a=input()
        if(a=="y"):
            n=0
        else:
            n=1
    f.close()

    menu()

def viewallstudentdetails():
    f2=open("project.txt","r")
    print("regno studname      DateOfBirth   gender cast sessstart   sessend   address                    Userid   Password")
    print("----------------------------------------------------------------------------------------------------------------------")
    for line in f2: 
        val=line.split()
        print('%-6s %-12s %-12s %-7s %-5s %-10s %-8s %-25s %-8s %-9s' % (val[0],val[1],val[2],val[3],val[4],val[5],val[6],val[7],val[8],val[9]))
    f2.close() 
    menu()
main()






