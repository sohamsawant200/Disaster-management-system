#DATABASE=CITIZENS
from tabulate import *
import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",
                                  passwd="kimaya",port='3306')
mycur=mycon.cursor()
mycur.execute("create database if not exists CITIZENS;")
mycur.execute("use citizens")


print("*"*188)
print("*")
print("*\t\t\t\t\t\t\t\t\t\tDISASTER MANAGEMENT SYSTEM")
print("*")
print("*"*188)


def script():
    
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",
                                      passwd="kimaya",port='3306',
                                  database='citizens')
    mycur=mycon.cursor()
    mycur.execute("create database if not exists CITIZENS;")
    mycur.execute("use citizens")

    
    import disaster_module
    print("\n\t\t\t\t\t\t\t\tARE YOU A 1.GOVERNMENT OFFICER OR  2. CITIZEN? (*enter 1 or 2 as required*)\n")
    PERSON=input()
    if PERSON=="2":
        print("~~~MAIN MENU~~~ \n1.REGISTER \n2. UPDATE MY DETAILS \n3.DISASTER ASSISTANCE \n4.REALTIME WEATHER \n5.DETAILS OF OFFICIALS IN CASE OF EMERGENCY \n6.CHECK MY DETAILS \n7.EXIT\n**enter task number and press enter**")
        choice=input()

        if choice=="1":#REGISTER
            x=disaster_module.register()
            print("\nNEED TO REGISTER NEW CITIZEN?(y/n)")
            inp=input("")
            if inp=="Y" or inp=="y":
                x=disaster_module.register()
                print("\nNEED TO REGISTER NEW CITIZEN?(y/n)")
                inp=input("")
                if inp=="Y" or inp=="y":
                    x=disaster_module.register()
                    print("\nNEED TO REGISTER NEW CITIZEN?(y/n)")
                    inp=input("")
                    if inp=="Y" or inp=="y":
                        x=disaster_module.register()
                    else:
                        print("Task terminating. ThankYou!")
                else:
                    print("Task terminating. ThankYou!!")
            else:
                print("Task terminating. ThankYou!")
                

        elif choice=='2':#UPDATE
            x=disaster_module.updatefn()
            print("\nNEED TO UPDATE MORE?(y/n)")
            inp=input("")
            if inp=="YES" or inp=="yes":
                x=disaster_module.updatefn()
                print("\nNEED TO UPDATE MORE?(y/n)")
                inp=input("")
                if inp=="YES"  or inp=="yes":
                    x=disaster_module.updatefn()
                    print("\nNEED TO UPDATE MORE?(y/n)")
                    inp=input("")
                    if inp=="YES"  or inp=="yes":
                        x=disaster_module.updatefn()
                    else:
                        print("Task terminating. ThankYou!")
                else:
                    print("Task terminating. ThankYou!")
            else:
                print("Task terminating. ThankYou!")

                
        elif choice=='4':#WEATHER
            x=disaster_module.weather_forecast()
            print("\nNEED ANOTHER FORECAST?(y/n)")
            inp=input("")
            if inp=="Y" or inp=="y":
                x=disaster_module.weather_forecast()
                print("\nNEED ANOTHER FORECAST?(y/n)")
                inp=input("")
                if inp=="Y"  or inp=="y":
                    x=disaster_module.weather_forecast()
                    print("\nNEED ANOTHER FORECAST?(y/n)")
                    inp=input("")
                    if inp=="Y"  or inp=="y":
                        x=disaster_module.weather_forecast()
                    else:
                        print("Task terminating. ThankYou!")
                else:
                    print("Task terminating. ThankYou!")
            else:
                print("Task terminating. ThankYou!")



        elif choice=="3": #DISASTER HELP
            x=disaster_module.detail()
            print("\nCHECK PRECAUTIONS FOR ANOTHER CALAMITY?(y/n)")
            inp=input("")
            if inp=="Y" or inp=="y":
                x=disaster_module.detail()
                print("\nCHECK PRECAUTIONS FOR ANOTHER CALAMITY?(y/n)")
                inp=input("")
                if inp=="Y" or inp=="y":
                    x=disaster_module.detail()
                    print("\nCHECK PRECAUTIONS FOR ANOTHER CALAMITY?(y/n)")
                    inp=input("")
                    if inp=="Y" or inp=="y":
                        x=disaster_module.detail()
                    else:
                        print("Task terminating. ThankYou!")
                else:
                    print("Task terminating. ThankYou!")
            else:
                print("Task terminating. ThankYou!")

     
        elif choice=="5":#DETAILS OF OFFICERS
            x=disaster_module.officer_help()
            print("\nNEED MORE DETAILS?(y/n)")
            inp=input("")
            if inp=="Y"  or inp=="y":
                x=disaster_module.officer_help()
                print("\nNEED MORE DETAILS?(y/n)")
                inp=input("")
                if inp=="Y" or inp=="y":
                    x=disaster_module.officer_help()
                    print("\nNEED MORE DETAILS?(y/n)")
                    inp=input("")
                    if inp=="Y" or inp=="y":
                        x=disaster_module.officer_help()
                    else:
                        print("Task terminating. ThankYou!")
                else:
                    print("Task terminating. ThankYou!")
            else:
                print("Task terminating. ThankYou!")


        elif choice=="6":#PRINT_DETAILS
            x=disaster_module.printdet()
            print("\nNEED TO CHECK MORE DETAILS?(y/n)")
            inp=input("")
            if inp=="Y" or inp=="y":
                x=disaster_module.printdet()
                print("\nNEED TO CHECK MORE DETAILS?(y/n)")
                inp=input("")
                if inp=="Y" or inp=="y":
                    x=disaster_module.printdet()
                    print("\nNEED TO CHECK MORE DETAILS?(y/n)")
                    inp=input("")
                    if inp=="Y" or inp=="y":
                        x=disaster_module.printdet()
                    else:
                        print("Task terminating. ThankYou!")
                else:
                    print("Task terminating. ThankYou!")
            else:
                print("Task terminating. ThankYou!")

                
        else:#EXIT
            choice=="7"
            print("Task terminating. ThankYou!")
            
             
                
    else: #GOVERNMENT OFFICER
        
        print("\t~~~~~ENTER PASSWORD~~~~~(refer source_code)") #PASSWORD=KV
        password=input("")
        
        if password=="KV":
            print("LOGIN SUCCESS\n\n~~~MAIN MENU~~~ \n1. UPDATE MY DETAILS \n2.CHECK MY DETAILS \n3.KNOW MY CITIZENS(statewise) \n4.VIEW ALL CITIZENS   \n5.EDIT CITIZENS \n6.DELETE CITIZEN  \n7. REGISTER AS NEW(password required) \n**enter task number and press enter**")
            INPUT=input("")

            if INPUT=='1':#update
                x=disaster_module.update_officers()
                print("\nNEED TO UPDATE AGAIN?(y/n)")
                inp=input("")
                
                if inp=="Y" or inp=="y":
                    x=disaster_module.update_officers()
                    print("\nNEED TO UPDATE AGAIN?(y/n)")
                    inp=input("")
                    if inp=="Y" or inp=="y":
                        x=disaster_module.update_officers()
                        print("\nNEED TO UPDATE AGAIN?(y/n)")
                        inp=input("")
                        if inp=="Y" or inp=="y":
                            x=disaster_module.update_officers()
                        else:
                            print("Task terminating. ThankYou!")
                    else:
                        print("Task terminating. ThankYou!")
                else:
                    print("Task terminating. ThankYou!")

                   
            if INPUT=='2':#checkdetails
                selected=input("ENTER YOUR EMPLOYEE NO:")    
                query=("SELECT * FROM GOVT WHERE EMP_NO ='%s' " %(selected))
                mycur.execute(query)
                data=mycur.fetchall()
                c=mycur.rowcount
                if c>0:
                    print(tabulate(data,tablefmt='simple',numalign="justify",colalign=("justify",)))
                else:
                    print("EMPLOYEE NUMBER" ,selected,"NOT FOUND") 
                    
                    
            if INPUT=='3':#statewise citizens
                inp=input("ENTER YOUR STATE:")
                query=("SELECT * FROM NATION WHERE STATE ='%s' " %(inp))
                mycur.execute(query)
                data=mycur.fetchall()
                c=mycur.rowcount
                if c>0:
                    print(tabulate(data,tablefmt='simple',numalign="justify",colalign=("justify",)))
                elif c<=0:
                    print("NO CITIZENS IN" ,inp,"YET")
                print("\nANOTHER STATE CHECK?(y/n)")
                inp=input("")
                if inp=="Y" or inp=="y":
                    inp=input("ENTER YOUR STATE:")
                    query=("SELECT * FROM NATION WHERE STATE ='%s' " %(inp))
                    mycur.execute(query)
                    data=mycur.fetchall()
                    c=mycur.rowcount
                    if c>0:
                        print(tabulate(data,tablefmt='simple',numalign="justify",colalign=("justify",)))
                    else:
                        print("NO CITIZENS IN" ,inp,"YET")
                    
                

            if INPUT=='4': #all citizens
                query=("SELECT * FROM NATION;")
                mycur.execute(query)
                data=mycur.fetchall()
                alist=list(data)
                for row in alist:
                    print(row,"\n")

            if INPUT=='5':#updateforcitizens
                x=disaster_module.updatefn()
                print("\nNEED TO UPDATE FOR ANOTHER CITIZEN?(y/n)")
                inp=input("")
                if inp=="Y" or inp=="y":
                    x=disaster_module.updatefn()
                    print("\nNEED TO UPDATE FOR ANOTHER CITIZEN?(y/n)")
                    inp=input("")
                    if inp=="Y"  or inp=="y":
                        x=disaster_module.updatefn()
                        print("\nNEED TO UPDATE FOR ANOTHER CITIZEN?(y/n)")
                        inp=input("")
                        if inp=="Y"  or inp=="y":
                            x=disaster_module.updatefn()
                        else:
                            print("Task terminating. ThankYou!")
                    else:
                        print("Task terminating. ThankYou!")
                else:
                    print("Task terminating. ThankYou!")

            if INPUT=='6':
                x=disaster_module.deletecitizen()
                print("\nNEED TO DELETE ANOTHER CITIZEN?(y/n)")
                inp=input("")
                if inp=="Y" or inp=="y":
                    x=disaster_module.deletecitizen()
                    print("\nNEED TO DELETE ANOTHER CITIZEN?(y/n)")
                    inp=input("")
                    if inp=="Y" or inp=="y":
                        x=disaster_module.deletecitizen()
                        print("\nNEED TO DELETE ANOTHER CITIZEN?(y/n)")
                        inp=input("")
                        if inp=="Y" or inp=="y":
                            x=disaster_module.deletecitizen()
                        else:
                            print("Task terminating. ThankYou!")
                    else:
                        print("Task terminating. ThankYou!")
                else:
                    print("Task terminating. ThankYou!")


            if INPUT=='7':#exit
                 x=disaster_module.register_officers()
                
        else:
            print("~~~~~~WRONG PASSWORD~~~~~~ \n~~~~~~~~TRY AGAIN~~~~~~~~")
           
        
    restart = input("Would you like to restart this program?(y/n)\n")
    if restart == "Y" or restart == "y":
        script()
    if restart == "N" or restart == "n":
        print ("Script terminating. ThankYou!")

script()






