from expense import Expense 
from datetime import datetime


def main():
    print(f"***Running expense tracker****:")

    #Choose the options below
    expense=get_user_expense()
    file_path="Expense.csv"
    month_budget=2000

    #write those to csv
    write_expense_to_file(expense,file_path )
 
    #read file and summarize the expense
    summarize_expenses(file_path,month_budget)


def get_user_expense():
    print("🎯Getting user expense:")
    expense_categories=[
        "🍎Food",
        "🏠Home",
        "💻Work",
        "🎉Fun",
        "🌠Misc"
    ]
    expense_name=input("Enter the Expense Name:")
    expense_amount=float(input("Enter the amount:"))
    while True:
        print("Select your Expense Category: \n------------------------------------")
        for i , category in enumerate(expense_categories):
            print(f"{i+1}. {category}")

        value_range=f"[1 - {len(expense_categories)}]"
        selected_index=int(input(f"Select a category {value_range}:")) -1
        if selected_index in range(len(expense_categories)):
            selected_category=expense_categories[selected_index]
            new_expense=Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid Category. Plase try again!")



def write_expense_to_file(expense:Expense, file_path):
    print(f"\n🎯Updating the expense{expense} to {file_path} .")

    with open(file_path,"a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount} \n")

def summarize_expenses(file_path,month_budget):
    print("\n🎯Summary of the expenses:")

    with open(file_path,"r") as f:
        lines=f.readlines()
        expense_list=[]
        expense_dict={        
        "🍎Food":0,
        "🏠Home":0,
        "💻Work":0,
        "🎉Fun":0,
        "🌠Misc":0}
        total_expense=0

        for line in lines:
            stripped_line=line.strip()
            expense_name,expense_category,expense_amount=stripped_line.split(",")
            line_expense=Expense(name=expense_name,category=expense_category,amount=expense_amount)
            expense_list.append(line_expense)  

            # Storing the total expense by category
            expense_dict[expense_category]+=float(expense_amount)
            total_expense+=float(expense_amount)

        for key in expense_dict:

            print(f" {key} : €{expense_dict[key]:.2f}")
            

        print(f"\n💸 Total Expense till <{datetime.now().date()}>  is : {total_expense:.2f}")
        print(green(f"💰 Budget left for the month: {(month_budget - total_expense):.2f}"))

#function to convert text to green
def green(text):
    return f"\033[92m{text}\033[0m"


if __name__ == "__main__":
    main()
