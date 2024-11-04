"""
Author: Ved Vyas
Functionality of code:
I built this cool investment calculator to figure out how much money I'd make if I had 
invested in Apple stock 10 years ago. I've always been fascinated by the power of 
long-term investing, so I wanted to create something that would show me (and others) 
the potential returns. The program is pretty straightforward - you just input some basic 
info about stock prices and it tells you how rich (or not) you'd be today!
"""

from datetime import datetime, timedelta  # I need these for handling dates
import numpy as np  # This is my go-to library for mathematical calculations

def calculate_investment_returns():
    # I like to start with a nice header to make it look professional
    print("Apple Stock Investment Calculator")
    print("-" * 30)  # Just a simple line to make things look organized
    
    # Here's where I get the current date from the user and make sure they enter it correctly
    while True:
        try:
            current_date_str = input("Enter current date (YYYY-MM-DD): ")
            current_date = datetime.strptime(current_date_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD")  # I hate when dates are formatted wrong!
    
    # Now I'll calculate what date it was 10 years ago - simple math really
    past_date = current_date - timedelta(days=365*10)
    print(f"\nCalculating returns from {past_date.date()} to {current_date.date()}")
    
    # This is where I collect all the important numbers I need for the calculation
    try:
        # Getting the historical stock price
        past_price = float(input(f"\nEnter Apple stock price on {past_date.date()}: $"))
        # Getting today's price
        current_price = float(input(f"Enter current Apple stock price: $"))
        # How much money they want to invest
        initial_investment = float(input("Enter your initial investment amount: $"))
    except ValueError:
        print("Invalid input. Please enter numerical values.")  # Gotta catch those pesky invalid inputs!
        return
    
    # Here's where the magic happens - calculating how many shares they could've bought
    shares_bought = initial_investment / past_price
    
    # Now let's see what those shares are worth today
    current_value = shares_bought * current_price
    
    # I love this part - showing them how much money they made (or lost)
    total_return = current_value - initial_investment
    return_percentage = (total_return / initial_investment) * 100
    
    # This is a fancy calculation I learned about - CAGR shows the annual growth rate
    cagr = (pow(current_value / initial_investment, 1/10) - 1) * 100
    
    # Time to show off all the calculations I did!
    print("\nInvestment Analysis:")
    print("-" * 30)  # Another line for organization - I'm a bit obsessive about clean output
    print(f"Initial Investment: ${initial_investment:,.2f}")  # The :,.2f makes numbers look nice with commas
    print(f"Shares Purchased: {shares_bought:.2f}")
    print(f"Investment Value Today: ${current_value:,.2f}")
    print(f"Total Return: ${total_return:,.2f}")
    print(f"Return Percentage: {return_percentage:.2f}%")
    print(f"Compound Annual Growth Rate: {cagr:.2f}%")
    
    # I added some emoji to make it more fun - who doesn't love emoji?
    if total_return > 0:
        print("\nThis investment would have been profitable! 📈")
    else:
        print("\nThis investment would have resulted in a loss. 📉")
    
    # I thought it'd be cool to add a future projection too
    future_years = 5
    future_value = current_value * (1 + cagr/100)**future_years
    print(f"\nIf this growth rate continues, in {future_years} years your investment could be worth: ${future_value:,.2f}")

# This is my main program wrapper - I always include error handling because things can go wrong!
if __name__ == "__main__":
    try:
        calculate_investment_returns()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")  # In case someone hits Ctrl+C
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")  # Catch any other weird errors that might pop up