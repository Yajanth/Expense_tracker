def main():
    print(f"***Running expense tracker:")

    #Choose the options below
    get_user_expense()


    #write those to csv
    write_expense_to_file()



    #read file and summarize the expense
    summarize_expenses()


def get_user_expense():
    print("Getting user expense:")
    expense_categories=[
        "🍎Food",
        "🏠Home",
        "💻Work",
        "🎉Fun",
        "🌠Misc"
    ]
    while True:
        print("Select your Expense Category: \n------------------------------------")

    expense_name=input("Enter the Expense Name:")
    expense_amount=float(input("Enter the amount:"))

def write_expense_to_file():
    print("Updating the expenses:")

def summarize_expenses():
    print("summary of the expenses:")



if __name__ == "__main__":
    main()
