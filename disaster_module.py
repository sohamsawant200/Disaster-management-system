import datetime
from tabulate import *
import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",
                                  passwd="kimaya",port='3306',
                              database='citizens')
mycur=mycon.cursor()
mycur.execute("create database if not exists CITIZENS;")
mycur.execute("create database if not exists GOVT;")
mycur.execute("use citizens")

#functions
def tsunami():
    return "                                      TSUNAMI \n\n****What to do before and During Tsunami****\n--->Turn on your radio to learn if there is tsunami warning if an earthquake occurs and you are in a coastal area. \n--->Be alert for early warninIf you are in dangerous area, immediately turn all the water gas and electricity and quickly move to a higher ground.\n--->Remember once tsunami warning is issued, it could be a matter of minutes, or even seconds, before the wave’s hits.\n--->If tsunami warning is issued, never go down to the beach to watch the waves come in.\n--->Listen to the portable radio to learn when its safe to return home.\n--->Stay away from the beach.\n--->Learn to understand and notice the sea. If there is noticeable recession in water away from the shore time become caution and move away immediately..\n--->Move inland to higher ground immediately and stay there.\n\n****What to do after Tsunami****\n--->After the Tsunami has hit, all food and water should be tested for contamination before they are eaten.\n--->All buildings should be checked for gas leaks and electricity shorts before anyone enters.\n--->Administrator first old only if you know what to do.\n--->Stay away from flooded and damaged areas until official say it is safe to returns.\n--->*Stay away from debris in the water, it may be safety hazards to boats and people.\n--->Save yourself not you’re passionate."    
def earthquake():
    return"                                      EARTHQUAKE  \n\nWhat to Do Before an Earthquake\n--->Repair deep plaster cracks in ceilings and foundations. Get expert advice if there are signs of structural defects.\n--->Anchor overhead lighting fixtures to the ceiling.\n--->Follow BIS codes relevant to your area for building standards\n--->Fasten shelves securely to walls.\n--->Place large or heavy objects on lower shelves.\n--->Store breakable items such as bottled foods, glass, and china in low, closed cabinets with latches.\n--->Hang heavy items such as pictures and mirrors away from beds, settees, and anywhere that people sit.\n--->Brace overhead light and fan fixtures.\n--->Repair defective electrical wiring and leaky gas connections. These are potential fire\n--->Secure water heaters, LPG cylinders etc., by strapping them to the walls or bolting to the\n--->Store weed killers, pesticides, and flammable products securely in closed cabinets with latches and on bottom shelves.\n--->Identify safe places indoors and outdoors.\n--->Under strong dining table, bed\n--->Against an inside wall\n--->Away from where glass could shatter around windows, mirrors, pictures, or where heavy bookcases or other heavy furniture could fall over\n--->In the open, away from buildings, trees, telephone and electrical lines, flyovers and bridges\n--->Know emergency telephone numbers (such as those of doctors, hospitals, the police, etc)\n--->Educate yourself and family members\n--->What to Do During an Earthquake\n--->Stay as safe as possible during an earthquake. Be aware that some earthquakes are actually foreshocks and a larger earthquake might occur. Minimize your movements to a few steps that reach a nearby safe place and stay indoors until the shaking has stopped and you are sure exiting is safe.\n\nIf indoors\n--->DROP to the ground; take COVER by getting under a sturdy table or other piece of furniture; and HOLD ON until the shaking stops. If there is no a table or desk near you,   cover your face and head with your arms and crouch in an inside corner of the building.\n--->Protect yourself by staying under the lintel of an inner door, in the corner of a room, under a table or even under a bed.\n--->Stay away from glass, windows, outside doors and walls, and anything that could fall, (such as lighting fixtures or furniture).\n--->Stay in bed if you are there when the earthquake strikes. Hold on and protect your head with a pillow, unless you are under a heavy light fixture that could fall. In that case, move           to the nearest safe place.\n--->Use a doorway for shelter only if it is in close proximity to you and if you know it is a strongly supported, load bearing doorway.\n--->Stay inside until the shaking stops and it is safe to go outside. Research has shown that most injuries occur when people inside buildings attempt to move to a different location          inside the building or try to leave.\n--->Be aware that the electricity may go out or the sprinkler systems or fire alarms may turn on.\n\nIf outdoors\n--->Do not move from where you are. However, move away from buildings, trees, streetlights, and utility wires.\n--->If you are in open space, stay there until the shaking stops. The greatest danger exists directly outside buildings; at exits; and alongside exterior walls. Most earthquake-related    casualties result from collapsing walls, flying glass, and falling objects.\n\nIf in a moving vehicle\n--->Stop as quickly as safety permits and stay in the vehicle. Avoid stopping near or under buildings, trees, overpasses, and utility wires.\n--->Proceed cautiously once the earthquake has stopped. Avoid roads, bridges, or ramps that might have been damaged by the earthquake.\n\nIf trapped under debris\n--->Do not light a match.\n--->Do not move about or kick up dust.\n--->Cover your mouth with a handkerchief or clothing.\n--->Tap on a pipe or wall so rescuers can locate you. Use a whistle if one is available. Shout only as a last resort. Shouting can cause you to inhale dangerous amounts of dust."
