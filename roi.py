# INCOME = sum(rental, storage, misc) 
# EXPENSES = sum(taxes, ins, utilities, HOA, groundskeeping, vacancy, repairs, CapEx, property mgmt, mortgage)
# MONTHLY CASH FLOW = INCOME - EXPENSES
# TOTAL INVESTMENT  = sum(down payment, closing cost, repair budget, misc)
# ANNUAL ROI  = ((MONTHLY CASH FLOW) * 12) / TOTAL INVESTMENT - which will produce a float output


from IPython.display import clear_output

class Calc_ROI():
    ROI = 0
    incomes, expenses = 0, 0
    monthly_cash_flow = 0
    init_invest = 0
    rent_inc = 0    
    laundry_inc, storage_inc, pet_fee, misc = 0, 0, 0, 0
    taxes, ins, utils, mortgage, repairs, capEx = 0, 0, 0, 0, 0, 0
    HOA, lawncare, vacancy, prop_manage = 0, 0, 0, 0
    down_pay, closing_costs, rehab = 0, 0, 0

    def returnROI(self):
        while True:
            check = input("Do you have any monthly income on your property besides rent? Y/N: ")
            if check.lower().strip() == "y" or check.lower().strip() == "yes":
                while True:
                    try:
                        self.rent_inc = int(input("\nWhat is your income from renting? Please round amount to nearest whole dollar, or enter zero if none: "))
                        clear_output(wait = True)
                        break
                    except:
                        print("Invalid input, Please try again!\n")
                        clear_output(wait = True)
                while True:
                    try:
                        self.laundry_inc = int(input("\nWhat is your income from laundry? Please round amount to nearest whole dollar, or enter zero if none: "))
                        clear_output(wait = True)
                        break
                    except:
                        print("Invalid input, Please try again!\n")
                        clear_output(wait = True)
                while True:
                    try:
                        self.storage_inc = int(input("\nWhat is your income from storing/storage? Please round amount to nearest whole dollar, or enter zero if none: "))
                        clear_output(wait = True)
                        break
                    except:
                        print("Invalid input, Please try again!\n")
                        clear_output(wait = True)
                while True:
                    try:
                        self.pet_fee = int(input("\nWhat is your income from pet fees? Please round amount to nearest whole dollar, or enter zero if none: "))
                        clear_output(wait = True)
                        break
                    except:
                        print("Invalid input, Please try again!\n")
                        clear_output(wait = True)
                while True:
                    try:
                        self.misc = int(input("\nWhat is your income from miscellaneous sources? Please round amount to nearest whole dollar, or enter zero if none: "))
                        clear_output(wait = True)
                        break
                    except:
                        print("Invalid input, Please try again!\n")
                        clear_output(wait = True)
                self.incomes = self.rent_inc + self.laundry_inc + self.storage_inc + self.pet_fee + self.misc
                break
            elif check.lower().strip() == "n" or check.lower().strip() == "no":
                while True:
                    try:
                        self.rent_inc = int(input("\nWhat is your income from renting? Please round amount to nearest whole dollar, or enter zero if none: "))
                        clear_output(wait = True)
                        break
                    except:
                        print("Invalid input, Please try again!\n")
                        clear_output(wait = True)
                self.incomes = self.rent_inc
                break
            else:
                print("Invalid input, Please try again!\n")
                clear_output(wait = True)
        print(f"\nYour monthly income is ${self.incomes}.\n\n")
        while True:
            print("The main monthly expenses for rental properties are:\nTaxes\nInsurance\nUtilities\nMortgage\nRepairs\nCapital Expenditure")
            check2 = input("\nDo you have any monthly expenses on your property besides the ones above? Y/N: ")
            if check2.strip().lower() == "y" or check2.strip().lower() == "yes":
                while True:
                    try:
                        self.HOA = int(input("\nWhat are your monthly fees for the Home Owners Association? Please round amount to nearest whole dollar, or enter zero if none: "))
                        clear_output(wait = True)
                        break
                    except:
                        print("Invalid input, Please try again!\n")
                        clear_output(wait = True)
                while True:
                    try:
                        self.lawncare = int(input("\nWhat are your monthly fees for lawncare? Please round amount to nearest whole dollar, or enter zero if none: "))
                        clear_output(wait = True)
                        break
                    except:
                        print("Invalid input, Please try again!\n")
                        clear_output(wait = True)
                while True:
                    try:
                        self.vacancy = int(input("\nWhat are your monthly fees for vacancy savings? Please round amount to nearest whole dollar, or enter zero if none: "))
                        clear_output(wait = True)
                        break
                    except:
                        print("Invalid input, Please try again!\n")
                        clear_output(wait = True)
                while True:
                    try:
                        self.prop_manage = int(input("\nWhat are your monthly fees for property management? Please round amount to nearest whole dollar, or enter zero if none: "))
                        break
                    except:
                        print("Invalid input, Please try again!\n")
                        clear_output(wait = True)
                break
            elif check2.strip().lower() == "n" or check2.strip().lower() == "no":
                print("\nThank you, just checking!")
                clear_output(wait = True)
                break
            else:
                print("Invalid input, Please try again!\n")
                clear_output(wait = True)
        while True:
            try:
                self.taxes = int(input("\nWhat are your monthly expenses for taxes? Please round amount to nearest whole dollar, or enter zero if none: "))
                break
            except:
                print("Invalid input, Please try again!\n")
                clear_output(wait = True)
        while True:
            try:
                self.ins = int(input("\nWhat are your monthly expenses for insurance? Please round amount to nearest whole dollar, or enter zero if none: "))
                break
            except:
                print("Invalid input, Please try again!\n")
                clear_output(wait = True)
        while True:
            try:
                self.utils = int(input("\nWhat are your monthly expenses for utilities? Please round amount to nearest whole dollar, or enter zero if none: "))
                break
            except:
                print("Invalid input, Please try again!\n")
                clear_output(wait = True)
        while True:
            try:
                self.mortgage = int(input("\nWhat are your monthly expenses for your mortgage? Please round amount to nearest whole dollar, or enter zero if none: "))
                break
            except:
                print("Invalid input, Please try again!\n")
                clear_output(wait = True)
        while True:
            try:
                self.repairs = int(input("\nWhat are your monthly expenses for repairs? Please round amount to nearest whole dollar, or enter zero if none: "))
                break
            except:
                print("Invalid input, Please try again!\n")
                clear_output(wait = True)
        while True:
            try:
                self.capEx = int(input("\nWhat are your monthly expenses for capital expenditures? Please round amount to nearest whole dollar, or enter zero if none: "))
                break
            except:
                print("Invalid input, Please try again!\n")
                clear_output(wait = True)
        self.expenses = (self.taxes + self.ins + self.utils + self.mortgage + self.repairs + self.capEx + self.HOA + self.lawncare + self.vacancy + self.prop_manage)
        print(f"Your monthly expenses are ${self.expenses}.\n\n")
        self.monthly_cash_flow = self.incomes - self.expenses
        print("Great, now let's calculate your initial investment.\n")
        while True:
            try:
                self.down_pay = int(input("\nWhat was the down payment on the property? Please round amount to nearest whole dollar, or enter zero if none: "))
                clear_output(wait = True)
                break
            except:
                print("Invalid input, Please try again!\n")
                clear_output(wait = True)
        while True:
            try:
                self.closing_costs = int(input("\nWhat was the closing cost for the property? Please round amount to nearest whole dollar, or enter zero if none: "))
                clear_output(wait = True)
                break
            except:
                print("Invalid input, Please try again!\n")
                clear_output(wait = True)
        while True:
            try:
                self.rehab = int(input("\nWhat were your final expenses when rehabilitating the property? Please round amount to nearest whole dollar, or enter zero if none: "))
                clear_output(wait = True)
                break
            except:
                print("Invalid input, Please try again!\n")
                clear_output(wait = True)
        self.init_invest = self.down_pay + self.closing_costs + self.rehab
        print(f"\nYour initial investment was ${self.init_invest}.\n")
        print("\nCalculating your ROI...\n")
        self.ROI = (round(((self.monthly_cash_flow * 12)/self.init_invest) * 10000))/100
        print(f"\nYour Cash on Cash ROI is {self.ROI}% every year.\n")

