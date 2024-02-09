import mysql.connector as connector #module import
db=connector.connect(
    host="localhost", user="root", passwd="marvelavengers",database="to_dolist", auth_plugin="mysql_native_password"
)

cursor=db.cursor() #creating cursor

# if db.is_connected():
#     print("Connected")
# else:
#     print("Failed to connect")

def checkDuplicateUserID(id):
    #to fetch all the ids from the table accounts and check if the id is present or not
    cursor.execute("SELECT ID FROM ACCOUNTS")
    ids=cursor.fetchall()
    if(id,) not in ids:
        return False
    else:
        return True

def create_Account(accountDetails):
    
        #This Method will create a Database for the User based on the Account ID of the User
        #Along with that will create a table in the User Database 
        #The table will contain all the Task which will be inserted in the To-Do-List
        #The Parameter accountDetails is a dictionary which will contain all the Account details
        
    
    records = (accountDetails["userid"],accountDetails["username"],accountDetails["password"])
    try:
        stringQuery = "INSERT INTO ACCOUNTS VALUES{records}".format(records=records)
        cursor.execute(stringQuery)
        db.commit()

        table_parameters = "TASK_ID INT PRIMARY KEY,TASK VARCHAR(30),STARTTIME TIME,ENDTIME TIME,COMPLETED CHAR(5)"
        
        stringQuery = "CREATE TABLE {table_name}({table_parameters})".format(table_name=accountDetails["userid"],table_parameters=table_parameters)
        cursor.execute(stringQuery)
        db.commit()
        return True
    except:
        return False



def accountlogin(accountDetails):
    
        #This method will be used for Login into the User Account
    
    id = accountDetails["userid"]
    try:
        stringQuery = "SELECT * FROM ACCOUNTS WHERE ID='{}'".format(id) # Creation of String Query
        cursor.execute(stringQuery) # Execution of the String Query in MySQL
        record = cursor.fetchall()[0] 
        # [("123","Samayita","paswd")]
        username = record[1]
        password = record[2]
        if username == accountDetails["username"] and password == accountDetails["password"]:
            return "success"
        else:
            return "failure"
    except:
        return "error"
    
def fetchRecordNumber(id):
    cursor.execute("SELECT TASK_ID FROM {}".format(id))
    rec=cursor.fetchall()
    l=len(rec)
    if l==0:
        return 1
    else:
        return l+1
    
def inserttask(id, tasktuple):
    try:
        stringQuery= "INSERT INTO {tablename} value{taskdetails}".format(tablename=id, taskdetails=tasktuple)
        cursor.execute(stringQuery)
        db.commit()
        return "success"
    except:
        return "failure"
    

def taskrecords(id):
    cursor.execute("select TASK_ID,TASK,STARTTIME,ENDTIME from {}".format(id))
    record=cursor.fetchall()
    return record

def update_Task(taskDetails):
    query= "UPDATE {tablename} SET COMPLETED='{value}' where TASK_ID={taskid}".format(
        tablename=taskDetails["userid"],
        value=taskDetails["compStatus"],
        taskid=taskDetails["taskid"]
    )
    try:
        cursor.execute(query)
        db.commit()
        return True
    except:
        return False
    
def delete_Task(taskid,accountId):
    
        #This Method will be deleting the task based on the TaskId from the Task List of the User
    
    try:
        cursor.execute("delete from {tablename} where TASK_ID={taskid}".format(tablename=accountId,taskid=taskid))
        db.commit()
        return True
    except:
        return False
    pass

def view_Task_List(accountId):
    
        #This Method will display the full Task List of the User that the User needs to follow
        #along with Task is Completed or not
    
    cursor.execute("select * from {}".format(accountId))
    record = cursor.fetchall()
    return record