def flood():
    return "                                      FLOOD   \n\n****What to do before a flood**** \n\nTo prepare for a flood, you should:\n--->Avoid building in flood prone areas unless you elevate and reinforce your home.\n--->Elevate the furnace, water heater, and electric panel if susceptible to flooding.\n--->Install “Check Valves” in sewer traps to prevent floodwater from backing up into the drains of your home.\n--->Contact community officials to find out if they are planning to construct barriers (levees, beams and floodwalls) to stop floodwater from entering the homes in your area.\n--->Seal the walls in your basement with waterproofing compounds to avoid seepage.\n\nIf a flood is likely to hit your area, you should:\n--->Listen to the radio or television for information.\n--->Be aware that flash flooding can occur. If there is any possibility of a flash flood, move immediately to higher ground. Do not wait for instructions to move.\n--->Be aware of streams, drainage channels, canyons, and other areas known to flood Flash floods can occur in these areas with or without such typical warnings as     rain clouds or heavy rain.\n\nIf you must prepare to evacuate, you should:\n--->Secure your home. If you have time, bring in outdoor furniture. Move essential items to an upper floor.\n--->Turn off utilities at the main switches or valves if instructed to do so. Disconnect electrical Do not touch electrical equipment if you are wet or standing in water.\n\nIf you have to leave your home, remember these evacuation tips:\n--->Do not walk through moving water. Six inches of moving water can make you fall. If you have to walk in water, walk where the water is not moving. Use a stick to check the            firmness of the ground in front of you.\n--->Do not drive into flooded areas. If floodwaters rise around your car, abandon the car and move to higher ground if you can do so safely. You and the vehicle can be quickly swept   away"
def cyclone():
    return "                                      CYCLONE \n\n****Before the Cyclone season:****\n--->Check the house; secure loose tiles and carry out repairs of doors and windows\n--->Remove dead branches or dying trees close to the house; anchor removable objects such as lumber piles, loose tin sheets, loose bricks, garbage cans, sign-boards etc. which can fly in strong winds.\n--->Keep some wooden boards ready so that glass windows can be boarded if needed\n--->Keep a hurricane lantern filled with kerosene, battery operated torches and enough dry cells\n--->Demolish condemned buildings\n--->Keep some extra batteries for transistors\n--->Keep some dry non-perishable food always ready for use in emergency"
