import datetime

def validate_date(date_str):
   
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def format_currency(amount):
  
    return "${:,.2f}".format(amount)

def calculate_net_worth(income, expenses):
   
    return income - expenses

if __name__ == "__main__":
    date_str = "2023-10-02"
    print(validate_date(date_str))  

    amount = 12345.6789
    print(format_currency(amount))  

    income = 500000.0
    expenses = 300000.0
    net_worth = calculate_net_worth(income, expenses) 
    print("Net Worth:", format_currency(net_worth))
