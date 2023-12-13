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
    city_flight = input("\nWhere are you flying to? (please enter 'Warsaw', 'Amsterdam' or 'Cape Town'): ")
    city_flight = city_flight.lower() # lowering the variable to ensure different input can be accepted
    if city_flight == "warsaw": 
        print("\nYou are going to Warsaw!") # prints the choice
        break # breaks the loop
    elif city_flight == "amsterdam":
        print("\nYou are going to Amsterdam!")
        break
    elif city_flight == "cape town":
        print("\nYou are going to Cape Town!") 
        break
    else:
        print("\nWrong input!!!")


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
        num_nights = int(input("\nHow many nights are you staying?: "))
        print("\nThank You!")
    except ValueError:
        print("\nWrong input, please enter a number!")
# making sure input can't be a negative number
    if num_nights < 0:
        print("\nNo negative numbers!")
        num_nights = 0
        continue

# Rent per night = 90
def hotel_cost(num_nights):
    sleeping_cost = num_nights * 90
    return sleeping_cost


# Calculating cost of the car
rental_days = 0

while rental_days == 0:
    try:
        rental_days = int(input("\nHow many days are you renting a car for?: "))
        print("\nThank You!")
    except ValueError:
        print("\nWrong input, please enter a number!")
# making sure input can't be a negative number
    if rental_days < 0:
        print("\nNo negative numbers!")
        rental_days = 0  
        continue 

# Rent per day = 69
def car_rental(rental_days):
    rent_cost = rental_days * 69
    return rent_cost


# Calculating the cost of the holiday
def holiday_cost(city_flight, num_nights, rental_days):
    p_cost = plane_cost(city_flight) 
    h_cost = hotel_cost(num_nights)
    r_cost = car_rental(rental_days)
    print("\nHoliday trip details:\n++++++++++++++++++++")
    print(f"Flight cost with a return ticket: £{p_cost}")
    print(f"\nHotel cost: £{h_cost}")
    print(f"\nCar rental cost: £{r_cost}")
    grand_total = p_cost + h_cost + r_cost
    return grand_total


# calling holiday_cost function, and assigning it to the variable total_holiday_cost
total_holiday_cost = holiday_cost(city_flight, num_nights, rental_days)

print(f"\nYour total holiday cost is: £{total_holiday_cost}\nEnjoy Your Trip!!!")