def landslide():
    return "                                      LANDSLIDE \n\n****Do’s****\n--->Prepare tour to hilly region according to information given by weather department or news\n--->Move away from landslide path or downstream valleys quickly without wasting time.\n--->Keep drains clean,\n--->Inspect drains for – litter, leaves, plastic bags, rubble etc.\n--->Keep the weep holes open.\n--->Grow more trees that can hold the soil through roots,\n--->Identify areas of rock fall and subsidence of buildings, cracks that indicate landslides and move to safer areas. Even muddy river waters indicate landslides upstream.\n--->Notice such signals and contact the nearest Tehsil or District Head Quarters.\n--->Ensure that toe of slope is not cut, remains protected, don’t uproot trees unless re- vegetation is planned.\n--->Listen for unusual sounds such as trees cracking or boulders knocking together.\n--->Stay alert, awake and active (3A’s) during the impact or probability of impact.\n--->Locate and go to shelters,\n--->Try to stay with your family and companions.\n\n****Don’ts****\n--->Check for injured and trapped persons.\n--->Mark path of tracking so that you can’t be lost in middle of the forest.\n--->Know how to give signs or how to communicate during emergency time to flying helicopters and rescue team.\n--->Try to avoid construction and staying in vulnerable areas.\n--->Do not panic and loose energy by crying.\n--->Do not touch or walk over loose material and electrical wiring or pole.\n--->Do not built houses near steep slopes and near drainage path.\n--->Do not drink contaminated water directly from rivers, springs, wells but rain water if collected directly without is fine.\n--->Do not move an injured person without rendering first aid unless the casualty is in immediate danger."
def covid():
    return"                                      IN CASE OF SUSPICION OF INFECTION OF COVID-19: \n--->Stay home until 14 days after last exposure and maintain social distance (at least 6 feet) from others at all times. \n--->The best way to protect yourself and others is to stay home for 14 days if you think you’ve been exposed to someone who has COVID-19. Check your local health department’s website for information about options in your area to possibly shorten this quarantine period.\n--->Self-monitor for symptoms. Check temperature twice a day.\n---> Watch for fever ,cough, or shortness of breath, or other symptoms of COVID-19. \n--->If you have a cough, fever and difficulty breathing seek medical care early - call your health facility by telephone first. If you have fever and live in an area with malaria or dengue seek medical care immediately"


def weather_forecast():
    from selenium import webdriver
    driver=webdriver.Chrome()
    city=str(input("ENTER THE NAME OF THE CITY FOR CURRENT WEATHER FORECAST:"))
    print ("\t\t\t\tFETCHING DATA...")

    try:
        driver.get("https://www.weather-forecast.com/locations/"+city+"/forecasts/latest")
        print(driver.find_elements_by_class_name("b-forecast__table-description-content")[0].text)
    except Exception as e:
            print("ERROR",e)


def update_officers():
    print("WHICH OF THE FOLLOWING NEED RECTIFICATION? \n1.STATE \n2.NAME \n3.POST \n4.CONTACT_NUMBER \n~~~~ENTER NUMBER~~~~")
    inp=input()
    if inp=='1':
        try:
            state_=input("ENTER YOUR STATE NAME:")
            empno=input("ENTER EMPLOYEE NUMBER;")
            sql = ("UPDATE GOVT SET STATE = '%s' WHERE EMP_NO = '%s' " %(state_,empno))
            mycur.execute(sql)
            mycon.commit()
            c=mycur.rowcount
            if c>0:
                print("UPDATED STATE")
            else:
                print("EMPLOYEE NUMBER" ,empno,"NOT FOUND")    
        except Exception as e:
            print("ERROR",e)
            
    if inp=='2':
        try:
            name__=input("ENTER NAME;")
            empno=input("ENTER EMPLOYEE NUMBER;")
            sql = ("UPDATE GOVT SET NAME = '%s' WHERE EMP_NO = '%s' " %(name__,empno))
            mycur.execute(sql)
            mycon.commit()
            c=mycur.rowcount
            if c>0:
                print("\nUPDATED NAME")
            else:
                print("EMPLOYEE NUMBER" ,empno,"NOT FOUND")    
        except Exception as e:
            print("ERROR",e)
            
    if inp=='3':
        try:
            POST=input("ENTER POST :")
            empno=input("ENTER EMPLOYEE NUMBER;")
            sql = ("UPDATE GOVT SET POST = '%s' WHERE EMP_NO = '%s' " %(POST,empno))
            mycur.execute(sql)
            mycon.commit()
            c=mycur.rowcount
            if c>0:
                print("\nUPDATED POST")
            else:
                print("EMPLOYEE NUMBER" ,empno,"NOT FOUND") 
        except Exception as e:
            print("ERROR",e)
            
    if inp=='4':
        try:
            contact_number=input("ENTER CONTACT NUMBER;")
            empno=input("ENTER EMPLOYEE NUMBER;")
            sql = ("UPDATE GOVT  SET CONTACT_NUMBER = '%s' WHERE EMP_NO = '%s' " %(contact_number,empno))
            mycur.execute(sql)
            mycon.commit()
            c=mycur.rowcount
            if c>0:
                print("\nUPDATED CONTACT NUMBER")
            else:
                print("EMPLOYEE NUMBER" ,empno,"NOT FOUND") 
        except Exception as e:
            print("ERROR",e)