test_calc = Calc_ROI()

def use_calc():
    print("Welcome to the ROI calculator!")
    name = input("What is your name?: ")
    while True:
        action = input("What would you like to do? ROI / quit: ")
        if action.lower().strip() == "roi":
            test_calc.returnROI()
            while True:
                option = input("\nWould you like to see any of the numbers again? Y/N: ")
                if option.lower().strip() == "y" or option.lower().strip() == "yes":
                    while True:
                        deep_option = input("Which number would you like to see: \nincome(type i) \nexpenses(type e) \ninitial investment (type in) \nROI (type r) \nor quit (type q)\n ")
                        if deep_option.lower().strip() == "income" or deep_option.lower().strip() == "i":
                            print(f"\nYour monthly income is ${test_calc.incomes}.\n")
                        elif deep_option.lower().strip() == "expenses" or deep_option.lower().strip() == "e":
                            print(f"\nYour monthly expenses are ${test_calc.expenses}.\n")
                        elif deep_option.lower().strip() == "initial investment" or deep_option.lower().strip() == "in":
                            print(f"\nYour initial investment was ${test_calc.init_invest}.\n")
                        elif deep_option.lower().strip() == "roi" or deep_option.lower().strip() == "r":
                            print(f"\nYour ROI is {test_calc.ROI}%.\n")
                        elif deep_option.lower().strip() == "q" or deep_option.lower().strip() == "quit":
                            print("\nHope this helps!\n")
                            break
                        else:
                            print("\nInvalid input, Please try again!\n")
                            clear_output(wait = True)
                    break
                elif option.strip().lower() == "n" or option.strip().lower() == "no":
                    print("\nOkay, just wanted to check!")
                    break
        elif action.lower().strip() == "quit":
            print(f"\n\nThanks for using the ROI calculator, {name.title()}!")
            break
        else:
            print("Invalid input, Please try again!\n")

use_calc()