''' make a holiday calculator that will sum up 
cost of the plane(city_flight), 
hotel(num_nights),
and renting a car(rental_days). 
Ask user where are they flying to(each city different cost),
how many days they stay at the hotel,
and how many days they want to rent their car for. 
so 3 inputs - city_flight, num_nights, rental_days,

4 functions:
plane_cost - assign cost of the flight from the users choice
hotel_cost - make up price per night, and multiply by number of nights using num_nights input,
car_rental - make up price per day, multiply per number of days
holiday_cost - sum up hotel_cost, plane_cost, and car_rental to output final holiday cost,
 '''

print("You can fly to: \n (a) Warsaw (£156), \n (b) Amsterdam (£58), \n (c) Cape Town (£364),")
# user choosing flight
while True:
    city_flight = input("Where are you flying to? (please enter 'Warsaw', 'Amsterdam' or 'Cape Town'): ")
    city_flight = city_flight.lower() # lowering the variable to ensure different input can be accepted
    if city_flight == "warsaw": 
        print("You are going to Warsaw!\n") # prints the choice
        break # breaks the loop
    elif city_flight == "amsterdam":
        print("You are going to Amsterdam!\n")
        break
    elif city_flight == "cape town":
        print("You are going to Cape Town!\n") 
        break
    else:
        print("Wrong input!!!")


# Getting cost of the flight


def plane_cost(city_flight):
    if city_flight == "warsaw":
        return 156 * 2
    elif city_flight == "amsterdam":
        return 58 * 2
    elif city_flight == "cape town":
        return 364 * 2
    else:
        return 0


# Calculating cost of stay
num_nights = 0

while num_nights == 0:
    try:
        num_nights = int(input("How many nights are you staying?: "))
        print("Thank You!\n")
    except ValueError:
        print("Wrong input, please enter a number!\n")

# Rent per night = 90


def hotel_cost(num_nights):
    sleeping_cost = num_nights * 90
    return sleeping_cost


# Calculating cost of the car

rental_days = 0

while rental_days == 0:
    try:
        rental_days = int(input("How many days are you renting a car for?: "))
        print("Thank You!\n")
    except ValueError:
        print("Wrong input, please enter a number!\n")

# Rent per day = 69


def car_rental(rental_days):
    rent_cost = rental_days * 69
    return rent_cost


# Calculating the cost of the holiday


def holiday_cost(plane_cost,hotel_cost,car_rental):
    print("Holiday trip details:")
    pcost = int(plane_cost(city_flight))
    print(f"\nFlight cost with a return ticket: £{pcost}")
    hcost = int(hotel_cost(num_nights))
    print(f"\nHotel cost: £{hcost}")
    rcost = int(car_rental(rental_days))
    print(f"\nCar rental cost: £{rcost}")
    grand_total = pcost + hcost + rcost
    return grand_total


# calling holiday_cost function, and assigning it to the variable total_holiday_cost
total_holiday_cost = holiday_cost(plane_cost,hotel_cost,car_rental)

print(f"\nYou total holiday cost is: £{total_holiday_cost}\nEnjoy Your Trip!!!")