def deletecitizen():
    try:
        cn=input("ENTER THE CITIZEN NUMBER FOR DELETING:")
        delete=("DELETE FROM NATION WHERE CNUMBER = '%s' ") %(cn)
        mycur.execute(delete)
        mycon.commit()
        c=mycur.rowcount
        if c>0:
            print ("CITIZEN DELETED")
        else:
            print("CITIZEN NUMBER" ,cn,"NOT FOUND")       

    except Exception as e:
            print("ERROR",e)

def updatefn():
    print("WHICH OF THE FOLLOWING NEED RECTIFICATION? \n1.STATE \n2.NAME \n3.AADHAR CARD \n4.BLOOD GROUP \n5.CONTACT_NUMBER \n6.DOB\n ~~~~ENTER NUMBER~~~~")
    inp=input()
    if inp=='1':
        try:
            state_=input("ENTER YOUR STATE NAME:")
            cn=input("ENTER YOUR CONFIDENTIAL CITIZEN NUMBER:")
            sql = ("UPDATE NATION SET STATE = '%s' WHERE CNUMBER = '%s' " ) %(state_, cn)
            mycur.execute(sql)
            mycon.commit()
            c=mycur.rowcount
            if c>0:
                print("UPDATED STATE")
                query=("SELECT * FROM NATION WHERE CNUMBER ='%s' " %(cn))
                mycur.execute(query)
                data=mycur.fetchall()
                print(tabulate(data,tablefmt='simple',numalign="justify",colalign=("justify",))) 
                print("\n~~~~~UPDATED SUCCESFULLY~~~~")
            else:
                print("CITIZEN NUMBER" ,cn,"NOT FOUND")
        except Exception as e:
            print("ERROR",e)    
        
    if inp=='2':
        try:
            name__=input("ENTER NAME;")
            cn=input("ENTER YOUR CONFIDENTIAL CITIZEN NUMBER:")
            sql = ("UPDATE NATION SET NAME = '%s' WHERE CNUMBER = '%s' ") %(name__,cn)
            mycur.execute(sql)
            mycon.commit()
            c=mycur.rowcount
            if c>0:
                print("\nUPDATED NAME")
                
                query=("SELECT * FROM NATION WHERE CNUMBER ='%s' " %(cn))
                mycur.execute(query)
                data=mycur.fetchall()
                print(tabulate(data,tablefmt='simple',numalign="justify",colalign=("justify",))) 
                print("\n~~~~~UPDATED SUCCESFULLY~~~~")
            else:
                print("CITIZEN NUMBER" ,cn,"NOT FOUND")
        except Exception as e:
            print("ERROR",e)
        
    if inp=='3':
        try:
            aadhar__card=input("ENTER AADHAR CARD NUMBER(12);")
            cn=input("ENTER YOUR CONFIDENTIAL CITIZEN NUMBER:")
            sql = ("UPDATE NATION SET AADHAR_CARD = '%s' WHERE CNUMBER = '%s' ") %(aadhar__card,cn)
            mycur.execute(sql)
            mycon.commit()
            c=mycur.rowcount
            if c>0:
                print("\nUPDATED AADHARCARD")
                
                query=("SELECT * FROM NATION WHERE CNUMBER ='%s' " %(cn))
                mycur.execute(query)
                data=mycur.fetchall()
                print(tabulate(data,tablefmt='simple',numalign="justify",colalign=("justify",))) 
                print("\n~~~~~UPDATED SUCCESFULLY~~~~")
            else:
                print("CITIZEN NUMBER" ,cn,"NOT FOUND")
        except Exception as e:
            print("ERROR",e)
        
    if inp=='4':
        try:
            blood_grp=input("ENTER BLOODGRP:")
            cn=input("ENTER YOUR CONFIDENTIAL CITIZEN NUMBER:")
            sql = ("UPDATE NATION SET BLOOD_GROUP = '%s' WHERE CNUMBER = '%s' ")  %(blood_grp,cn)
            mycur.execute(sql)
            mycon.commit()
            c=mycur.rowcount
            if c>=0:
                print("\nUPDATED BLOODGRP")
                query=("SELECT * FROM NATION WHERE CNUMBER ='%s' " %(cn))
                mycur.execute(query)
                data=mycur.fetchall()
                print(tabulate(data,tablefmt='simple',numalign="justify",colalign=("justify",))) 
                print("\n~~~~~UPDATED SUCCESFULLY~~~~")
            else:
                print("CITIZEN NUMBER" ,cn,"NOT FOUND")
        except Exception as e:
            print("ERROR",e)
       
    if inp=='5':
        try:
            contact_number=input("ENTER CONTACT NUMBER;")
            cn=input("ENTER YOUR CONFIDENTIAL CITIZEN NUMBER:")
            sql = ("UPDATE NATION SET CONTACT_NUMBER = '%s' WHERE CNUMBER = '%s' ") %(contact_number,cn)
            mycur.execute(sql)
            mycon.commit()
            c=mycur.rowcount
            if c>0:
                print("\nUPDATED CONTACT NUMBER")
                query=("SELECT * FROM NATION WHERE CNUMBER ='%s' " %(cn))
                mycur.execute(query)
                data=mycur.fetchall()
                print(tabulate(data,tablefmt='simple',numalign="justify",colalign=("justify",))) 
                print("\n~~~~~UPDATED SUCCESFULLY~~~~")
            else:
                print("CITIZEN NUMBER" ,cn,"NOT FOUND")   
        except Exception as e:
            print("ERROR",e)
            
    if inp=='6':
        try:
            D_OB=input("ENTER DOB(YYYY/MM/DD);")
            dateObject = datetime.datetime.strptime(D_OB, "%Y/%m/%d")
            queryValues = (str(dateObject.date()))
            cn=input("ENTER YOUR CONFIDENTIAL CITIZEN NUMBER:")
            sql = ("UPDATE NATION SET DOB = '%s' WHERE CNUMBER = '%s' ") %(queryValues,cn)
            mycur.execute(sql)
            mycon.commit()
            c=mycur.rowcount
            if c>0:
                print("\nUPDATED DOB")
                query=("SELECT * FROM NATION WHERE CNUMBER ='%s' " %(cn))
                mycur.execute(query)
                data=mycur.fetchall()
                print(tabulate(data,tablefmt='simple',numalign="justify",colalign=("justify",))) 
                print("\n~~~~~UPDATED SUCCESFULLY~~~~")
            else:
                print("CITIZEN NUMBER" ,cn,"NOT FOUND")
        except Exception as e:
            print("ERROR",e)

