#Import section
from datetime import date
from os import system
import csv 

class User:
    def __init__(self, name, user_id, income, initial_date):
        self.name = name
        self.user_id = user_id
        self.income = income
        self.initial_date = initial_date
        self.expenses = 0.0
        self.expense_type_list = []

    def __repr__(self):
        #system('clear')
        return f"""
-------- USER INFO --------

- User: {self.name}

    ID: {self.user_id} 

    Income: {self.income}

    Expenses: {self.expenses} 

    List of Expenses: {self.expense_type_list}

    Starting Date: {self.initial_date}       

--------------------------"""
    
    #Defining two methods for adding incomes and to register expenses
    def add_income(self, new_income):
        self.income += new_income
    
    def add_expense(self, expense_description_as_list):
        new_expense = float(expense_description_as_list[2])
        self.expenses += new_expense
        self.expense_type_list.append(expense_description_as_list)
    
    def financial_summary(self):
        ideal_essentials = self.income * 0.50
        ideal_dispensables = self.income * 0.30
        ideal_savings = self.income * 0.20 

        real_essentials = 0.0
        real_dispensabe = 0.0
        for list in self.expense_type_list:
            if list[0] == 'essential':
                real_essentials += float(list[2])
            else:
                real_dispensabe += float(list[2])
        debt_or_profit = round(((self.income-self.expenses)*100)/self.income)
        
        if debt_or_profit > 0:
            system('clear')
            financial_health = f"""
---------- FINANCIAL HEALTH SUMMARY ----------

- Essential expenses   
    Percentage expend: ({round((real_essentials*100)/self.income)}%)
    Money expend:      ${real_essentials}
    (Ideal ${round(ideal_essentials, 1)} (50%))
    --- Money left for essential expenses: ${ideal_essentials-real_essentials} ---

- Dispensable expenses 
    Percentage expend: ({round((real_dispensabe*100)/self.income)}%)
    Money expend:      ${real_dispensabe}
    (Ideal ${round(ideal_dispensables, 1)} (30%))
    --- Money left for dispensables: {ideal_dispensables - real_dispensabe}

- Savings budget       
    Percentage for posible savings: ({debt_or_profit}%)
    Money for posible savings:      ${self.income-self.expenses}
    (Ideal ${round(ideal_savings, 1)} (20%))
------------------------------------------------
              """
        else:
            system('clear')
            financial_health = f"""
---------- FINANCIAL HEALTH SUMMARY ----------

- Essential expenses   
    Percentage expend: ({round((real_essentials*100)/self.income)}%) 
    Money expend:      ${real_essentials}  
    (Ideal ${round(ideal_essentials, 1)} (50%))

- Dispensable expenses 
    Percentage expend: ({round((real_dispensabe*100)/self.income)}%) 
    Money expend:      ${real_dispensabe}
    (Ideal ${round(ideal_dispensables, 1)} (30%))

- Debt                 ({debt_or_profit*-1}%): ${self.income-self.expenses}
------------------------------------------------
              """
        
        financial_health += "\n----- EXPENSE LIST: -----"
        enumerator = 1
        for i in self.expense_type_list:
            financial_health += f"\n{enumerator}. {i[1].upper()}: ${i[2]}"
            enumerator += 1
        print(financial_health)
    
    def save(self):
        with open('./financial-health-user-data.csv', 'a', newline='')  as user_data:
            writer = csv.writer(user_data, delimiter=',')
            temp_list = None
            for i in self.expense_type_list:
                if temp_list == None:
                    temp_list = [[self.user_id, i[0], i[1], str(i[2])]]
                else:
                    temp_list.append([self.user_id, i[0], i[1], str(i[2])])
            writer.writerow([self.name, self.user_id, self.income, self.initial_date])
            writer.writerows(temp_list)
  
#Defining global variables

streaming_platform = {1: 'netflix', 2: 'max', 3: 'amazon prime', 4: 'paramount+', 5: 'disney+'}

