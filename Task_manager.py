'''Capstone template project for FCS Task 19 Compulsory task 1.
This template provides a skeleton code to start compulsory task 1 only.
Once you have successfully implemented compulsory task 1 it will be easier to
add a code for compulsory task 2 to complete this capstone'''

#=====importing libraries===========
#Read and write files

from datetime import date

#open text files
##open_task = open("tasks_file.txt","a+")      
open_user = open("user_password_file.txt","r+")
a_open_task = open("tasks_file.txt","a+")  

#====Login Section====
#prompted to enter a username and password 
file_username_ = input ("Enter your username:\n")                
file_pass_ = input ("Enter your password:\n")      
entry = False

#have the programme check run through the login details on the user text file 
#split the sentance
#if the login credentials are correct break
for line in open_user:                                      
    split_sentance = line.split(", ")                      
    code_username1 = split_sentance[0]
    code_pass = split_sentance[1]   
    code_pass = code_pass.replace("\n","")
    if code_username1 == file_username_ and code_pass == file_pass_:     
        entry=True
        break
open_user.close()

#if incorrect username and password prompt user to re-enter details
if entry == False:
    print("Username/Passwords do not match. Please try again:\n")                            
    file_username_ = input("Incorrect username. Enter correct username:\n") 
    file_pass_ = input("Incorrect password. Enter correct password:\n")
    open_user = open("user_password_file.txt","r+")
    for line in open_user:
        split_sentance = line.split(", ")
        code_username1 = split_sentance[0]
        code_pass = split_sentance[1]
        code_pass = code_pass.replace("\n","")
        if code_username1 == file_username_ and code_pass == file_pass_:
            entry=True
            break
#===========================================================================        
#if correct display the menu option
#if the user is admin display the menu with view stats. Prompt the user to chose an input 
while entry == True:                                        
    if file_username_ == "admin":                             
        menu=input ('''Select one of the following Options below:
                    r - Registering a user
                    a - Adding a task
                    va - View all tasks
                    vm - view my task
                    vs - view stats
                    e - Exit
                    :\n ''').lower()

#if it's a different user display the menu without view stats. Prompt the user to choose an input
    else:                                              
        menu=input ('''Select one of the following Options below:
                    r - Registering a user
                    a - Adding a task
                    va - View all tasks
                    vm - view my task
                    e - Exit
                    :\n ''').lower()
#===========================================================================          
#if the user is admin and chooses "r" allow  the user to register a new user
#admin to enter name, admin to enter password,  admin to confrim password
#if the password don't match, prompt admin to re-enter the correct password
#if passwords match write the name and password on the text
    if menu == "r":
        if file_username_ == "admin":
            print('Registering a user please\n')
            r_new_user_name=input("Enter the new username:\n")  
            r_new_user_pass=input("Enter the new user's password:\n")
            con_new_pass = input ("Please confirm the password:\n") 
            while con_new_pass != r_new_user_pass:         
                con_new_pass = input("Passwords do not match. Please reconfirm the password:\n")
            if con_new_pass == r_new_user_pass: 
                open_user.write("\n"+r_new_user_name+", "+r_new_user_pass)
        else:
            print("You don't have access to this function.")
#===========================================================================                  
#if the user chooses "a" open the task text, to read and write
#ask user to input the details & print the details on the tasks text
    elif menu == "a": 
        a_open_task = open("tasks_file.txt","a+")                               
        a_task_username=input("Enter the username of the person the task is assigned to:\n")  
        a_task_title=input("Enter the title of the task:\n")
        a_task_describtion=input("Enter a description of the task:\n")
        a_task_date=input("Enter the due date of the task: \n")
        #today_date=date.today()
        #print(today_date)
        a_task_complete = ("No")                         
        a_open_task.write ("\n"+a_task_username+", "+a_task_title+", "+a_task_describtion+", "+str(a_task_date)+", "+a_task_complete)
        a_open_task.close()
#==============================================================================
#if the user "va" open the task text, to read
#split the sentence and assign names to the new strings & print all tasks in user-friendly, easy to read manner     
    elif menu == "va":                                  
        a_open_task = open("tasks_file.txt","r")
        for line in a_open_task:
            split_task=line.split(", ")                                  
            task_username1=split_task[0]
            task_title1=split_task[1]
            task_describtion1=split_task[2]
            task_date1=split_task[3]
            today_date1=split_task[4]
            task_completed1=split_task[5]               
            print("Task:\t\t\t"+task_title1+"\n Assigned to:\t\t"+task_username1+"\nDate assigned:\t\t"+today_date1+"\nDue date:\t\t"+task_date1+"\nTask completed:\t\t"+task_completed1+"Task description:\n"+task_describtion1+"\n")
        a_open_task.close()
#==============================================================================
#if the user "vm" open the task text, to read and write
#split the sentence and assign names to the new strings         
    elif menu=="vm":                                    
        a_open_task = open("tasks_file.txt","r+")
        for line in a_open_task:
            split_task=line.split(", ")                 
            if str.lower(file_username_)== str.lower(split_task[0]):
                tusername = split_task[0]               
                task = split_task[1]
                task_description = split_task[2]
                task_assigned = split_task[3]
                due_date = split_task[4]
                task_completion = split_task[5]
                print("Task username: ", tusername,
                      '\nTask: ', task,
                      '\nTask Description: ', task_description,
                      '\nDate Assigned: ', task_assigned,
                      '\nTask Due Date: ', due_date,
                      '\nTask Completed: ', task_completion)
        a_open_task.close()
#==============================================================================
#if the user "vs" open the task text, to read
#create variable with the value zero, split the sentence
#if the user name is equal to task user. then count the sentences that with the username

    elif menu=="vs":                                 
        task_count = 0
        user_count = 0
    
        # Open the task file and count the number of tasks
        with open("tasks_file.txt", "r") as f:
            for line in f:
                task_count += 1
    
        # Open the user password file and count the number of users
        with open("user_password_file.txt", "r") as f:
            for line in f:
                user_count += 1
    
        # Display the statistics
        print("Total number of tasks: ", task_count)
        print("Total number of users: ", user_count)





    
#==============================================================================                   
    elif menu=="e":
        break         
      
open_user.close()