def detail():
    try:
        print("1.CYCLONE \n2.TSUNAMI \n3.EARTHQUAKE \n4.FLOOD \n5.LANDSLIDE \n6.COVID \n~~~~~enter the number to get details of any calamity~~~~")
        themechoose=input("")
        if themechoose=="1":
            print(cyclone())
        elif themechoose=="2":
                print(tsunami())
        elif themechoose=="3":
            print(earthquake())
        elif themechoose=="4":
            print(flood())
        elif themechoose=="6":
            print(covid())
            print("--------------------------------------------------!! IMPORTANT !!  IN CASE OF COVID, CONTACT CONCERNED AUTHORITIES IMMEDIATELY!------------------------------------")
        else:
            themechoose=="5"
            print(landslide())
    except Exception as e:
            print("ERROR",e)

def register():
    try:
        STATE=input("ENTER YOUR STATE NAME:")
        name=input("ENTER NAME;")
        aadharcard=input("ENTER AADHAR CARD NUMBER(12);")
        bloodgrp=input("ENTER BLOODGRP;")
        contactnum=input("ENTER CONTACT NUMBER;")
        dob=input("ENTER DOB(YYYY\MM\DD);")
        xyz=input("ENTER YOUR CNUMBER(single digit to create your unique identity number)")
        cn=name[0]+STATE[0]+str(dob[9])+str(dob[6])+str(xyz)
        input1=(name,aadharcard,STATE,bloodgrp,contactnum,dob,cn)
        add_citizen="INSERT INTO NATION(Name,AADHAR_CARD,STATE,BLOOD_GROUP,CONTACT_NUMBER,DOB,CNUMBER) VALUES (%s, %s, %s,%s, %s, %s, %s);"
        mycur.execute(add_citizen,input1)
        mycon.commit()
        print("\n\n~~~~~REGISTRATION SUCCESFULL~~~~")
        query=("SELECT * FROM NATION WHERE CNUMBER ='%s' " %(cn))
        mycur.execute(query)
        data=mycur.fetchall()
        print(tabulate(data,tablefmt='simple',numalign="justify",colalign=("justify",))) 
    except Exception as e:
            print("ERROR",e)

