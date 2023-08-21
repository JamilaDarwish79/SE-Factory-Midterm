import os 
import datetime

employee_info_file =("employee_info.txt")
login_attempts = 0
maximum_login_attempts = 5

def load_employee_info(filename) :
    employee_info = {}
    if os.path.exists(filename):
        with open(filename, "r") as file: 
          for line in file:
              employee_ID, username, join_date, gender, salary =line.strip().split(", ")   
              employee_info[employee_ID] ={
                  "username": username,
                  "join_date": join_date,
                  "salary": int(salary),
              }
    return employee_info 
def save_employee_info(filename,employee_info):
  with open(filename, "w") as file:
    for employee_ID, data in employee_info.items():
       file.write(f"{employee_ID},{data['username']},{data['join_date']},{data['gender']},{data['salary']}")

def admin_menu(employee_info):
    while True:
      print("1. display statistics")
      print("2. add an employee")
      print("3. display all employees")
      print("4. change employee salary")
      print("5. remove employee")
      print("6. raise employee salary")
      print("7. exit")

      choice = input(" enter a number ")
      if choice == "1":
         male_number = sum(1 for employee in employee_info.values() if employee["gender"] == "male")
         female_number = sum(1 for employee in employee_info.values() if employee["gender"] == "female")
         print(f"male employees: {male_number}")
         print(f"female employees: {female_number}")
        
      elif choice == "2":
          employee_ID =  "employee{len(employee_info) + 1:02}"
          username = input("enter the employee username")
          gender = input("employee gender") 
          salary = int(input("enter employee salary"))
          join_date = datetime.datetime.now()
          employee_info[employee_ID] = {
            "username": username,
            "join_date": join_date,
            "gender" : gender,
            "salary": salary,
          }
          print(f"employee {employee_ID} is added")
      elif choice == "3":
      
   
          print(f"Employee ID: {employee_ID}")
          print(f"Username: {employee_data['username']}")
          print(f"Join Date: {employee_data['join_date']}")
          print(f"Gender: {employee_data['gender']}")
          print(f"Salary: {employee_data['salary']}")
        
      elif choice == "4":
      
         employee_ID = input("Enter the ID ")
      if employee_ID in employee_info:
                new_salary = int(input("Enter the new salary"))
                employee_info[employee_ID]["salary"] = new_salary
                print(f"Salary for employee {employee_ID} is updated")
              
      elif choice == "5":
            employee_ID = input("Enter the ID ")
            if employee_ID in employee_info:
                del employee_info[employee_ID]
                print(f"employee {employee_ID}is removed")
         
      elif choice == "6":
            employee_ID = input("Enter the ID ")
      if employee_ID in employee_info:
                raise_percentage = float(input("Enter raise percentage"))
                employee_info[employee_ID]["salary"] *= raise_percentage
                print(f"Salary of {employee_ID} is raised")
        
      elif choice == "7":
            save_employee_info(employee_info_file, employee_info)
            print("Data saved. Will exit now")
            break
          
def user_menu(username, gender, employee_info):
    while True:
      if gender == "male":
            print("Hello Mr. {username}")
      else:
            print("Hello Ms. {username}")
        
      print("1. Check Salary")
      print("2. Exit")
        
      choice =input("Enter a number ")
        
      if choice == "1":
          if username in [employee_data["username"] for employee_data in 
             employee_info.values()]:
                salary = next(employee_data["salary"] for employee_data in employee_info.values()if employee_data["username"] == username)
                print("The salary is: {salary}")
        
      elif choice == "2":
         print("Exiting")
         break
            

employee_info = load_employee_info(employee_info_file)

while login_attempts < maximum_login_attempts:
    username = input("Enter username ")
    password = input("Enter password (and if you are a normal user dont enter any data) ")
    
    if username == "admin" and password == "admin123123":
        admin_menu(employee_info)
        break
    elif username in [employee_data["username"] for employee_data in employee_info.values()]:
        gender = next(employee_data["gender"] for employee_data in employee_info.values() if employee_data["username"] == username)
        user_menu(username, gender, employee_info)
        break

if login_attempts >=  maximum_login_attempts:
    print("You reached the maximum allowed limit for login tries. Closing the program.")
