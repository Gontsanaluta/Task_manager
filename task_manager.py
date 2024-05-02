"""
Create a program to manage tasks assigned to users
 - Create login system for the users
 - Allow a user to:
    - Add task
    - View all tasks
    - View individual task

 - Allow only the admin to:
    - Register the users
    - View total tasks available
    - View the total number of registered users

"""

#=====importing libraries===========
from datetime import date

# Function to display information to the users and allows them to choose an option.
def user_menu():

    # List of available options to choose from
    opt = ['r', 'a', 'va', 'vm', 'e']

    print("\nSelect one of the following options: \n")
    print("r - register a user")
    print("a - add task")
    print("va - view all tasks")
    print("vm - view my tasks")
    print("e - exit: ")

    try:
        user_input = input("\nEnter the option\n").lower()
        if user_input in opt:
            pass
        else:
            print("Please enter one of the options provided i.e (\"a\" to add task)")
    except:
        ValueError("Invalid input")

    return user_input

# Function to register new users
def register():

    # Open the file and split users into a list
    with open("user.txt", "r") as file:
        file_list = file.read().splitlines()

    users = []
    password = []

    # Loops through the list and get only users from the file.
    for i in file_list:
        a, _ = i.split(",")
        users.append(a)
        
    new_user = input("Username: ")
    new_password = input("Password: ")
    password_confirm = input("Confirm password: ")
    
    # Verify the password to ensure the user did not make the mistake
    if new_password != password_confirm:
        print("\nPassword do not match\n")
        register()

    # Ensures that the new user name is not in the users file to avoid confusion and duplicates
    elif new_user in users:
        print("\nUsername exists\n")
        register()
    else:
        # Add the new user to the text file
        with open("user.txt", "a") as f:
            f.write(f'\n{new_user}, {password_confirm}')
    return

# Function to assign task to users
def assign_task():
    
    current_date = date.today()
    today = current_date.strftime("%d %b %Y")

    # Open the file and split users into a list
    with open("user.txt", "r") as file:
        file_list = file.read().splitlines()

    usernames = []

    # The for loop split the file_list which is in the form ["username, password"] into a variable "names" which stores only the usernames
    # and variable "_" which stores the passwords. However, password is not needed hence an underscore is used and only "names" is appended to the user's list
    for i in file_list:
        names , _ = i.split(",")
        usernames.append(names)

    try:
        user = input("Assign a user for the task: ")

        # Check if the user is registered
        if user in usernames:
                        title = input("Enter the title: ")   
                        description = input("Description of the task: ")
                        due_date = input("Due date: ")
                        status = "No" 
                        today_date = today

                        with open("tasks.txt", "a") as f:
                            f.writelines([f"\nTask:              {title}\n", 
                                          f"Assigned to:       {user}\n",
                                          f"Date assigned:     {today_date}\n", 
                                          f"Due date:          {due_date}\n",
                                          f"Task complete?     {status}\n", 
                                          f"Description:       {description}\n"])
        else:
            print(f"\n{user} is not registered! \n")
    except:
        ValueError("\nInvalid input try again!\n")
    

    return

# Function to print out all the tasks assigned to users
def view_task():

    # Opens and split the file where there are double lines
    file = open("tasks.txt", "r")
    read_file = file.read().split("\n\n")

    all_task = ""
    
    # Check if the file is empty and return appropriate message
    for line in read_file:
        all_task += line + "\n"*2

    if len(all_task.strip()) >= 1:
        print(all_task.strip())
        
    else:
        print("\nNo task available\n")

    return

# Function to find specified task for the user
def find_task(user):

    # Opens and split the file where there are double lines
    with open("tasks.txt", "r") as f:
        file = f.read()
        list_tasks = file.split("\n\n")

        # Stores task for specific user
        user_task = ""
            
        for line in list_tasks:

            if user in line:
                user_task += line + "\n"*2
                
        # Check if the file is empty and return appropriate message 
        if len(user_task.strip()) >= 1:
            print(user_task.strip())
        else:
            print("\nNo task available\n")

    return

# Function to allow only the admin to register and view statistics of the task.
def administrator():

    # Stores users and tasks to perfom calculations
    users = []
    tasks = []
    
    with open("user.txt", "r") as file:
        read_file = file.readlines()

        for line in read_file:
            a = line.strip().split(", ")
            users.append(a)
            
    with open("tasks.txt", "r") as f:
        file = f.read()
        list_tasks = file.strip().split("\n\n")
        
        for line in list_tasks:
            tasks.append(line)
            
    print(f"\nThe total number of registered users:     {len(users)}\n")
    print(f"The total number of tasks assigned:       {len(tasks)}\n")
    
    return 

# Function to display options for the admin
def admin_options():

    print("\nOptions\n")
    print("r -  Register a user")
    print("s - Display user stats")
    print("a - add task")
    print("va - view all tasks")
    print("vm - view my tasks")
    print("e - exit: ") 

    # Available options to choose from
    opt = ['r', 'a', 'va', 'vm', 's', 'e']

    try:
        admin_input = input("\nSelect an option: \n").lower()

        if admin_input in opt:
            pass
        else:
            print("Please enter one of the options provided i.e (\"r\" to Register a user)")
    except:
        ValueError("Invalid input")
    
    return admin_input

# Function to allow only registered users to access the file and the tasks.
def login():

    users = []

    # Opens and read user text file 
    with open("user.txt", "r") as file:
        read_file = file.readlines()
        for line in read_file:
            a = line.strip().split(", ")
            users.append(a)

    while True:
        user_name = input("Usermame: ")
        user_password = input("Password: ")

        # Loop through the users list
        for user in users:

            # Check if the user_name is in the users list
            if user[0] == user_name:
                # Check if the password correspond with the user
                if user[1] == user_password:
                    while True:

                        # Check if the user is the admin and provide the relavent options
                        if user[0] == "admin":
                            option = admin_options()

                            if option == "r":
                                register()
                            elif option == "s":
                                administrator()
                            elif option == "a":
                                assign_task()
                            elif option == "va":
                                view_task()
                            elif option == "vm":
                                admin_user = user_name
                                find_task(admin_user)
                            elif option == 'e':
                                print("\nGoodbye!!!\n")
                                exit()

                        # If not the admin display menu options to the user
                        else:
                            menu = user_menu()

                            if menu == 'r':
                                print("You are not allowed to register a user")

                            elif menu == 'a':
                                assign_task()

                            elif menu == 'va':
                                view_task()

                            elif menu == 'vm':
                                user = user_name
                                find_task(user)

                            elif menu == 'e':
                                print('\nGoodbye!!!\n')
                                exit()
                    else:
                        break
                else:
                    print("Incorrect password. Please try again")
                    login()
        else:
            print("Incorrect username. Please try again")
    return

login()
