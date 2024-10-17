from expense import Expense 

def main():
    print(f"***Running expense tracker:")

    #Choose the options below
    expense=get_user_expense()
    file_path="Expense.csv"

    #write those to csv
    write_expense_to_file(expense,file_path )
 
    #read file and summarize the expense
    summarize_expenses()


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
    print(f"🎯Updating the expense{expense} to {file_path} :")

    with open(file_path,"a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount} \n")

def summarize_expenses():
    print("🎯Summary of the expenses:")



if __name__ == "__main__":
    main()