def register_officers():
    try:
        print("PLEASE ENTER PASSWORD BEFORE REGISTERING")
        password=input('')
        if password=="GOVT123":
            print("LOGIN SUCCESSFUL")
            STATE=input("\nENTER YOUR STATE NAME:")
            name=input("ENTER YOUR NAME;")
            POST=input("ENTER YOUR POST;")
            contactnum=input("ENTER CONTACT NUMBER:")
            xyz=input("ENTER EMPLOYEE NUMBER(single digit to create your unique identity number):")
            emp_no=name[0]+STATE[0]+STATE[1]+str(contactnum[3])+str(contactnum[2])+str(xyz)
            input1=(name,STATE,POST,contactnum,emp_no)
            add_citizen="INSERT INTO GOVT(Name,STATE,POST,CONTACT_NUMBER,EMP_NO) VALUES (%s, %s, %s,%s, %s);"
            mycur.execute(add_citizen,input1)
            mycon.commit()
            query=("SELECT * FROM GOVT WHERE EMP_NO ='%s' " %(emp_no))
            mycur.execute(query)
            data=mycur.fetchall()
            print(tabulate(data,tablefmt='simple',numalign="justify",colalign=("justify",))) 
            print("\n~~~~~REGISTRATION SUCCESFULL~~~~")
        else:
            print("wrong password")
    except Exception as e:
            print("ERROR",e)
            
def officer_help():
    try:
        selected=input("enter state:")    
        query=("SELECT NAME,POST,CONTACT_NUMBER FROM GOVT WHERE STATE ='%s' " %(selected))
        mycur.execute(query)
        data=mycur.fetchall()
        c=mycur.rowcount
        if c==0:
            print("NO DETAILS YET")
        else:
            print(tabulate(data,tablefmt='simple',numalign="justify",colalign=("justify",)))  
    except Exception as e:
            print("ERROR",e)


def printdet():
    try:
        cn=input("ENTER YOUR CONFIDENTIAL CITIZEN NUMBER:")    
        query=("SELECT * FROM NATION WHERE CNUMBER ='%s' " %(cn))
        mycur.execute(query)
        c=mycur.rowcount
        data=mycur.fetchall()
        if data=="None":
                print("NO DETAILS YET")
        else:
                print(tabulate(data,tablefmt='simple',numalign="justify",colalign=("justify",)))  
    except Exception as e:
            print("ERROR",e)

    
    
    