#Defining global functions
def main():
    while True:
        welcome_string = f""" 
        ------------ MAIN MENU ------------
        Hello, {object1.name} and welcome
        to the main menu, here you can chose
        what you want the program to do, so...
        what you want to do this time?
                
            1. Add a New Income 

            2. Add a New Expense 

            3. Print your information

            4. Get your "Financial Health" Summary

            5. EXIT

        -----------------------------------
            Please type your choice: """
            
        # Checks if the input is a digit before trying to convert to int()
        in_or_outcome = input(welcome_string)
        while in_or_outcome.isdigit() == False:
            print('\nInvalid option.\nChoose between option 1 and 5.\n')
            in_or_outcome = input(welcome_string)
        in_or_outcome = int(in_or_outcome)

        system("clear")
        if in_or_outcome == 1:
            _new_income = float(input("Type the amount of the income: $"))
            object1.add_income(_new_income)
            print("-- INFORMATION --\n-- Income added successfully --")

        elif in_or_outcome == 2:
            #I just create a temp list cuz else it will create a list of a list causing a problem when saving
            expense_description = []
            temp_expense_list = []
            temp_expense_list.append(expense_tags())
            expense_amount = float(input("Please, type the amount you spend: $"))
            
            temp_expense_list[0].append(expense_amount)
            expense_description = temp_expense_list[0]

            object1.add_expense(expense_description)

        elif in_or_outcome == 3:
            print(object1)

        elif in_or_outcome == 4:
            object1.financial_summary()

        elif in_or_outcome == 5:
            object1.save()
            break
        else:
            print("Error: not a valid option")

#Function to add diferent types of entertaiment expenses
def expense_tags():
    #system('clear')
    choice_string = """ 
---------- TYPE OF EXPENSE ----------------
Please, choice what type of expense it was:
                                  
    1. Paying rent
    2. Buying grocerys
    3. Paying the electric, water and/or gas bill
    4. Transportations and/or own transportation + gas
    5. Buying medicine
    6. Money for an emergency situation
    7. For eating out or a delivery food
    8. Entertaiment
                              
-------------------------------------------
    Type your choice: """
    # Checks if the input is a digit before trying to convert to int()
    option_choice = input(choice_string)
    while option_choice.isdigit() == False:
        print('\nInvalid option.\nChoose between option 1 and 8.\n')
        option_choice = input(choice_string)
    option_choice = int(option_choice)

    if option_choice == 1:
        return ['essential', 'rent']
    elif option_choice == 2:
        return ['essential', 'grocery']
    elif option_choice == 3:
        return ['essential', 'house bills']
    elif option_choice == 4:
        return ['essential', 'transportation']
    elif option_choice == 5:
        return ['essential', 'medicine']
    elif option_choice == 6:
        return ['essential', 'emergency']
    elif option_choice == 7:
        return ['dispensable', 'delivery']
    elif option_choice == 8:
        is_streaming = int(input("What type of entertaiment:\n1. Streaming services\n2. Other\nType your option choice: "))
        if is_streaming == 1:
            streaming_name = str(input("Which one (Like Netflix, Disney+, etc...): "))
            return ['dispensable', streaming_name.lower()]
        elif is_streaming == 2:
            return ['dispensable', 'entertaiment']
        else:
            print("Error: Not a Valid Option")
            main()
    else:
        print("Error: Not a Valid Option")
        main()
    
#Welcome and Reading the variables for the object
print("""
________________________________________________________
------------------  FINANCIAL HEALTH  ------------------
       
Welcome to "Financial Helth". This program will help you
keep track of all your expenses and also will give you 
some hits in case your "Financial Health" is in bad shape
To start, let me know some information about you.\n""")

user_id_input = input("ID number: ")
#Reading the file to compare the user_id to see if is a new or an existent user
with open('./financial-health-user-data.csv') as user_data:
            data = csv.reader(user_data, delimiter=',')
            file_to_list = list(data)
            temp_list = []
            for sub_list in file_to_list:
                for item in sub_list:
                    temp_list.append(item)
            
            #This next piece of code will check if the user already exists by the "user_id" input
            if user_id_input in temp_list:
                for users in file_to_list:
                    if users[1] == user_id_input:

                        expenses_count = 0
                        list_for_saving = []

                        index = file_to_list.index(users)
                        name_in_file = users.pop(0)
                        user_id_in_file = users.pop(0)
                        income_in_file = float(users.pop(0))
                        date_in_file =  users.pop(0)
                        object1 = User(name_in_file, user_id_in_file, income_in_file, date_in_file)

                        expenses_for_this_user = file_to_list[index+1:]
                        
                        for expense_description_in_file in expenses_for_this_user:
                            if expense_description_in_file[0] != user_id_in_file:
                                break
                            else:
                                expenses_count +=1
                                object1.add_expense(expense_description_in_file[1:])
                        list_for_saving = file_to_list[:index] + file_to_list[(index+expenses_count)+1: ]
                        with open('/Users/alejandrohenaoecheverri/Documents/Python/FH App/financial-health-user-data.csv', 'w', newline='')  as user_data:
                            writer = csv.writer(user_data, delimiter=',')
                            writer.writerows(list_for_saving)
                        print(f"""
-----------------------
Welcome back, {object1.name}
Here is your current info:
{object1}
                              """)
            else:
                name_input = input("Name: ")
                income_input = float(input("Monthly Income: "))
                initial_date_input = date.today()
                object1 = User(name_input, user_id_input, income_input, initial_date_input)

system('clear')
main()


