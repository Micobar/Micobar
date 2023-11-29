import math

# menu bar
print("\n")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print("\n")
menu = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
menu = menu.lower()
if menu == "investment" or menu == "bond":
# investment section 
    if menu == "investment":
        print("\n")
        print("You chose investment option!")
        print("\n")
        deposit = float(input("How big is the deposit?: "))
        interest_rate = float(input("What is the percentage of the interest rate?: "))
        interest_rate = interest_rate / 100
        deplength = int(input("For how many years you want to deposit?: "))
        print("\n")
        #compound or simple plan
        print("Would you like a simple investment plan or compounding investment plan?")
        print("\n")
        interest = input("Type 'simple' or 'compound' to choose your interest plan: ")
        # simple plan
        if interest == "simple":
            print("\n")
            print("Simple investment plan:")
            depinterest = deposit *(1 + interest_rate*deplength) # calculating interest
            print(f"After {deplength} years you're going to have: {depinterest}")
            money = depinterest - deposit
            print(f" You will make: {money} after {deplength} years!")
            print("\n")
         # compound plan   
        elif interest == "compound":
            print("\n")
            print("Coumpound investment plan:")
            depinterest1 = deposit * math.pow((1 + interest_rate), + deplength) # calculating interest
            depinterest1 = int(depinterest1)
            print(f"After {deplength} years you're going to have: {depinterest1}")
            money = depinterest1 - deposit
            money = int(money)
            print(f" You will make: {money} after {deplength} years!")
            print("\n")
# bond section
    elif menu == "bond":
        print("\n")
        print("You chose bond option!")
        print("\n")
        house = float(input("What the value of the house?: "))
        hinterest_rate = float(input("What is the percenetage of the interest rate?: "))
        hinterest_rate = hinterest_rate / 100
        hinterest_rate = hinterest_rate / 12
        months = int(input("In how many moths you will repay your bond?: "))
        repay = (hinterest_rate * house)/(1- (1 + hinterest_rate)**( - months)) # calculating repayment
        repay = int(repay)
        print("\n")
        print(f"You will have to repay: {repay} interest only after {months} months!")
        print("\n")

else:
    print("Invalid entry!!!")       
