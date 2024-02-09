import random

from tabulate import tabulate
import databaseconnection as to_dolist
 
print("================================================================".center(140))
print("your todolist".center(140))
print("================================================================".center(140))
flag=0
id=""
a=input("DO you want to USE THE TO_DO_LIST(Y/y/N/n):".center(140))
a=a.lower()
if a=='n' or a=='no':
    quit()

#for user login
while True:
    print("================================================================".center(140))
    print("PLEASE LOGIN OR REGISTER TO USE THIS APPLICATION".center(140))
    print("1) LOGIN".center(140))
    print("2) REGISTER".center(140))
    print("3) EXIT".center(140))
    print("================================================================".center(140))

    choice=int(input("enter your choice: ".center(140)))
    

    if choice==2:
        #signup info
        username=input("enter username:".center(140))
        psswd=input("enter password:".center(140))

        #to generate userid
        id="U"+str(random.randint(0,999))

        #to check for duplicate id
        while to_dolist.checkDuplicateUserID(id):
            id="U"+str(random.randint(0,999))

        #to display the id
        print("Your id {} is successfully generated".format(id).center(140))
        print("THIS ID IS REQUIRED FOR NEXT TIME LOGIN".center(140))
        accountdetails={
        "userid":id,
        "username":username,
        "password":psswd
        }
        if to_dolist.create_Account(accountdetails):
            print("===========================================================================".center(140))
            print("Dear {} Your Account has been created Succesfully".format(username).center(140))
            print("You are successfully Logged-In to your account".center(140))
            print("===========================================================================".center(140))
            flag = 1
            break
        else:
            print("===========================================================================".center(140))
            print("Dear {} Some Problem occurred while creating you Account".format(username).center(140))
            print("Try Again".center(140))
            print("===========================================================================".center(140))
            flag = 0
            continue


        
    if choice==1:
        #login implementation
        id=input("Enter your id: ")
        username=input("Enter username:")
        psswd=input("Enter password:")
    
    #creating dictionary to store account details
    accountdetails={
        "userid":id,
        "username":username,
        "password":psswd
    }
    #to call the login function
    status= to_dolist.accountlogin(accountdetails)
    if status=="success":
        print("=========================================================================".center(140))
        print("Dear{}".format(username).center(140))
        print(" you are successfully logged in".center(140))
        print("=========================================================================".center(140))
        flag=1
        break
    elif status=="failure":
        print("=========================================================================".center(140))
        print("Dear{}".format(username).center(140))
        print("Provide valid username and password".center(140))
        print("=========================================================================".center(140))
    elif status=="error":
        print("=========================================================================".center(140))
        print("Dear{}".format(username).center(140))
        print(" Some error occurred while login".center(140))
        print("=========================================================================".center(140))

    if choice == 3:
        quit()

while True:
    print("===============================================================================================".center(140))
    print("To-Do-List Operations".center(140))
    print("===============================================================================================".center(140))
    print("1) Insert Task into the To-Do-List".center(140))
    print("2) Update Task in the To-Do-List ".center(140))
    print("3) Delete Task from the To-Do-List".center(140))
    print("4) Track Task".center(140))
    print("0) Log-Out from the Application".center(140))
    print("===============================================================================================".center(140))

    choice = int(input("Enter which Operation do you want to perform : "))
    if choice == 1:
        
            #Inserting of Task into the To-Do-List
            
        taskname = input("Enter the Task Name : ")
        startTime = input("Enter the Starting Time of the Task (Enter the Starting Time in the Format (hh:mm:ss)) : ")
        endTime = input("Enter the Ending Time of the Task (Enter the Ending Time in the Format (hh:mm:ss)) : ")
        # By Default Completed will be No
        complete = "No"
        # to get the record Number
        taskid = to_dolist.fetchRecordNumber(id) 
        tasktuple=(taskid, taskname, startTime, endTime, complete)
        status=to_dolist.inserttask(id, tasktuple)
        if status == "success":
            print("===============================================================================================".center(140))
            print("Insertion of the Task is Successfull".center(140))
            print("===============================================================================================".center(140))
        else:
            print("===============================================================================================".center(140))
            print("Insertion of the Task is Not Done. Some error Occurred".center(140))
            print("===============================================================================================".center(140))
    
    elif choice==2:
        records=to_dolist.taskrecords(id)
        print(tabulate(records,headers=['TASK_ID','TASK','STARTTIME','ENDTIME']).center(140))
        taskid=int(input("Enter the task id of the task you want to update."))
        isCompleted= input("Is the task completed?(yes/no):")
        if isCompleted == "No":
            print("===============================================================================================".center(140))
            print("There is no need for any Updation as Completed Status is By Default No".center(140))
            print("===============================================================================================".center(140))
            continue
        taskDetails = {"taskid":taskid,"compStatus":isCompleted,"userid":id}
        if to_dolist.update_Task(taskDetails):
            print("===============================================================================================".center(140))
            print("Updation of the Task is Succesfull".center(140))
            print("===============================================================================================".center(140))
        else:
            print("===============================================================================================".center(140))
            print("Updation of the Task is Not Succesfull".center(140))
            print("===============================================================================================".center(140))

    elif choice == 3:
        
            #Deletion of the specified Task by the user from the To-Do-List of the User
            #First it will promt the User to enter any Task which they want to delete and then it will delete the Task from the To-Do-List
        

        print("===============================================================================================".center(140))
        print("The Task List As Follows : ".center(140))
        records = to_dolist.view_Task_List(id)
        print(tabulate(records,headers=['TASK_ID','TASK','STARTTIME','ENDTIME','COMPLETED']).center(140))
        print("===============================================================================================".center(140))
        taskid = int(input("Enter the Task you want to delete : ".center(140)))
        if to_dolist.delete_Task(taskid,id):
            print("===============================================================================================".center(140))
            print("Deletion is Suuccessfully Done".center(140))
            print("===============================================================================================".center(140))
        else:
            print("===============================================================================================".center(140))
            print("Deletion is Not Suuccessfully Done".center(140))
            print("===============================================================================================".center(140))

    elif choice == 4:
       
            #After Clicking on this Option the User can View the Full To-Do-List in a Tabular format
        
        print("===============================================================================================".center(140))
        print("The Task List As Follows : ".center(140))
        records = to_dolist.view_Task_List(id)
        print(tabulate(records,headers=['TASK_ID','TASK','STARTTIME','ENDTIME','COMPLETED']).center(140))
        print("===============================================================================================".center(140))
    
    elif choice==0:
        quit()

        

      